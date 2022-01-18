from django import forms
from .models import Mark, Category

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('__all__')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')