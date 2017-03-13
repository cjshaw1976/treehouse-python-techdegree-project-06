from django.shortcuts import get_object_or_404, render

from . models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_random(request):
    mineral = Mineral.objects.order_by('?').first()
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})
