from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Inquiry
from .forms import InquiryForm


def index(request):
    return render(request, 'website/index.html')


class InquiryFormView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'website/inquiry.html'
    success_url = '/'
