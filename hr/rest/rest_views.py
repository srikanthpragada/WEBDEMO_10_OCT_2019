from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from hr.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email', 'mobile','profile')


@api_view(['GET', 'POST'])
def process_authors(request):
    if request.method == "GET":
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    else:  # Post
        author = AuthorSerializer(data=request.data)
        if author.is_valid():
            author.save()  # insert into table
            return Response(author.data)
        else:
            return Response(author.errors, status=400)  # bad request


@api_view(['GET', 'DELETE'])
def process_author(request, id):
    try:
        author = Author.objects.get(id=id)
    except:
        return Response(status=404)  # not found

    if request.method == "GET":
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    else:  # DELETE
        author.delete()
        return Response(status=204)  # No data
