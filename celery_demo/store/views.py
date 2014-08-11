import time


from django.shortcuts import render, redirect
from django.views.generic import TemplateView


from store.forms import ImageStoreForm
from store.tasks import make_thumbnails, process_payment, add

"""
This is just some example views and methods
for demonstrating Celery.  These are intentionally trivial
"""



class HomePage(TemplateView):
    template_name = 'home.html'

def sync_upload(request):
    if request.method == 'POST':
        form = ImageStoreForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            # BLOCKING!
            img.make_thumbnails()
            return redirect('/')
    form = ImageStoreForm()
    return render(request, 'store/upload.html', {'form': form})

def async_upload(request):
    if request.method == 'POST':
        form = ImageStoreForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            # NON Blocking!
            make_thumbnails.delay(img)
            return redirect('/')
    form = ImageStoreForm()
    return render(request, 'store/upload.html', {'form': form})


def process_transaction():
    time.sleep(10)
    print("Transaction Processed")
