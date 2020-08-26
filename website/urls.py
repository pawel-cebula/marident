from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Inquiry page
    path('inquiry', views.InquiryFormView.as_view(), name='inquiry'),
    # Procedure page
    path('procedures', views.ProcedureList.as_view(), name='procedures'),
]
