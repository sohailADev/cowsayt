from django import forms
from cowsay_app.models import Cow

class AddCowForm(forms.Form):    
      
    cowsay = forms.CharField(max_length=50,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'say something...'
        }
    ))
