from django import forms

from django.core.exceptions import ValidationError

from .models import curso, disciplina

LISTA_DISCIPLINAS = (('Elec','Electronica'),
                    ('Rep','Reposteria'),
                    ('Lit','Literatura'),
                    )

class CursoForm(forms.ModelForm):

    # titulo = forms.CharField(widget=forms.TextInput
    # descripcion = forms.CharField(widget=forms.Textarea)
    # disciplina = forms.CharField(widget=forms.TextInput)
    # avatar = forms.ImageField(widget=forms.ClearableFileInput)
    # precio = forms.DecimalField(widget=forms.NumberInput(attrs={'step': 0.01}))
    # # calificacion = forms.DecimalField(widget=forms.NumberInput(attrs={'step': 0.5}))
    # # alumnos = forms.DecimalField(widget=forms.NumberInput())
    # profesor = forms.CharField(help_text="Ingrese un nombre de profesor")

    class Meta:
        model = curso
        # fields = "__all__"
        fields = ['titulo','descripcion','disciplina','avatar','precio']

        widgets = {'titulo': forms.TextInput(attrs={'class':'form-control'}),
                   'descripcion': forms.Textarea(attrs={'class':'form-control'}),
                   'disciplina': forms.Select(choices=disciplina.objects.all(),attrs={'class':'form-control'}),
                   'avatar': forms.ClearableFileInput(attrs={'class':'form-control'}),
                   'precio':forms.NumberInput(attrs={'step':0.01,'class':'form-control'})}
        labels = {'titulo':'Titulo del Curso:',
                  'descripcion': 'Descripcion del Curso',
                  'disciplina': 'Disciplina',
                  'avatar': 'Logo del Curso',
                  'precio': 'Precio de venta'}

    def clean_calificacion(self):
        calificacion = self.cleaned_data['calificacion']
        if calificacion < 0 or calificacion > 5:
            raise ValidationError('La calificacion debe estar entre 0 y 5')
        return calificacion

class DisciplinaForm(forms.ModelForm):

    class Meta:
        model = disciplina

        fields = ['nombre']

        widgets = {'nombre': forms.TextInput(attrs={'class':'form-control'})}
        labels = {'nombre':'Nombre de la disciplina:'}
