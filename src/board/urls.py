from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, users
from .views import IndexView, AboutView, CreateProfileView, MypageView
from .views import BoardList, ShowPostView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('mypage/', MypageView.as_view(), name='mypage'),
    path('mypage/<int:pk>', users, name='users'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout', logoutfunc, name='logout'),
    #----------------------------
    # Tett作成掲示板
    path('board/', BoardList.as_view(), name='board_list'),
    path('board/<int:pk>', ShowPostView.as_view(), name='show'),
    path('create_post/', CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/update/', UpdatePostView.as_view(), name='update'),
    path('<int:pk>/delete/', DeletePostView.as_view(), name='delete'),
    # ---------------------------
]


    # # -------Koo作成掲示板--------
    # path('list/', listfunc, name='list'),
    # path('detail/<int:pk>', detailfunc, name='detail'),
    # path('good/<int:pk>', goodfunc, name='good'),
    # path('read/<int:pk>', readfunc, name='read'),
    # path('create/', BoardCreate.as_view(), name='create'),
