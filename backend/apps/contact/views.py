from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])  # ← Autorise l'envoi sans authentification
def contact_message_view(request):
    """
    Endpoint pour recevoir les messages du formulaire de contact.
    POST /api/contact/contact/
    """
    try:
        # Récupération des données
        name = request.data.get('name', '').strip()
        email = request.data.get('email', '').strip()
        phone = request.data.get('phone', '').strip()
        company = request.data.get('company', '').strip()
        service = request.data.get('service', '').strip()
        message = request.data.get('message', '').strip()
        lang = request.data.get('lang', 'fr')

        # Validation minimale
        if not name or not email or not message:
            return Response(
                {'error': 'Name, email and message are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ✅ Option 1 : Envoi d'email (si configuré)
        try:
            if getattr(settings, 'DEFAULT_FROM_EMAIL', None) and settings.DEFAULT_FROM_EMAIL:
                send_mail(
                    subject=f'Nouveau contact depuis ACD ({name})',
                    message=f"""
Nom: {name}
Email: {email}
Téléphone: {phone}
Entreprise: {company}
Service: {service}
Langue: {lang}

Message:
{message}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,  # Ne pas bloquer si l'email échoue
                )
        except Exception as e:
            logger.warning(f"Failed to send email notification: {str(e)}")
            # We continue execution to save in database

        # ✅ Option 2 : Sauvegarde en base (décommentez si vous avez un modèle)
        try:
            from .models import ContactMessage
            ContactMessage.objects.create(
                name=name, email=email, phone=phone,
                company=company, service=service, message=message, lang=lang
            )
            logger.info(f"Contact message received and saved from {email}")
        except Exception as e:
            logger.error(f"Failed to save contact message to database: {str(e)}")
            return Response(
                {'error': 'Erreur lors de la sauvegarde du message en base de données'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {'message': 'Message reçu avec succès'},
            status=status.HTTP_200_OK
        )

    except Exception as e:
        logger.error(f"Contact form error: {str(e)}")
        return Response(
            {'error': 'Une erreur interne est survenue'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )