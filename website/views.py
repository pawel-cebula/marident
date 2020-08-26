from django.shortcuts import render
from django.views.generic.edit import CreateView
from django_tables2 import SingleTableView
from .models import Inquiry, Procedure
from .forms import InquiryForm
from .tables import ProcedureTable


def index(request):
    return render(request, 'website/index.html')


class InquiryFormView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'website/inquiry.html'
    success_url = '/'


class ProcedureList(SingleTableView):
    table_class = ProcedureTable
    template_name = "website/procedure_list.html"
    queryset = Procedure.objects.order_by('category', 'id')
