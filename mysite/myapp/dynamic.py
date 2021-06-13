from .services import get_countries


def country(request):
    countries = get_countries()

    ctx = {
        "countries": countries
    }
    return ctx
