from django import forms
from .models import WorkOrder

class WorkOrderForm(forms.Form):
    class Meta:
        model = WorkOrder
        fields = '__all__'

