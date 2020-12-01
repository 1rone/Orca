from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import Context, loader


# def list(request, sid):
#     try:
#         sid = int(sid)
#     except ValueError:
#         raise Http404
#     else:
#         template = loader.get_template('demo.html')
#         context = Context()
#         return HttpResponse(template.render(context))

def _list(request):
    return render(request, 'form_test/demo.html', {})