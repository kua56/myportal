from django.http import HttpResponse
from django.shortcuts import render
from memo.models import Memo

def top(request):
    # メモ一覧を取得
    memo = Memo.objects.all()
    # テンプレートへ設定するコンテキストを設定
    context = {"memo": memo}
    return render(request, "memo/top.html", context)

def memo_new(request):
    return HttpResponse('メモの登録')

def memo_detail(request, memo_id):
    return HttpResponse('メモの詳細')

def memo_edit(request, memo_id):
    return HttpResponse('メモの編集')