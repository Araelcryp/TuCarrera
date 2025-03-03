from django import forms
from django.core.exceptions import ValidationError
import re

class SignupForm(forms.Form):
    apellidoPaterno = forms.CharField(max_length=100, required=True)
    apellidoMaterno = forms.CharField(max_length=100, required=True)
    nombres = forms.CharField(max_length=100, required=True)
    fechaNacimiento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    curp = forms.CharField(max_length=18, required=True)
    telefono = forms.CharField(max_length=30    , required=True)
    email = forms.EmailField(required=True)
    email_tutor = forms.EmailField(required=True, label="Correo del padre/tutor")
    password1 = forms.CharField(
        widget=forms.PasswordInput, required=True
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput, required=True
    )
    procedencia = forms.ChoiceField(
        choices=(("si", "Sí"), ("no", "No")), required=True
    )
    #Campos opcionales según procedencia
    estado = forms.CharField(max_length=100, required=False)
    institucion = forms.CharField(max_length=100, required=False)
    municipio = forms.CharField(max_length=100, required=False)
    bachillerato = forms.CharField(max_length=100, required=False)
    otro_bachillerato = forms.CharField(max_length=100, required=False)
    matricula = forms.CharField(max_length=50, required=False)

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        if not re.search(r'[A-Z]', password):
            raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')
        if not re.search(r'[a-z]', password):
            raise ValidationError('La contraseña debe contener al menos una letra minúscula.')
        if not re.search(r'[0-9]', password):
            raise ValidationError('La contraseña debe contener al menos un número.')
        if not re.search(r'[@$!%*?#]', password):
            raise ValidationError('La contraseña debe contener al menos un signo especial.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Las contraseñas no coinciden.')
        return cleaned_data

    def clean_curp(self):
        curp = self.cleaned_data.get("curp", "").upper()
        REGEX_CURP = r'^[A-ZÑ]{4}\d{6}[HM][A-ZÑ]{5}[A-Z0-9]{2}$'
        if len(curp) != 18:
            raise ValidationError('CURP inválida. Debe tener 18 caracteres!')
        if not re.match(REGEX_CURP, curp):
            raise ValidationError('CURP inválida. Verifica nuevamente!')
        return curp
    

    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono", "")
        REGEX_TELEFONO = r'^\d{10}$'
        if not re.match(REGEX_TELEFONO, telefono):
            raise ValidationError('Teléfono inválido. Debe tener 10 dígitos!')
        return telefono