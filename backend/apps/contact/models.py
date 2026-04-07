from django.db import models

SERVICE_CHOICES = [
    ('branding',     'Branding & Identité visuelle'),
    ('digital',      'Marketing Digital'),
    ('evenement',    'Événementiel'),
    ('print',        'Print & Édition'),
    ('social',       'Social Media & Community'),
    ('audiovisuel',  'Audiovisuel & Production'),
    ('conseil',      'Conseil Stratégique'),
    ('autre',        'Autre'),
]

class ContactMessage(models.Model):
    name      = models.CharField("Nom complet", max_length=120)
    email     = models.EmailField("Email")
    phone     = models.CharField("Téléphone", max_length=30)
    company   = models.CharField("Entreprise / Organisation", max_length=120, blank=True)
    service   = models.CharField("Service souhaité", max_length=30, choices=SERVICE_CHOICES, blank=True)
    message   = models.TextField("Message")
    lang      = models.CharField("Langue", max_length=5, default='fr')
    is_read   = models.BooleanField("Lu", default=False)
    is_replied = models.BooleanField("Répondu", default=False)
    created_at = models.DateTimeField("Reçu le", auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.email} ({self.created_at.strftime('%d/%m/%Y')})"

    class Meta:
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"
        ordering = ['-created_at']
