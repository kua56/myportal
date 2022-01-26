from django.contrib import admin
from memo.models import Memo


# 管理画面にアプリを追加
admin.site.register(Memo)