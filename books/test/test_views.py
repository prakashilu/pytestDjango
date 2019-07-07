from django.contrib.auth.models import User, AnonymousUser
from mixer.backend.django import mixer
from django.urls import reverse
from django.test import RequestFactory
from books.views import books_detail
import pytest


@pytest.fixture
def factory():
    return RequestFactory()


@pytest.fixture
def books(db):
    return mixer.blend('books.Books')


def test_details_info(factory, books):
    urls = reverse('detail', kwargs={'pk': 1})
    request = factory.get(urls)
    request.user = mixer.blend(User)

    response = books_detail(request, pk=1)
    assert response.status_code == 200


def test_details_info(factory, books):
    urls = reverse('detail', kwargs={'pk': 1})
    request = factory.get(urls)
    request.user = AnonymousUser()

    response = books_detail(request, pk=1)
    assert 'accounts/login' in response.url