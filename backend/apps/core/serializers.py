from rest_framework import serializers
from .models import (
    SiteSettings, HeroSection, AboutSection,
    Service, WhyItem, PortfolioItem, Testimonial
)


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = '__all__'


class HeroSectionSerializer(serializers.ModelSerializer):
    bg_image_url = serializers.SerializerMethodField()

    class Meta:
        model = HeroSection
        exclude = ['bg_image']

    def get_bg_image_url(self, obj):
        request = self.context.get('request')
        if obj.bg_image and request:
            return request.build_absolute_uri(obj.bg_image.url)
        return None


class AboutSectionSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutSection
        exclude = ['image']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class WhyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyItem
        fields = '__all__'


class PortfolioItemSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category_display = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = PortfolioItem
        exclude = ['image']

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class TestimonialSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        exclude = ['avatar']

    def get_avatar_url(self, obj):
        request = self.context.get('request')
        if obj.avatar and request:
            return request.build_absolute_uri(obj.avatar.url)
        return None
