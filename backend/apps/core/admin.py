from django.contrib import admin
from django.utils.html import format_html, mark_safe
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from .models import (
    SiteSettings, HeroSection, AboutSection,
    Service, WhyItem, PortfolioItem, Testimonial
)


# ── MIXIN Aperçu image ────────────────────────────────────────────────
class ImagePreviewMixin:
    @display(description="Aperçu")
    def image_preview(self, obj):
        img = getattr(obj, 'image', None) or getattr(obj, 'bg_image', None) or getattr(obj, 'avatar', None)
        if img:
            return format_html(
                '<img src="{}" style="height:70px;border-radius:8px;object-fit:cover;'
                'box-shadow:0 2px 8px rgba(0,0,0,.15);" />',
                img.url
            )
        return mark_safe('<span style="color:#9ca3af;font-style:italic;">Aucune image</span>')


# ── SITE SETTINGS ─────────────────────────────────────────────────────
@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True

    fieldsets = (
        ("🌐 Texte Topbar", {
            "fields": ("topbar_fr", "topbar_en", "topbar_ar"),
            "classes": ["tab"],
        }),
        ("📞 Coordonnées", {
            "fields": ("email", "phone", "address_fr", "address_en", "address_ar"),
            "classes": ["tab"],
        }),
        ("📱 Réseaux sociaux", {
            "fields": ("facebook", "linkedin", "twitter", "instagram", "youtube"),
            "classes": ["tab"],
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ── HERO SECTION ─────────────────────────────────────────────────────
@admin.register(HeroSection)
class HeroSectionAdmin(ImagePreviewMixin, ModelAdmin):
    list_display   = ("title_fr", "is_published", "image_preview", "updated_at")
    list_filter    = ("is_published",)
    list_editable  = ("is_published",)
    readonly_fields = ("image_preview", "created_at", "updated_at")
    warn_unsaved_form = True
    compressed_fields = True

    fieldsets = (
        ("🟢 Statut", {
            "fields": ("is_published",),
            "classes": ["tab"],
        }),
        ("🇫🇷 Français", {
            "fields": ("label_fr", "title_fr", "subtitle_fr", "cta1_fr", "cta2_fr"),
            "classes": ["tab"],
        }),
        ("🇬🇧 English", {
            "fields": ("label_en", "title_en", "subtitle_en", "cta1_en", "cta2_en"),
            "classes": ["tab"],
        }),
        ("🇸🇦 العربية", {
            "fields": ("label_ar", "title_ar", "subtitle_ar", "cta1_ar", "cta2_ar"),
            "classes": ["tab"],
        }),
        ("📊 Statistiques", {
            "fields": (
                ("stat1_value", "stat1_label_fr", "stat1_label_en", "stat1_label_ar"),
                ("stat2_value", "stat2_label_fr", "stat2_label_en", "stat2_label_ar"),
                ("stat3_value", "stat3_label_fr", "stat3_label_en", "stat3_label_ar"),
            ),
            "classes": ["tab"],
        }),
        ("🖼️ Image de fond", {
            "fields": ("bg_image", "image_preview"),
            "classes": ["tab"],
        }),
    )


# ── ABOUT SECTION ────────────────────────────────────────────────────
@admin.register(AboutSection)
class AboutSectionAdmin(ImagePreviewMixin, ModelAdmin):
    list_display  = ("title_fr", "is_published", "years_exp", "updated_at")
    list_filter   = ("is_published",)
    readonly_fields = ("image_preview", "created_at", "updated_at")
    warn_unsaved_form = True
    compressed_fields = True

    fieldsets = (
        ("🟢 Statut", {
            "fields": ("is_published", "years_exp"),
            "classes": ["tab"],
        }),
        ("🇫🇷 Français", {
            "fields": ("eyebrow_fr", "title_fr", "text_fr", "cta_fr"),
            "classes": ["tab"],
        }),
        ("🇬🇧 English", {
            "fields": ("eyebrow_en", "title_en", "text_en", "cta_en"),
            "classes": ["tab"],
        }),
        ("🇸🇦 العربية", {
            "fields": ("eyebrow_ar", "title_ar", "text_ar", "cta_ar"),
            "classes": ["tab"],
        }),
        ("📌 Faits clés", {
            "fields": (
                ("fact1_label_fr", "fact1_label_en", "fact1_label_ar"),
                ("fact1_value_fr", "fact1_value_en", "fact1_value_ar"),
                ("fact2_label_fr", "fact2_label_en", "fact2_label_ar"),
                ("fact2_value_fr", "fact2_value_en", "fact2_value_ar"),
                ("fact3_label_fr", "fact3_label_en", "fact3_label_ar"),
                ("fact3_value_fr", "fact3_value_en", "fact3_value_ar"),
                ("fact4_label_fr", "fact4_label_en", "fact4_label_ar"),
                ("fact4_value_fr", "fact4_value_en", "fact4_value_ar"),
            ),
            "classes": ["tab"],
        }),
        ("🖼️ Image", {
            "fields": ("image", "image_preview"),
            "classes": ["tab"],
        }),
    )


# ── SERVICE ──────────────────────────────────────────────────────────
@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display  = ("icon_display", "title_fr", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter   = ("is_active",)
    search_fields = ("title_fr", "title_en")
    compressed_fields = True

    fieldsets = (
        ("⚙️ Configuration", {
            "fields": ("icon", "order", "is_active"),
            "classes": ["tab"],
        }),
        ("🇫🇷 Français", {
            "fields": ("title_fr", "text_fr"),
            "classes": ["tab"],
        }),
        ("🇬🇧 English", {
            "fields": ("title_en", "text_en"),
            "classes": ["tab"],
        }),
        ("🇸🇦 العربية", {
            "fields": ("title_ar", "text_ar"),
            "classes": ["tab"],
        }),
    )

    @display(description="Icône")
    def icon_display(self, obj):
        return format_html(
            '<i class="{}" style="font-size:1.2rem;color:#0C1931;margin-right:8px;"></i>'
            '<code style="font-size:.75rem;color:#64748b;">{}</code>',
            obj.icon, obj.icon
        )


# ── WHY ITEM ─────────────────────────────────────────────────────────
@admin.register(WhyItem)
class WhyItemAdmin(ModelAdmin):
    list_display  = ("icon_display", "title_fr", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter   = ("is_active",)
    compressed_fields = True

    fieldsets = (
        ("⚙️ Config", {"fields": ("icon", "order", "is_active"), "classes": ["tab"]}),
        ("🇫🇷 Français", {"fields": ("title_fr", "text_fr"), "classes": ["tab"]}),
        ("🇬🇧 English",  {"fields": ("title_en", "text_en"), "classes": ["tab"]}),
        ("🇸🇦 العربية",  {"fields": ("title_ar", "text_ar"), "classes": ["tab"]}),
    )

    @display(description="Icône")
    def icon_display(self, obj):
        return format_html(
            '<i class="{}" style="color:#6AAB2E;font-size:1.2rem;"></i>',
            obj.icon
        )


# ── PORTFOLIO ────────────────────────────────────────────────────────
@admin.register(PortfolioItem)
class PortfolioItemAdmin(ImagePreviewMixin, ModelAdmin):
    list_display  = ("image_preview", "title_fr", "category_badge", "client",
                     "year", "is_featured", "is_active", "order")
    list_editable = ("is_featured", "is_active", "order")
    list_filter   = ("category", "is_featured", "is_active", "year")
    search_fields = ("title_fr", "title_en", "client")
    readonly_fields = ("image_preview", "created_at", "updated_at")
    compressed_fields = True

    fieldsets = (
        ("📁 Infos générales", {
            "fields": ("category", "client", "year", "order", "is_featured", "is_active"),
            "classes": ["tab"],
        }),
        ("🇫🇷 Français", {
            "fields": ("title_fr", "description_fr"),
            "classes": ["tab"],
        }),
        ("🇬🇧 English", {
            "fields": ("title_en", "description_en"),
            "classes": ["tab"],
        }),
        ("🇸🇦 العربية", {
            "fields": ("title_ar", "description_ar"),
            "classes": ["tab"],
        }),
        ("🖼️ Image", {
            "fields": ("image", "image_preview"),
            "classes": ["tab"],
        }),
    )

    @display(description="Catégorie")
    def category_badge(self, obj):
        colors = {
            'branding': '#C9A84C', 'digital': '#3A5F8A',
            'evenement': '#6AAB2E', 'print': '#8B5CF6',
            'social': '#F59E0B', 'audiovisuel': '#EF4444',
        }
        color = colors.get(obj.category, '#64748B')
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 10px;'
            'border-radius:9999px;font-size:.75rem;font-weight:600;">{}</span>',
            color, obj.get_category_display()
        )


# ── TESTIMONIAL ──────────────────────────────────────────────────────
@admin.register(Testimonial)
class TestimonialAdmin(ImagePreviewMixin, ModelAdmin):
    list_display  = ("image_preview", "author", "company", "rating_stars", "is_active", "order")
    list_editable = ("is_active", "order")
    list_filter   = ("is_active", "rating")
    search_fields = ("author", "company")
    readonly_fields = ("image_preview",)
    compressed_fields = True

    fieldsets = (
        ("👤 Auteur", {
            "fields": ("author", "company", "rating", "order", "is_active", "avatar", "image_preview"),
            "classes": ["tab"],
        }),
        ("🇫🇷 Français", {
            "fields": ("role_fr", "text_fr"),
            "classes": ["tab"],
        }),
        ("🇬🇧 English", {
            "fields": ("role_en", "text_en"),
            "classes": ["tab"],
        }),
        ("🇸🇦 العربية", {
            "fields": ("role_ar", "text_ar"),
            "classes": ["tab"],
        }),
    )

    @display(description="Note")
    def rating_stars(self, obj):
        stars = '★' * obj.rating + '☆' * (5 - obj.rating)
        return format_html(
            '<span style="color:#C9A84C;font-size:1rem;">{}</span>', stars
        )
