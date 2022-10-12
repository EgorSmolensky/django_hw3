from django.shortcuts import render, redirect
from books.models import Book


def books_view(request):
    return redirect('booklist')


def booklist(request):
    template = 'books/books_list.html'
    context = {'books': Book.objects.all()}
    return render(request, template, context)


def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    pub_date = pub_date.date()
    dates = sorted(set(book.pub_date for book in Book.objects.all()))

    position = dates.index(pub_date)
    prev_date, next_date = None, None
    if position > 0:
        prev_date = dates[position - 1]
    if position < len(dates) -1:
        next_date = dates[position + 1]

    books = Book.objects.filter(pub_date=pub_date)
    context = {
        'books': books,
        'next_date': next_date,
        'prev_date': prev_date,
    }
    return render(request, template, context)
