from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from board.models import BoardModel, Board, Profile
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

    def get(self, request, *args, **kwargs):
        """get関数

        プロフィールデータを取得
        """
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        
        my_posts = Board.objects.order_by('-id')
        return render(request, 'board/mypage.html', {
            'profile_data': profile_data,
            'my_posts': my_posts
        })



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



class MypageAnswersView(generic.TemplateView):
    "マイページのAnswersを表示"
    template_name = "board/mypage_answers.html"



class MypageNiceswingsView(generic.TemplateView):
    "マイページのNice Swingsを表示"
    template_name = "board/mypage_niceswings.html"
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


def detailfunc(request, pk):
    "Written by Koo"
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'board/detail.html', {'object':object})


def goodfunc(request, pk):
    "Written by Koo"
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')


def readfunc(request, pk):
    "Written by Koo"
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
    "Written by Koo"
    template_name='board/create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'snsimage')
    success_url = reverse_lazy('list')



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


# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.views.generic import ListView
# from django.views.generic import DetailView
# from django.views.generic import CreateView
# from django.views.generic import UpdateView
# from django.views.generic import DeleteView
# from django.shortcuts import redirect
# from django.contrib import messages
# from django.urls import reverse_lazy
# from .forms import PhotoForm
# from .forms import CommentForm
# from .models import PhotoModel, Document, Board


# class MainView(TemplateView):
#     template_name = "board/main.html"


#     def get_context_data(self):
#         context = super().get_context_data()
#         context["num_app"] = 0
#         context["skills"] = [
#             "python(勉強中)",
#             "django(勉強中)",
#             "html(勉強中)",
#             "css(勉強中)",
#             "AWS(勉強中)"
#         ]
#         return context

# class AwsView(TemplateView):
#     template_name = "board/home.html"

# class Photo(CreateView):
#     model = PhotoModel
#     form_class = PhotoForm
#     #template_name = 'board/aws_upload/aws_upload.html'
#     success_url = reverse_lazy('board:index')
#     #success_url = 'aws_upload/aws_upload.html'

#     def get_context_data_photo(self, **kwargs):
#         #最初に継承元のメソッドを呼び出す
#         context = super(Photo, self).get_context_data_photo(**kwargs)
#         context["photos"] = PhotoModel.objects.all()
#         return context


# class DocumentCreateView(CreateView):
#     model = Document
#     fields = ['upload',]
#     success_url = reverse_lazy('home')

#     def get_context_data_document(self, **kwargs):
#         context = super().get_context_data_document(**kwargs)
#         documents = Document.objects.all()
#         context['documents'] = documents
#         return context


