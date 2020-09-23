from django import forms
from .models import Member, Message

class MemberForm(forms.Form):
    name = forms.CharField(label='name')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'member']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 120})
        }