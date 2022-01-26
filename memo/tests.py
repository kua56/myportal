from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase, Client, RequestFactory

from memo.models import Memo
from memo.views import top

UserModel = get_user_model()

class TopPageTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username = "test_user",
            email = "test@example.com",
            password = "top_secret_pass001",
        )
        self.memo = Memo.objects.create(
            title = "new memo1",
            desc = "memo contests",
            created_by = self.user,
        )

    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "メモページ", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "memo/top.html")
    
    def test_top_page_should_return_memo_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.memo.title)

    def test_top_page_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)