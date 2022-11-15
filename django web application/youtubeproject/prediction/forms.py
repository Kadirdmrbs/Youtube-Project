from django import forms
from . models import MlModel
from django.forms import ModelForm



'''
class MlForm(forms.Form):
    likes = forms.IntegerField(label='like amount')
    comments = forms.IntegerField(label='comment amount')
    category = forms.ChoiceField(label='please select a category',
                                widget=forms.RadioSelect, 
                                choices=CATEGORIES)
'''

class MlForm(ModelForm):
    class Meta:
        model = MlModel
        fields = '__all__'

        widgets = {

            'likes': forms.NumberInput(attrs={'class':'form-control',
                                            'placeholder':'Enter like amount'}),
            'comments': forms.NumberInput(attrs={'class':'form-control',
                                            'placeholder':'Enter comment amount'}),
            'duration': forms.NumberInput(attrs={'class':'form-control',
                                            'placeholder':'Enter duration in seconds'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'year': forms.Select(attrs={'class':'form-control'}),


        }