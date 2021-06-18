from django import forms
from .models import Category, Product, Country, Commenter, Services, User_Commenter, \
    Agent, Testimonial, Amenities,Contact,News


class User_CommenterForm(forms.ModelForm):
    class Meta:
        model = User_Commenter()
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact()
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category()
        fields = '__all__'


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country()
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product()
        fields = '__all__'


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent()
        fields = '__all__'

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial()
        fields = '__all__'


class CommenterForm(forms.ModelForm):
    class Meta:
        model = Commenter()
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = '__all__'