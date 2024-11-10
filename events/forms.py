from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Event, Inscricao


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_date', 'start_time', 'end_date', 'end_time', 'description', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do evento'}),
            'start_date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(format='%H:%M', attrs={'class': 'form-control', 'type': 'time'}),
            'end_date': forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control', 'type': 'date'}),
            'end_time': forms.TimeInput(format='%H:%M', attrs={'class': 'form-control', 'type': 'time'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o local do evento'}),
        }


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['participant_name', 'participant_email']
        widgets = {
            'participant_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu nome'}),
            'participant_email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Digite o seu e-mail'}),
        }

    def clean_participant_email(self):
        participant_email = self.cleaned_data.get('participant_email')
        event = self.instance.event
        if Inscricao.objects.filter(event=event, participant_email=participant_email).exists():
            raise forms.ValidationError("Você já está inscrito neste evento com este e-mail.")
        return participant_email


class RegistroUsuario(UserCreationForm):
    nome_completo = forms.CharField(max_length=160)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nome_completo', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email


class EdicaoUsuario(forms.ModelForm):
    nome_completo = forms.CharField(max_length=160)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['nome_completo', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email
