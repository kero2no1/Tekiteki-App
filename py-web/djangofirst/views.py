from django.shortcuts import render

def index(request):
    
    context = {
        'title' : 'はじめての Django Web アプリケーション',
    }
    
    
    return render(request, 'djangofirst/index.html', context)