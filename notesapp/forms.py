from django import forms
from .models import NoteModel

class NoteForm(forms.ModelForm):
    TAG_CHOICES = [
        ('work', '💼 Work'),
        ('personal', '👤 Personal'),
        ('home', '🏠 Home'),
    ]
    
    tags = forms.ChoiceField(choices=TAG_CHOICES, widget=forms.Select(attrs={'style': 'font-size: 16px;'}))
    
    class Meta:
        model = NoteModel
        fields = ['title', 'content', 'tags']
