from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Author
from django.core.exceptions import ObjectDoesNotExist
from .forms import AuthorForm


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
    except:
        return render(request, 'author_delete.html',
                      {'msg': 'Author could not be deleted!'})


def author_add(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, 'author_add.html',
                      {'form': form})
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save() # Add author to table
            return redirect("/hr/author/list")
        else:
            return render(request, 'author_add.html',
                          {'form': form})


def author_edit(request,id):
    if request.method == "GET":
        try:
            author = Author.objects.get(id=id)
            form = AuthorForm(instance=author)
            return render(request, 'author_edit.html',
                          {'form' : form})
        except ObjectDoesNotExist:
            return render(request, 'author_edit.html',
                          {'msg': 'Author Id Not Found!'})
    else:
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author,data = request.POST)
        form.save()
        return redirect("/hr/author/list")



