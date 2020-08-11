from django import forms
from .models import Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'email',
            'subject',
            'message',
        ]
