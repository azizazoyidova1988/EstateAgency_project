from django.contrib import admin

from . import models

admin.site.register(models.News)
admin.site.register(models.Country)
admin.site.register(models.Category)
admin.site.register(models.Services)
admin.site.register(models.Product)
admin.site.register(models.Agent)
admin.site.register(models.Amenities)
admin.site.register(models.Testimonial)
admin.site.register(models.User_Commenter)
admin.site.register(models.Commenter)
