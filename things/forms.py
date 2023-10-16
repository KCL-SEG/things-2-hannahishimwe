"""Forms of the project."""
from django import forms
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator

class ThingForm(forms.ModelForm):
    
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(), 'quantity': forms.NumberInput()}

        quantity = forms.IntegerField(
         validators=[MinValueValidator(0),MaxValueValidator(50)]
         
     )
    
    def clean(self):
        super().clean()
        quantity = self.changed_data.get('quantity')
        if quantity > 100 | quantity < 0 :
            self.add_error('quanitity', 'Add valid input for quanitity')



   




