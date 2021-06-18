from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from myapp.models import *
from myapp.forms import *
from . import services


def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    products=services.get_products()
    category = services.get_categories_count()
    products_count = services.get_products_count()
    countries_count = services.get_countries_count()
    agents_count = services.get_agents_count()
    category_product = services.get_categories_products_count()

    ctx = {
        "category": category,
        "products_count": products_count,
        "countries_count": countries_count,
        "agents_count": agents_count,
        "category_product": category_product,
        "products":products

    }
    return render(request, 'dashboard/index.html', ctx)


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


@login_required_decorator
def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def categories_list(request):
    categories = services.get_categories()
    ctx = {
        "categories": categories
    }
    return render(request, 'dashboard/category/list.html', ctx)


@login_required_decorator
def categories_create(request):
    model = Category()
    form = CategoryForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def categories_edit(request, category_id):
    model = Category.objects.get(id=category_id)
    form = CategoryForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('categories_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/category/form.html', ctx)


@login_required_decorator
def categories_delete(request, category_id):
    model = Category.objects.get(id=category_id)
    model.delete()
    return redirect("categories_list")


@login_required_decorator
def countries_list(request):
    countries = services.get_countries()
    ctx = {
        "countries": countries
    }
    return render(request, 'dashboard/country/list.html', ctx)


@login_required_decorator
def countries_create(request):
    model = Country()
    form = CountryForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('countries_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/country/form.html', ctx)


@login_required_decorator
def countries_edit(request, country_id):
    model = Country.objects.get(id=country_id)
    form = CountryForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('countries_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/country/form.html', ctx)


@login_required_decorator
def countries_delete(request, country_id):
    model = Country.objects.get(id=country_id)
    model.delete()
    return redirect("countries_list")


@login_required_decorator
def agents_list(request):
    agents = services.get_agents()
    ctx = {
        "agents": agents
    }
    return render(request, 'dashboard/agent/list.html', ctx)


@login_required_decorator
def agents_create(request):
    model = Agent()
    form = AgentForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('agents_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/agent/form.html', ctx)


@login_required_decorator
def agents_edit(request, agent_id):
    model = Agent.objects.get(id=agent_id)
    form = AgentForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('agents_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/agent/form.html', ctx)


@login_required_decorator
def agents_delete(request, agent_id):
    model = Agent.objects.get(id=agent_id)
    model.delete()
    return redirect("agents_list")


@login_required_decorator
def products_list(request):
    products = services.get_products()
    ctx = {
        "products": products
    }
    return render(request, 'dashboard/product/list.html', ctx)


@login_required_decorator
def products_create(request):
    model = Product()
    form = ProductForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def products_edit(request, product_id):
    model = Product.objects.get(id=product_id)
    form = ProductForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/product/form.html', ctx)


@login_required_decorator
def products_delete(request, product_id):
    model = Product.objects.get(id=product_id)
    model.delete()
    return redirect("products_list")


@login_required_decorator
def news_list(request):
    news = services.get_news()
    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news/list.html', ctx)


@login_required_decorator
def news_create(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)


@login_required_decorator
def news_edit(request, news_id):
    model = News.objects.get(id=news_id)
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/news/form.html', ctx)


@login_required_decorator
def news_delete(request, news_id):
    model = News.objects.get(id=news_id)
    model.delete()
    return redirect("news_list")


@login_required_decorator
def testimonials_list(request):
    testimonials = services.get_testimonials()
    ctx = {
        "testimonials": testimonials
    }
    return render(request, 'dashboard/testimonial/list.html', ctx)


@login_required_decorator
def testimonials_create(request):
    model = Testimonial()
    form = TestimonialForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('testimonials_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/testimonial/form.html', ctx)


@login_required_decorator
def testimonials_edit(request, testimonial_id):
    model = Testimonial.objects.get(id=testimonial_id)
    form = TestimonialForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('testimonials_list')
        else:
            print(form.errors)
    ctx = {
        "form": form
    }
    return render(request, 'dashboard/testimonial/form.html', ctx)


@login_required_decorator
def testimonials_delete(request, testimonial_id):
    model = Testimonial.objects.get(id=testimonial_id)
    model.delete()
    return redirect("testimonials_list")
