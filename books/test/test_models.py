from mixer.backend.django import mixer
import pytest


@pytest.fixture
def books(request, db):
    return mixer.blend('books.Books', quantity=request.param)


@pytest.mark.parametrize('books', [1], indirect=True)
def test_books_in_stock(books):
    assert books.in_stock == True


@pytest.mark.parametrize('books', [0], indirect=True)
def test_books_in_stock(books):
    assert books.in_stock == False
