from django.shortcuts import render, redirect
from . import services
from myapp.models import Product, Agent, User_Commenter, Contact
from .forms import User_CommenterForm, ContactForm
from django.core.paginator import Paginator, EmptyPage

var = [{
    "title": "About Us",
    "image1": "../static/frontend/img/slide-about-1.jpg",
    "image2": "../static/frontend/img/about-2.jpg",
    "desc": "Far far away, behind the word mountains, ' \
        'far from the countries Vokalia and Consonantia,' \
        ' there live the blind texts. Separated they live ' \
        'in Bookmarksgrove right at the coast of the ' \
        'Semantics, a large language ocean. Sed porttitor lectus nibh.' \
        ' Vivamus magna justo, lacinia eget consectetur sed, convallis at ' \
        'tellus. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. ' \
        'Vivamus magna justo, lacinia eget consectetur sed, convallis at tellus."
}]


def home(request):
    products = services.get_products()
    service = services.get_services()
    latest_products = services.get_latest_products()
    agents = services.get_agents()
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
    agents = Agent.objects.all().order_by("-created_at")[4:]
    ctx = {
        "about": 'active',
        "var": var,
        "agents": agents,
    }
    return render(request, 'frontend/about.html', ctx)


def blog(request):
    posts = services.get_posts()
    p = Paginator(posts, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(posts)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    ctx = {
        "blog": 'active',
        "posts": posts,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages

    }
    return render(request, 'frontend/blog.html', ctx)


def blog_single(request, news_id):
    model = User_Commenter()
    form = User_CommenterForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    new = services.get_news_by_id(news_id=news_id)
    commenter = services.get_commenter()
    ctx = {
        "blog-single": 'active',
        "commenter": commenter,
        "new": new

    }
    return render(request, 'frontend/blog-single.html', ctx)


def property(request):
    product = services.get_products()
    status = services.get_products()
    filter = "all"
    if request.POST:
        filter = request.POST.get("order_filter")

        if filter == "new":
            status = services.get_product_by_created_at()

        if filter == "rent":
            status = services.get_product_by_rent()

        if filter == "sale":
            status = services.get_product_by_sale()
    p = Paginator(product, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(product)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    ctx = {
        "property": 'active',
        "product": product,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages,
        "filter": filter,
        "status": status

    }
    return render(request, 'frontend/property.html', ctx)


# def order_list(request):
#     status = get_status_info([1, 2, 3])
#     filter = "all"
#     if request.POST:
#         filter = request.POST.get("order_filter")
#
#         if filter == "done":
#             status = get_status_info([2])
#
#         if filter == "failed":
#             status = get_status_info([3])
#
#     ctx = {
#         "status": status,
#         "filter": filter,
#     }
#     return render(request, 'dashboard/order/list.html', ctx)


def property_single(request, product_id):
    model = User_Commenter()
    form = User_CommenterForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('blog-single')
        else:
            print(form.errors)
    product = services.get_products_by_id(product_id=product_id)
    amenities = services.get_amenities()
    agents = Agent.objects.all().order_by("-created_at")[6:]
    ctx = {
        "property-single": 'active',
        "product": product,
        "amenities": amenities,
        "agents": agents,

    }
    return render(request, 'frontend/property-single.html', ctx)


def agents(request):
    agent = services.get_agents()
    p = Paginator(agent, 3)
    page_num = request.GET.get('page', 1)
    total_pages = len(agent)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    ctx = {
        "agents": 'active',
        "agent": agent,
        "page": page,
        "page_num": page_num,
        "total_pages": total_pages

    }
    return render(request, 'frontend/agents.html', ctx)


def agent_single(request, agent_id):
    ag = services.get_agent(agent_id=agent_id)
    product = services.get_products()

    ctx = {
        "agent-single": 'active',
        "ag": ag,
        "product": product,
    }
    return render(request, 'frontend/agent-single.html', ctx)


def contact(request):
    model = Contact()
    form = ContactForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)
    ctx = {
        "contact": 'active',

    }
    return render(request, 'frontend/contact.html', ctx)
