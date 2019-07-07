from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Books


@login_required()
def books_detail(request, pk):
    books = get_object_or_404(Books, pk=pk)
    return render(request, 'details.html', {'books': books})
