import time


from django.shortcuts import render
from django.views.generic import TemplateView

"""
This is just some example views and methods
for demonstrating Celery.  These are intentionally trivial
"""



class HomePage(TemplateView):
    template_name = 'home.html'

def sync_transaction(request):
    pass

def async_transaction(request):
    pass


def sync_upload(request):
    pass

def async_upload(request):
    pass


def process_transaction():
    time.sleep(10)
    print("Transaction Processed")
