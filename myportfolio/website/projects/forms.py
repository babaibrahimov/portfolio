# from dataclasses import fields
# from pyexpat import model
from django import forms
from . import models

class AddProjectForm(forms.ModelForm):
    class Meta:
        model = models.Projects
        fields = '__all__'
