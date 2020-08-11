from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Submit
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Imię i nazwisko'})
        self.fields['phone'].widget.attrs.update(
            {'placeholder': 'Numer telefonu'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Adres email'})
        self.fields['subject'].widget.attrs.update(
            {'placeholder': 'Temat zapytania'})
        self.fields['message'].widget.attrs.update(
            {'placeholder': 'Wiadomość'})
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.input_class = 'bg-gray-600 w-full my-2 px-4 py-2 border border-gray-200'
        self.helper.layout = Layout(
            Div(
                Field('name', css_class=self.input_class),
                Field('phone', css_class=self.input_class),
                Field('email', css_class=self.input_class),
                Field('subject', css_class=self.input_class),
                Field('message', css_class=self.input_class),
                Submit('submit', 'Wyślij zapytanie',
                       css_class='bg-green-400 self-center px-4 py-2 text-xl text-white font-bold'),
                css_class='flex flex-col',
            ),
        )
