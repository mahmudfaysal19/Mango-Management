from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from models import MangoExport
from forms import MangoExportForm

def mango_list(request):
    search_query = request.GET.get('search')
    if search_query:
        mangoes = MangoExport.objects.filter(order_id__icontains=search_query)
    else:
        mangoes = MangoExport.objects.all()
    return render(request, 'mango/mango_list.html', {'mangoes': mangoes})

def mango_create(request):
    if request.method == 'POST':
        form = MangoExportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mango export created successfully!')
            return redirect('mango_list')
    else:
        form = MangoExportForm()
    return render(request, 'mango/mango_form.html', {'form': form, 'action': 'Create'})

def mango_update(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == 'POST':
        form = MangoExportForm(request.POST, instance=mango)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mango export updated successfully!')
            return redirect('mango_list')
    else:
        form = MangoExportForm(instance=mango)
    return render(request, 'mango/mango_form.html', {'form': form, 'action': 'Update'})

def mango_delete(request, pk):
    mango = get_object_or_404(MangoExport, pk=pk)
    if request.method == 'POST':
        mango.delete()
        messages.success(request, 'Mango export deleted successfully!')
        return redirect('mango_list')
    return render(request, 'mango/mango_confirm_delete.html', {'mango': mango})