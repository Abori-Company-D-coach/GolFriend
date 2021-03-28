from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from board.models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '' , password)
            return render(request, 'board/signup.html', {'some': 100})            
        except IntegrityError:
            return render(request, 'board/signup.html', {'error': 'このユーザは既に登録されています。'})

        user = User.objects.create_user(username, '' , password)
    return render(request, 'board/signup.html')


def loginfunc(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')            
        else:
            return render(request, 'board/login.html', {})    
    return render(request, 'board/login.html', {})


@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'board/list.html', {'object_list':object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'board/detail.html', {'object':object})


def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')


def readfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    username = request.user.get_username()
    if username in object.readtext:
        return redirect('list')
    else:
        object.read = object.read + 1
        object.readtext = object.readtext + ' ' + username
        object.save()
        return redirect('list')



class BoardCreate(CreateView):
    template_name='board/create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('list')
