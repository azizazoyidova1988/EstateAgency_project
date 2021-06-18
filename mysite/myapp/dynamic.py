from .services import get_countries
from .models import Product


def country(request):
    countries = get_countries()

    ctx = {
        "countries": countries
    }
    return ctx


def search(request):
    if request.GET:
        a = request.GET.get("search")
        print(a, 'A')
        # product = Product.objects.filter(price__icontains=request.GET.get("search"))
        # ctx = {
        #     "product": product
        # }
        # return ctx
