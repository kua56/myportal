from django.db import models
from django.conf import settings

class Memo(models.Model):
    title = models.CharField('タイトル', max_length=128)
    desc = models.TextField('メモ', blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="投稿者",
        on_delete=models.CASCADE)
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField('コメント', blank=True)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)
    commented_to = models.ForeignKey(Memo,
                                        verbose_name="メモ",
                                        on_delete=models.CASCADE)
    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        verbose_name="投稿者",
                                        on_delete=models.CASCADE) 
    def __str__(self):
        return self.text