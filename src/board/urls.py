from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, BoardCreate, IndexView, AboutView
from .views import MypageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name='good'),
    path('read/<int:pk>', readfunc, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('mypage/', MypageView.as_view(), name='mypage')
]

# from django.urls import path

# from .views import IndexView, MainView, AboutView, AwsView, Photo, BoardList
# from .views import ShowCommentView, CreateCommentView, UpdateCommentView, DeleteCommentView

# app_name = "board"
# urlpatterns = [
#     path('', IndexView.as_view()),
#     path('main/', MainView.as_view()),
#     path('about/', AboutView.as_view()),
#     path('aws/', Photo.as_view()),
#     path('board/', BoardList.as_view(), name='index'),
#     path('board/<int:pk>', ShowCommentView.as_view(), name='show'),
#     path('create/', CreateCommentView.as_view(), name='create'),
#     path('<int:pk>/update/', UpdateCommentView.as_view(), name='update'),
#     path('<int:pk>/delete/', DeleteCommentView.as_view(), name='delete'),
# ]
