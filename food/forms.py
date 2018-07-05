from django import forms
from .models import Food

class FoodForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()

    def save(self, commit=True):
        food = Food(**self.cleaned_data)
        if commit:
            food.save()
        return food
