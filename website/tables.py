import django_tables2 as tables
from .models import Procedure


class ProcedureTable(tables.Table):
    class Meta:
        model = Procedure
        sequence = ("name", "price", )
        exclude = ("id", )
