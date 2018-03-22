from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

#from ChaRate.models import Character, Movie, TV
#from ChaRate.forms import UserForm, UserProfileForm

# from django.db.utils import OperationalError
# format_list = [('', '(all)')]
# geom_type_list = [('', '(all)')]
# try:
#     format_list.extend([(i[0],i[0]) 
#         for i in Format.objects.values_list('name')])
#     geom_type_list.extend([(i[0],i[0]) 
#         for i in Geom_type.objects.values_list('name')])
# except OperationalError:
#     pass  # happens when db doesn't exist yet, views.py should be
#           # importable without this side effect


def index(request):
    context_dict = {}
    return render(request, 'ChaRate/index.html', context=context_dict)

def about(request):
    return render(request, 'ChaRate/about.html', {})
    

def link_movie(request):
    return render(request, 'ChaRate/link_mov.html', {})

def linkTv(request):
    return render(request, 'ChaRate/link_tv.html', {})

def Account(request,):
    return render(request, 'ChaRate/account.html', {})

def filter_tv(request):
    return render(request, 'ChaRate/character.html', {})


def filter_mov(request):
    return render(request, 'ChaRate/character.html', {})

def search(request):
    return render(request, 'ChaRate/character.html', {})

def show_character(request):
    return render(request, 'ChaRate/character.html', {})

def show_movie(request):
    return render(request, 'ChaRate/movpage.html', {})

def show_tvShow(request):
    return render(request, 'ChaRate/tvpage.html', {})

def add_tv(request):
    return render(request, 'ChaRate/add_tv.html', {})

def add_mov(request):
    return render(request, 'ChaRate/add_mov.html', {})

def add_comment(request):
    return render(request, 'ChaRate/add_comment.html', {})

def add_character(request):
    return render(request, 'ChaRate/create_character.html', {})

def mov_filter(request):
    return render(request, 'ChaRate/movfilter.html', {})

def tv_filter(request):
    return render(request, 'ChaRate/tvfilter.html', {})

def search(request):
    return render(request, 'ChaRate/search.html', {})

# User Authentication: ------------------------------------

def register(request):
    return render(request, 'ChaRate/register.html', {})
#
def user_login(request):
        return render(request, 'ChaRate/login.html', {})
#
#@login_required
#def user_logout(request):
#    logout(request)
#    return HttpResponseRedirect(reverse('index'))


# ------------------------------------
