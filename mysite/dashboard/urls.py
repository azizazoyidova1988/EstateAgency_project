from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('country/list/', views.countries_list, name="countries_list"),
    path('country/add/', views.countries_create, name="countries_add"),
    path('country/<int:country_id>/edit/', views.countries_edit, name="countries_edit"),
    path('country/<int:country_id>/delete/', views.countries_delete, name="countries_delete"),

    path('category/list/', views.categories_list, name="categories_list"),
    path('category/add/', views.categories_create, name="categories_add"),
    path('category/<int:category_id>/edit/', views.categories_edit, name="categories_edit"),
    path('category/<int:category_id>/delete/', views.categories_delete,name="categories_delete"),

    path('product/list/', views.products_list, name="products_list"),
    path('product/add/', views.products_create, name="products_add"),
    path('product/<int:product_id>/edit/', views.products_edit, name="products_edit"),
    path('product/<int:product_id>/delete/', views.products_delete, name="products_delete"),

    path('agent/list/', views.agents_list, name="agents_list"),
    path('agent/add/', views.agents_create, name="agents_add"),
    path('agent/<int:agent_id>/edit/', views.agents_edit, name="agents_edit"),
    path('agent/<int:agent_id>/delete/', views.agents_delete, name="agents_delete"),

    path('news/list/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="news_add"),
    path('news/<int:news_id>/edit/', views.news_edit, name="news_edit"),
    path('news/<int:news_id>/delete/', views.news_delete, name="news_delete"),

    path('testimonials/list/', views.testimonials_list, name="testimonials_list"),
    path('testimonials/add/', views.testimonials_create, name="testimonials_add"),
    path('testimonials/<int:testimonial_id>/edit/', views.testimonials_edit, name="testimonials_edit"),
    path('testimonials/<int:testimonial_id>/delete/', views.testimonials_delete, name="testimonials_delete"),



   ]