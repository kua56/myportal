from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from memo.models import Memo
from memo.forms import MemoForm

def top(request):
    # メモ一覧を取得
    memo = Memo.objects.all()
    # テンプレートへ設定するコンテキストを設定
    context = {"memo": memo}
    return render(request, "memo/top.html", context)

@login_required
def memo_new(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.created_by = request.user
            memo.save()
            return redirect(memo_detail, memo_id=memo.pk)
    else:
        form = MemoForm()
    return render(request, "memo/memo_new.html", {'form': form})

def memo_detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, "memo/memo_detail.html", {'memo': memo})

@login_required
def memo_edit(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    if memo.created_by_id != request.user.id:
        return HttpResponseForbidden("このメモの編集は許可されていません")
    
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_detail', memo_id=memo_id)
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo/memo_edit.html', {'form': form})
