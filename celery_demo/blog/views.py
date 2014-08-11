from django.shortcuts import render

# Create your views here.


def blocking_view(request, object_pk=None):
    object = get_object_or_404(SomeObject, pk=object_pk)
    object.do_method()

    # Non-blocking.  Celery takes over this code and lets us move right along
    ObjectTransaction.delay(object)

    return render(request, 'template.html')
