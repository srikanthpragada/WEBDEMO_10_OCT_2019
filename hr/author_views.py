from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Author
from django.core.exceptions import ObjectDoesNotExist


def author_home(request):
    details = Author.objects.all().aggregate(author_count=Count('id'))
    return render(request, 'author_home.html',
                  {'count': details['author_count']})


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html',
                  {'authors': authors})


def author_delete(request,id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return redirect("/hr/author/list")
    except ObjectDoesNotExist:
        return render(request,'author_delete.html',
                      {'msg':'Author Id Not Found!'})




