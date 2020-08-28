from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django_tables2 import SingleTableView
from .models import Inquiry, Procedure
from .forms import InquiryForm
from .tables import ProcedureTable
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


def index(request):
    return render(request, 'website/index.html')


class InquiryFormView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'website/inquiry.html'
    success_url = '/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        from_email = settings.DEFAULT_FROM_EMAIL
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        inquiry_email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        email_content = f'Name: {name}\nPhone: {phone}\nEmail: {inquiry_email}\nSubject: {subject}\nMessage: {message}'

        form.save()

        try:
            send_mail(subject, email_content, from_email, [
                      'ptcebula@gmail.com'], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found')
        return redirect('website:index')


class ProcedureList(SingleTableView):
    table_class = ProcedureTable
    template_name = "website/procedure_list.html"
    queryset = Procedure.objects.order_by('category', 'id')
