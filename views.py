from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import WorkOrder
from .serializers import WorkOrderSerializer
from django.shortcuts import render
from .forms import WorkOrderForm

def create_work_order(request):
    if request.method == 'POST':
        form = WorkOrderForm(request.POST)
        if form.is_valid():
            work_order = form.save(commit=True)
            work_order.save()
            return render(request, 'work_order/work_order_created.html', {'work_order': work_order})
    else:
        form = WorkOrderForm()
    return render(request, 'work_order/create_work_order.html', {'form': form})


class WorkOrderCreateView(generics.CreateAPIView):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
