from django import forms
from django.forms import ModelForm, Textarea


from .models import Note

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('note_type', 'note', 'message')
        widgets = {
            'message': Textarea(attrs={'cols': 80, 'rows': 8}),
        }
