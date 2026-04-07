from django.urls import path
from .views import (
    SiteSettingsView, HeroView, AboutView,
    ServiceListView, WhyItemListView,
    PortfolioListView, TestimonialListView,
    AllDataView
)

urlpatterns = [
    path('settings/',     SiteSettingsView.as_view(),    name='site-settings'),
    path('hero/',         HeroView.as_view(),             name='hero'),
    path('about/',        AboutView.as_view(),            name='about'),
    path('services/',     ServiceListView.as_view(),      name='services'),
    path('why/',          WhyItemListView.as_view(),      name='why-items'),
    path('portfolio/',    PortfolioListView.as_view(),    name='portfolio'),
    path('testimonials/', TestimonialListView.as_view(),  name='testimonials'),
    path('all/',          AllDataView.as_view(),          name='all-data'),
]
