from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    return None
