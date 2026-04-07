from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    SiteSettings, HeroSection, AboutSection,
    Service, WhyItem, PortfolioItem, Testimonial
)
from .serializers import (
    SiteSettingsSerializer, HeroSectionSerializer, AboutSectionSerializer,
    ServiceSerializer, WhyItemSerializer, PortfolioItemSerializer, TestimonialSerializer
)


class SiteSettingsView(APIView):
    def get(self, request):
        settings = SiteSettings.load()
        serializer = SiteSettingsSerializer(settings)
        return Response(serializer.data)


class HeroView(APIView):
    def get(self, request):
        hero = HeroSection.objects.filter(is_published=True).last()
        if not hero:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = HeroSectionSerializer(hero, context={'request': request})
        return Response(serializer.data)


class AboutView(APIView):
    def get(self, request):
        about = AboutSection.objects.filter(is_published=True).last()
        if not about:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        serializer = AboutSectionSerializer(about, context={'request': request})
        return Response(serializer.data)


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class WhyItemListView(generics.ListAPIView):
    queryset = WhyItem.objects.filter(is_active=True)
    serializer_class = WhyItemSerializer


class PortfolioListView(generics.ListAPIView):
    serializer_class = PortfolioItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'is_featured']

    def get_queryset(self):
        return PortfolioItem.objects.filter(is_active=True)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class TestimonialListView(generics.ListAPIView):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class AllDataView(APIView):
    """Endpoint unique qui retourne toutes les données du site"""
    def get(self, request):
        data = {
            'settings':     SiteSettingsSerializer(SiteSettings.load()).data,
            'hero':         HeroSectionSerializer(
                                HeroSection.objects.filter(is_published=True).last(),
                                context={'request': request}).data
                            if HeroSection.objects.filter(is_published=True).exists() else {},
            'about':        AboutSectionSerializer(
                                AboutSection.objects.filter(is_published=True).last(),
                                context={'request': request}).data
                            if AboutSection.objects.filter(is_published=True).exists() else {},
            'services':     ServiceSerializer(
                                Service.objects.filter(is_active=True), many=True).data,
            'why_items':    WhyItemSerializer(
                                WhyItem.objects.filter(is_active=True), many=True).data,
            'portfolio':    PortfolioItemSerializer(
                                PortfolioItem.objects.filter(is_active=True),
                                many=True, context={'request': request}).data,
            'testimonials': TestimonialSerializer(
                                Testimonial.objects.filter(is_active=True),
                                many=True, context={'request': request}).data,
        }
        return Response(data)
