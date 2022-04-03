"""djangostudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'djangofirst'

urlpatterns = [
    path('', views.index, name='index'),
    path('pref_quiz', views.pref_quiz, name='pref_quiz'),
    path('pref_result', views.pref_result, name='pref_result'),
    path('random_quiz', views.random_quiz, name='random_quiz'),
    path('quiz_result', views.quiz_result, name='quiz_result'),
    path('wiki', views.wiki, name='wiki'),
    path('wiki_result', views.wiki_result, name='wiki_result'),
    
]
