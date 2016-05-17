from django import forms
from .models import Arquivo



class PostForm(forms.ModelForm):

    class Meta:
        model = Arquivo
        fields = ('arq')
