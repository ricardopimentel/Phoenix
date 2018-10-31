from django.shortcuts import render, resolve_url as r

# Create your views here.
def home(request):
    request.session['menu'] = ['logo', 'HOME', 'sair']
    request.session['url'] = [r('Home'), r('Home'), '']
    request.session['img'] = ['if.png', 'home24.png', '']
    return render(request, 'index.html', {'err': '', 'itemselec': 'HOME'})