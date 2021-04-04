from django.contrib import admin
from .models import BoardModel, Profile, Board


admin.site.register(BoardModel)
admin.site.register(Profile)
admin.site.register(Board)