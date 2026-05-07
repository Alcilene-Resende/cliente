from .models import Cliente
from django import forms 

class ClienteForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "forms-control"}))
    cpf = forms.CharField(widget =forms.TextInput(attrs={"class": "forms-control"}))
    telefone = forms.CharField(widget =forms.TextInput(attrs={"class": "forms-control"}))
    nascimento = forms.CharField(widget=forms.DateInput(attrs={"class": "forms-control", "type": "date"}))

    class Meta:
        model = Cliente
        fields = '__all__'