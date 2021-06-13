from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('agent_single/', views.agent_single, name='agent-single'),
    path('property/', views.property, name='property'),
    path('property_single/', views.property_single, name='property-single'),
    path('blog/', views.blog, name='blog'),
    path('blog_single', views.blog_single, name='blog-single'),
    path('contact', views.contact, name='contact'),
]
