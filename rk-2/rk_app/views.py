from django.shortcuts import render
from rk_app.models import Library
from rk_app.models import Disk

def index_page_router(request):
  return render(request, 'index.html', {"items": Disk.objects.all()})
  
def libs_page_router(request):
  return render(request, 'libraries.html', {"items": Library.objects.all()})

def lib_page_router(request, pk):
  lib = Library.objects.get(pk=pk)
  disks = lib.fk_storedDisks.all()
  print(lib)
  print(disks)
  return render(request, 'lib_details.html', {'item': lib, 'items': disks})