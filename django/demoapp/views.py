from django.shortcuts import render
from django.views.decorators.vary import vary_on_headers
from django.utils.cache import patch_vary_headers

@vary_on_headers('Accept-Language')
def homepage(request):
    context = {}
    response = render(request, 'p1.html', context)
    patch_vary_headers(response, ['User-Agent'])
    return response