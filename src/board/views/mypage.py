from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

# ここから追加ライブラリ
from board.models import BoardModel
from django.conf import settings

class MypageView(generic.TemplateView):
    # model = BoardModel
    template_name = "board/mypage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # contextに追加(htmlで使える)
        # context[''] = 
        return context