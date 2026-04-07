from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display  = (
        "name", "email", "phone",
        "service_badge", "lang_flag",
        "is_read", "is_replied",   # ← doivent être ici pour list_editable
        "created_at"
    )
    list_filter   = ("is_read", "is_replied", "service", "lang")
    search_fields = ("name", "email", "company", "message")
    readonly_fields = (
        "name", "email", "phone", "company",
        "service", "message", "lang", "created_at"
    )
    list_editable = ("is_read", "is_replied")
    date_hierarchy = "created_at"
    ordering      = ["-created_at"]
    compressed_fields = True

    fieldsets = (
        ("👤 Expéditeur", {
            "fields": ("name", "email", "phone", "company", "lang"),
            "classes": ["tab"],
        }),
        ("📋 Demande", {
            "fields": ("service", "message"),
            "classes": ["tab"],
        }),
        ("✅ Suivi", {
            "fields": ("is_read", "is_replied", "created_at"),
            "classes": ["tab"],
        }),
    )

    def has_add_permission(self, request):
        return False

    @display(description="Service")
    def service_badge(self, obj):
        colors = {
            "branding":    "#C9A84C",
            "digital":     "#3A5F8A",
            "evenement":   "#6AAB2E",
            "print":       "#8B5CF6",
            "social":      "#F59E0B",
            "audiovisuel": "#EF4444",
            "conseil":     "#0C1931",
            "autre":       "#64748B",
        }
        color = colors.get(obj.service, "#64748B")
        label = obj.get_service_display() if obj.service else "—"
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 10px;'
            'border-radius:9999px;font-size:.75rem;font-weight:600;">{}</span>',
            color, label
        )

    @display(description="Langue")
    def lang_flag(self, obj):
        flags = {"fr": "🇫🇷", "en": "🇬🇧", "ar": "🇸🇦"}
        return flags.get(obj.lang, "🌐")
