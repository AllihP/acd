from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([AllowAny])  # ← Autorise l'envoi sans connexion
def contact_view(request):
    # Votre logique d'envoi d'email / sauvegarde ici
    return Response({'message': 'Message envoyé avec succès'}, status=status.HTTP_200_OK)