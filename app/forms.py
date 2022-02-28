from django import forms

from app.models import Student

class StudentForm(forms.Form):
    first_name = forms.CharField(
        label="Prenom ",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Foulen'})
    )
    last_name = forms.CharField(
        label="Nom ",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'BEN FOULEN'})

    ) 
    email = forms.CharField(
        label="Email ",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'foulen.benfoulen@mail.end'})
    )
    
class StudentModelForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = '__all__'
        

