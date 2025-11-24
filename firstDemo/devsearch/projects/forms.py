from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'feature_image','description','demo_link', 'source_link','source_link','tags']

        widgets = {'tags': forms.CheckboxSelectMultiple(),}
    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__()
        for k,v in self.fields.items():
            v.widget.attrs.update({'class': 'input'})
       