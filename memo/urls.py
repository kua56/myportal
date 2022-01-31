from django.urls import path
from memo import views

urlpatterns = [
    path("new/", views.memo_new, name="memo_new"),
    path("<int:memo_id>/", views.memo_detail, name="memo_detail"),
    path("<int:memo_id>/edit/", views.memo_edit, name="memo_edit"),
    path("<int:memo_id>/comment/new", view.comment_new, name="commnet_new")
]