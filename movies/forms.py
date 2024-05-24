from django import forms
from .models import MovieReview


class NameForm(forms.Form):
    your_name = forms.CharField(label="Nombre", max_length=100, help_text="100 car. máximo", 
                                    error_messages={"required": "El nombre es obligatorio"},
                                    widget=forms.Textarea(attrs={"class":"text-gray-400", "rows": 3, "cols": 60}))
                                    
class MovieReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(0.5, '0.5'), (1, '1'), (1.5, '1.5'), (2, '2'), (2.5, '2.5'),
                                         (3, '3'), (3.5, '3.5'), (4, '4'), (4.5, '4.5'), (5, '5')],
                                label='Rating')

    class Meta:
        model = MovieReview
        fields = ['rating', 'review']
