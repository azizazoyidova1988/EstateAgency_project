from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.CharField(max_length=450, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "services"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "country"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=1)
    description = models.CharField(max_length=450, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    services = models.ForeignKey(Services, blank=False, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, blank=False, null=True, on_delete=models.SET_NULL)
    aria = models.CharField(max_length=50, blank=False, null=False)
    beds = models.IntegerField(blank=False, null=False, default=1)
    baths = models.IntegerField(blank=False, null=False, default=1)
    garages = models.IntegerField(blank=False, null=False, default=1)
    status = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class Amenities(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "amenities"

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    mobil_phone = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    telegram = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "agent"

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    author = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=650, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    big_image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "testimonial"

    def __str__(self):
        return self.name


class User_Commenter(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    comment = models.CharField(max_length=450, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name

class Commenter(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    message = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "commenter"

    def __str__(self):
        return self.name
