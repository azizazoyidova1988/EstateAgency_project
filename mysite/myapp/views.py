from django.shortcuts import render
from . import services
from myapp.models import Product


def home(request):
    products = services.get_products()
    service = services.get_services()
    latest_products = services.get_latest_products()
    agents = services.get_agent()
    news = services.get_news()
    testimonials = services.get_testimonials()
    ctx = {
        "index": 'active',
        "products": products,
        "agents": agents,
        "latest_products": latest_products,
        "service": service,
        "news": news,
        "testimonials": testimonials,
    }
    return render(request, 'frontend/index.html', ctx)


def about(request):
    ctx = {
        "about": 'active',

    }
    return render(request, 'frontend/about.html', ctx)


def agents(request):
    ctx = {
        "agents": 'active',

    }
    return render(request, 'frontend/agents.html', ctx)


def blog(request):
    ctx = {
        "blog": 'active',

    }
    return render(request, 'frontend/blog.html', ctx)


def blog_single(request):
    ctx = {
        "blog-single": 'active',

    }
    return render(request, 'frontend/blog-single.html', ctx)


def property(request):
    ctx = {
        "property": 'active',

    }
    return render(request, 'frontend/property.html', ctx)


def property_single(request):
    ctx = {
        "property-single": 'active',

    }
    return render(request, 'frontend/property-single.html', ctx)


def contact(request):
    ctx = {
        "contact": 'active',

    }
    return render(request, 'frontend/contact.html', ctx)


def agent_single(request):
    ctx = {
        "agent-single": 'active',
    }
    return render(request, 'frontend/agent-single.html', ctx)
