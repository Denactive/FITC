from django.shortcuts import render
from app.models import Library
from app.models import Disk
# V  DRF  V
from rest_framework import viewsets
from app.serializers import DiskSerializer

def index_page_router(request):
  return render(request, 'index.html', {"items": Disk.objects.all()})
  
def libs_page_router(request):
  return render(request, 'libraries.html', {"items": Library.objects.all()})

def lib_page_router(request, pk):
  lib = Library.objects.get(pk=pk)
  disks = lib.fk_storedDisks.all()
  return render(request, 'lib_details.html', {'item': lib, 'items': disks})

# V  DRF  V
class DiskViewSet(viewsets.ModelViewSet):
  """
  API endpoint, который позволяет просматривать и редактировать
  """
  # queryset всех пользователей для фильтрации по дате последнего изменения
  queryset = Disk.objects.all()
  serializer_class = DiskSerializer  # Сериализатор для модели