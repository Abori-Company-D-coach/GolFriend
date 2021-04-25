from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from board.models import Board, Profile
from .forms import PostForm, ProfileForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponse
from django.views import generic
from django.conf import settings


class IndexView(TemplateView):
    "トップページを表示"
    "Written by Tett"
    template_name = "board/index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "Guest User"
        return ctxt



class AboutView(TemplateView):
    "アバウトページを表示"
    "Written by Tett"
    template_name = "board/about.html"



"------------Tett作成マイページ---------------"
class MypageView(generic.TemplateView):
    "マイページのPosts表示"
    "Written by Taishin & Tett"
    # model = BoardModel
    template_name = "board/mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # contextに追加(htmlで使える)
        # context[''] = 
        return context

    "4/17 usersに置き換えることで消去可？"
    # def get(self, request, *args, **kwargs):
    #     """get関数

    #     プロフィールデータを取得
    #     """
    #     profile_data = Profile.objects.all()
    #     if profile_data.exists():
    #         profile_data = profile_data.order_by('-id')[0]
        
    #     my_posts = Board.objects.order_by('-id')
    #     return render(request, 'board/mypage.html', {
    #         'profile_data': profile_data,
    #         'my_posts': my_posts
    #     })


def users(request, pk):
    "マイページにログインユーザを紐づける"
    profile_data = get_object_or_404(Profile, pk=pk)
    my_posts = Board.objects.filter(user_num = '8')
    # my_posts = Board.objects.filter(user_num = Profile.pk)
    # my_posts = get_object_or_404(Board, user_num = 1)
    context = {
        'profile_data': profile_data,
        'my_posts': my_posts
    }
    return render(request, 'board/mypage.html', context)



class CreateProfileView(CreateView):
    "Written by Tett"
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('mypage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'プロフィールの作成'
        context['form_name'] = 'プロフィールの作成'
        context['button_label'] = 'プロフィールを作成する'
        return context
    
    def form_valid(self, form):
        self.object = profile = form.save()
        messages.success(self.request, 'プロフィールの作成が完了しました')
        return redirect(self.get_success_url())

"------------------------------------------"


def signupfunc(request):
    "Written by Koo"
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
    "Written by Koo"
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
    "Written by Koo"
    object_list = BoardModel.objects.all()
    return render(request, 'board/list.html', {'object_list':object_list})


def logoutfunc(request):
    "Written by Koo"
    logout(request)
    return redirect('login')


"--------------Tett作成掲示板---------------------------------"
class BoardList(ListView):
    "Written by Tett"
    model = Board
    queryset = Board.objects.order_by('-updated_at')
    paginate_by = 10



class ShowPostView(DetailView):
    "Written by Tett"
    model = Board



class CreatePostView(CreateView):
    "Written by Tett"
    model = Board
    form_class = PostForm
    success_url = reverse_lazy('board_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'コメントの投稿'
        context['form_name'] = 'コメントの投稿'
        context['button_label'] = 'コメントを投稿する'
        return context
    
    def form_valid(self, form):
        self.object = board = form.save()
        messages.success(self.request, '投稿が完了しました')
        return redirect(self.get_success_url())



class UpdatePostView(UpdateView):
    "Written by Tett"
    model = Board
    form_class = PostForm
    success_url = reverse_lazy('board_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'コメントの更新'
        context['form_name'] = 'コメントの更新'
        context['button_label'] = 'コメントを更新する'
        return context

    def form_valid(self, form):
        self.object = board = form.save()
        messages.success(self.request, '投稿を更新しました')
        return redirect(self.get_success_url())



class DeletePostView(DeleteView):
    "Written by Tett"
    model = Board
    success_url = reverse_lazy('board_list')

    def delete(self, request, *args, **kwargs):
        self.object = board = self.get_object()
        board.delete()
        messages.success(self.request, '投稿を削除しました')
        return redirect(self.get_success_url())
"---------------------------------------------------------------"

"Koo作成掲示板"
# def detailfunc(request, pk):
#     "Written by Koo"
#     object = get_object_or_404(BoardModel, pk=pk)
#     return render(request, 'board/detail.html', {'object':object})


# def goodfunc(request, pk):
#     "Written by Koo"
#     object = BoardModel.objects.get(pk=pk)
#     object.good += 1
#     object.save()
#     return redirect('list')


# def readfunc(request, pk):
#     "Written by Koo"
#     object = get_object_or_404(BoardModel, pk=pk)
#     username = request.user.get_username()
#     if username in object.readtext:
#         return redirect('list')
#     else:
#         object.read = object.read + 1
#         object.readtext = object.readtext + ' ' + username
#         object.save()
#         return redirect('list')



# class BoardCreate(CreateView):
#     "Written by Koo"
#     template_name='board/create.html'
#     model = BoardModel
#     fields = ('title', 'content', 'author', 'snsimage')
#     success_url = reverse_lazy('list')
