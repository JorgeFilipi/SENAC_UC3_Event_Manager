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


# class InscricaoForm(forms.ModelForm):
#     class Meta:
#         model = Inscricao
#         fields = ['participant_name', 'participant_email']
#         widgets = {
#             'participant_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu nome'}),
#             'participant_email': forms.EmailInput(
#                 attrs={'class': 'form-control', 'placeholder': 'Digite o seu e-mail'}),
#         }
#
#     def __init__(self, *args, event=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.event = event
#
#     def clean_participant_email(self):
#         participant_email = self.cleaned_data.get('participant_email')
#         if Inscricao.objects.filter(event=self.event, participant_email=participant_email).exists():
#             raise forms.ValidationError("Você já está inscrito neste evento com este e-mail.")
#         return self.cleaned_data.get('participant_email')


class RegistroUsuario(UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=30)
    last_name = forms.CharField(label='Sobrenome', max_length=30)
    username = forms.CharField(label='Usuário', max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email


class EdicaoUsuario(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O campo email é obrigatório.")
        return email
