from django.urls import path
from .views import contact_message_view  # ← Nom exact de la fonction ci-dessus

app_name = 'contact'

urlpatterns = [
    # Endpoint pour le formulaire de contact
    path('contact/', contact_message_view, name='contact_message'),
]