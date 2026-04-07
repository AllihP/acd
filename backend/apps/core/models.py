from django.db import models


# ─── HELPERS ──────────────────────────────────────────────────────────────────

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# ─── PARAMÈTRES GÉNÉRAUX ───────────────────────────────────────────────────────

class SiteSettings(TimestampMixin):
    """Paramètres généraux du site (singleton)"""
    # Topbar
    topbar_fr = models.CharField("Topbar (FR)", max_length=200, default="ACD — Agence de Communication pour le Développement")
    topbar_en = models.CharField("Topbar (EN)", max_length=200, default="ACD — Agency for Communication and Development")
    topbar_ar = models.CharField("Topbar (AR)", max_length=200, default="وكالة الاتصال من أجل التنمية")
    # Infos de contact
    email = models.EmailField("Email", default="contact@acd-tchad.com")
    phone = models.CharField("Téléphone", max_length=30, default="+235 66 00 00 00")
    address_fr = models.CharField("Adresse (FR)", max_length=200, default="N'Djamena, Tchad")
    address_en = models.CharField("Adresse (EN)", max_length=200, default="N'Djamena, Chad")
    address_ar = models.CharField("Adresse (AR)", max_length=200, default="إنجامينا، تشاد")
    # Réseaux sociaux
    facebook  = models.URLField("Facebook",  blank=True)
    linkedin  = models.URLField("LinkedIn",  blank=True)
    twitter   = models.URLField("Twitter / X", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    youtube   = models.URLField("YouTube",   blank=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Paramètres du site"

    class Meta:
        verbose_name = "Paramètres du site"
        verbose_name_plural = "Paramètres du site"


# ─── HERO / ACCUEIL ────────────────────────────────────────────────────────────

class HeroSection(TimestampMixin):
    """Section d'accueil (Hero)"""
    # Label de l'eyebrow
    label_fr = models.CharField("Label eyebrow (FR)", max_length=100, default="Agence 360° — N'Djamena, Tchad")
    label_en = models.CharField("Label eyebrow (EN)", max_length=100, default="360° Agency — N'Djamena, Chad")
    label_ar = models.CharField("Label eyebrow (AR)", max_length=100, default="وكالة 360° — إنجامينا، تشاد")
    # Titre principal
    title_fr = models.CharField("Titre (FR)", max_length=200, default="Communication. Stratégie. Impact.")
    title_en = models.CharField("Titre (EN)", max_length=200, default="Communication. Strategy. Impact.")
    title_ar = models.CharField("Titre (AR)", max_length=200, default="التواصل. الاستراتيجية. الأثر.")
    # Sous-titre
    subtitle_fr = models.TextField("Sous-titre (FR)", default="Nous bâtissons des marques qui inspirent.")
    subtitle_en = models.TextField("Sous-titre (EN)", default="We build brands that inspire.")
    subtitle_ar = models.TextField("Sous-titre (AR)", default="نبني علامات تجارية ملهمة.")
    # Boutons CTA
    cta1_fr = models.CharField("CTA principal (FR)", max_length=80, default="Démarrer un projet")
    cta1_en = models.CharField("CTA principal (EN)", max_length=80, default="Start a Project")
    cta1_ar = models.CharField("CTA principal (AR)", max_length=80, default="ابدأ مشروعك")
    cta2_fr = models.CharField("CTA secondaire (FR)", max_length=80, default="Voir nos réalisations")
    cta2_en = models.CharField("CTA secondaire (EN)", max_length=80, default="View Our Work")
    cta2_ar = models.CharField("CTA secondaire (AR)", max_length=80, default="شاهد أعمالنا")
    # Stats
    stat1_value  = models.PositiveIntegerField("Stat 1 — Valeur", default=120)
    stat1_label_fr = models.CharField("Stat 1 — Label (FR)", max_length=60, default="Projets réussis")
    stat1_label_en = models.CharField("Stat 1 — Label (EN)", max_length=60, default="Successful Projects")
    stat1_label_ar = models.CharField("Stat 1 — Label (AR)", max_length=60, default="مشروع ناجح")
    stat2_value  = models.PositiveIntegerField("Stat 2 — Valeur", default=8)
    stat2_label_fr = models.CharField("Stat 2 — Label (FR)", max_length=60, default="Années d'expertise")
    stat2_label_en = models.CharField("Stat 2 — Label (EN)", max_length=60, default="Years of Expertise")
    stat2_label_ar = models.CharField("Stat 2 — Label (AR)", max_length=60, default="سنوات من الخبرة")
    stat3_value  = models.PositiveIntegerField("Stat 3 — Valeur", default=98)
    stat3_label_fr = models.CharField("Stat 3 — Label (FR)", max_length=60, default="% clients satisfaits")
    stat3_label_en = models.CharField("Stat 3 — Label (EN)", max_length=60, default="% Satisfied Clients")
    stat3_label_ar = models.CharField("Stat 3 — Label (AR)", max_length=60, default="% رضا العملاء")
    # Image de fond
    bg_image     = models.ImageField("Image de fond", upload_to='hero/', blank=True, null=True)
    is_published = models.BooleanField("Publié", default=True)

    def __str__(self):
        return f"Hero — {self.title_fr[:50]}"

    class Meta:
        verbose_name = "Section Accueil (Hero)"
        verbose_name_plural = "Section Accueil (Hero)"


# ─── À PROPOS ─────────────────────────────────────────────────────────────────

class AboutSection(TimestampMixin):
    """Section À propos"""
    eyebrow_fr = models.CharField("Eyebrow (FR)", max_length=100, default="— Notre histoire")
    eyebrow_en = models.CharField("Eyebrow (EN)", max_length=100, default="— Our Story")
    eyebrow_ar = models.CharField("Eyebrow (AR)", max_length=100, default="— قصتنا")
    title_fr   = models.CharField("Titre (FR)", max_length=200, default="Nés à N'Djamena. Rayonnons en Afrique.")
    title_en   = models.CharField("Titre (EN)", max_length=200, default="Born in N'Djamena. Shining across Africa.")
    title_ar   = models.CharField("Titre (AR)", max_length=200, default="وُلدنا في إنجامينا. نتألق في أفريقيا.")
    text_fr    = models.TextField("Texte (FR)")
    text_en    = models.TextField("Texte (EN)")
    text_ar    = models.TextField("Texte (AR)")
    # Faits clés
    fact1_label_fr = models.CharField("Fait 1 — Label (FR)", max_length=60, default="Équipe")
    fact1_label_en = models.CharField("Fait 1 — Label (EN)", max_length=60, default="Team")
    fact1_label_ar = models.CharField("Fait 1 — Label (AR)", max_length=60, default="الفريق")
    fact1_value_fr = models.CharField("Fait 1 — Valeur (FR)", max_length=80, default="18 talents passionnés")
    fact1_value_en = models.CharField("Fait 1 — Valeur (EN)", max_length=80, default="18 passionate talents")
    fact1_value_ar = models.CharField("Fait 1 — Valeur (AR)", max_length=80, default="18 موهبة متحمسة")

    fact2_label_fr = models.CharField("Fait 2 — Label (FR)", max_length=60, default="Siège")
    fact2_label_en = models.CharField("Fait 2 — Label (EN)", max_length=60, default="HQ")
    fact2_label_ar = models.CharField("Fait 2 — Label (AR)", max_length=60, default="المقر")
    fact2_value_fr = models.CharField("Fait 2 — Valeur (FR)", max_length=80, default="N'Djamena, Tchad")
    fact2_value_en = models.CharField("Fait 2 — Valeur (EN)", max_length=80, default="N'Djamena, Chad")
    fact2_value_ar = models.CharField("Fait 2 — Valeur (AR)", max_length=80, default="إنجامينا، تشاد")

    fact3_label_fr = models.CharField("Fait 3 — Label (FR)", max_length=60, default="Mission")
    fact3_label_en = models.CharField("Fait 3 — Label (EN)", max_length=60, default="Mission")
    fact3_label_ar = models.CharField("Fait 3 — Label (AR)", max_length=60, default="المهمة")
    fact3_value_fr = models.CharField("Fait 3 — Valeur (FR)", max_length=120, default="Faire briller le Tchad sur la scène mondiale")
    fact3_value_en = models.CharField("Fait 3 — Valeur (EN)", max_length=120, default="Putting Chad on the world stage")
    fact3_value_ar = models.CharField("Fait 3 — Valeur (AR)", max_length=120, default="إبراز تشاد على الساحة العالمية")

    fact4_label_fr = models.CharField("Fait 4 — Label (FR)", max_length=60, default="Vision")
    fact4_label_en = models.CharField("Fait 4 — Label (EN)", max_length=60, default="Vision")
    fact4_label_ar = models.CharField("Fait 4 — Label (AR)", max_length=60, default="الرؤية")
    fact4_value_fr = models.CharField("Fait 4 — Valeur (FR)", max_length=120, default="L'agence de référence en Afrique centrale")
    fact4_value_en = models.CharField("Fait 4 — Valeur (EN)", max_length=120, default="The reference agency in Central Africa")
    fact4_value_ar = models.CharField("Fait 4 — Valeur (AR)", max_length=120, default="الوكالة المرجعية في وسط أفريقيا")

    cta_fr = models.CharField("CTA (FR)", max_length=80, default="Rejoignez l'aventure")
    cta_en = models.CharField("CTA (EN)", max_length=80, default="Join the Adventure")
    cta_ar = models.CharField("CTA (AR)", max_length=80, default="انضم إلى المغامرة")

    image       = models.ImageField("Photo principale", upload_to='about/', blank=True, null=True)
    years_exp   = models.PositiveIntegerField("Années d'expertise (badge)", default=8)
    is_published = models.BooleanField("Publié", default=True)

    def __str__(self):
        return f"À propos — {self.title_fr[:50]}"

    class Meta:
        verbose_name = "Section À propos"
        verbose_name_plural = "Section À propos"


# ─── SERVICES / PROJETS ────────────────────────────────────────────────────────

class Service(TimestampMixin):
    """Nos expertises / Services"""
    icon       = models.CharField("Icône FontAwesome", max_length=50, default="fas fa-star",
                                   help_text="Ex: fas fa-bullhorn, fas fa-palette, fas fa-globe")
    title_fr   = models.CharField("Titre (FR)", max_length=100)
    title_en   = models.CharField("Titre (EN)", max_length=100)
    title_ar   = models.CharField("Titre (AR)", max_length=100)
    text_fr    = models.TextField("Description (FR)")
    text_en    = models.TextField("Description (EN)")
    text_ar    = models.TextField("Description (AR)")
    order      = models.PositiveIntegerField("Ordre d'affichage", default=0)
    is_active  = models.BooleanField("Actif", default=True)

    def __str__(self):
        return self.title_fr

    class Meta:
        verbose_name = "Service / Expertise"
        verbose_name_plural = "Services / Expertises"
        ordering = ['order']


# ─── POURQUOI NOUS — PILIERS ───────────────────────────────────────────────────

class WhyItem(TimestampMixin):
    """Raisons de nous choisir (section Pourquoi ACD)"""
    icon       = models.CharField("Icône FontAwesome", max_length=50, default="fas fa-check")
    title_fr   = models.CharField("Titre (FR)", max_length=100)
    title_en   = models.CharField("Titre (EN)", max_length=100)
    title_ar   = models.CharField("Titre (AR)", max_length=100)
    text_fr    = models.TextField("Texte (FR)")
    text_en    = models.TextField("Texte (EN)")
    text_ar    = models.TextField("Texte (AR)")
    order      = models.PositiveIntegerField("Ordre", default=0)
    is_active  = models.BooleanField("Actif", default=True)

    def __str__(self):
        return self.title_fr

    class Meta:
        verbose_name = "Raison / Pilier"
        verbose_name_plural = "Raisons / Piliers (Pourquoi ACD)"
        ordering = ['order']


# ─── PORTFOLIO / RÉALISATIONS ──────────────────────────────────────────────────

CATEGORY_CHOICES = [
    ('branding',    'Branding & Identité'),
    ('digital',     'Marketing Digital'),
    ('evenement',   'Événement'),
    ('print',       'Print & Édition'),
    ('social',      'Social Media'),
    ('audiovisuel', 'Audiovisuel'),
]

class PortfolioItem(TimestampMixin):
    """Réalisations / Portfolio"""
    title_fr     = models.CharField("Titre (FR)", max_length=150)
    title_en     = models.CharField("Titre (EN)", max_length=150)
    title_ar     = models.CharField("Titre (AR)", max_length=150)
    category     = models.CharField("Catégorie", max_length=30, choices=CATEGORY_CHOICES)
    description_fr = models.TextField("Description (FR)", blank=True)
    description_en = models.TextField("Description (EN)", blank=True)
    description_ar = models.TextField("Description (AR)", blank=True)
    client       = models.CharField("Client", max_length=100, blank=True)
    year         = models.PositiveIntegerField("Année", default=2024)
    image        = models.ImageField("Image principale", upload_to='portfolio/')
    is_featured  = models.BooleanField("Mis en avant", default=False)
    is_active    = models.BooleanField("Actif", default=True)
    order        = models.PositiveIntegerField("Ordre", default=0)

    def __str__(self):
        return self.title_fr

    class Meta:
        verbose_name = "Réalisation"
        verbose_name_plural = "Réalisations (Portfolio)"
        ordering = ['-is_featured', 'order', '-year']


# ─── TÉMOIGNAGES ──────────────────────────────────────────────────────────────

class Testimonial(TimestampMixin):
    """Témoignages clients"""
    author    = models.CharField("Auteur", max_length=100)
    role_fr   = models.CharField("Rôle (FR)", max_length=120)
    role_en   = models.CharField("Rôle (EN)", max_length=120)
    role_ar   = models.CharField("Rôle (AR)", max_length=120)
    company   = models.CharField("Entreprise", max_length=100, blank=True)
    text_fr   = models.TextField("Témoignage (FR)")
    text_en   = models.TextField("Témoignage (EN)")
    text_ar   = models.TextField("Témoignage (AR)")
    avatar    = models.ImageField("Photo", upload_to='testimonials/', blank=True, null=True)
    rating    = models.PositiveIntegerField("Note (1-5)", default=5)
    is_active = models.BooleanField("Actif", default=True)
    order     = models.PositiveIntegerField("Ordre", default=0)

    def __str__(self):
        return f"{self.author} — {self.company}"

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['order']
