from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse

# Create your views here.
from .models import Movie
from .forms import MovieForm


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html', {'page_title': 'Home'})
    else:
        return redirect('app:movies')


@login_required
def movies(request):
    tmp = Movie.objects.all()
    return render(request, 'movies.html', {'movies': tmp})


@login_required
def movie(request, id):
    tmp = get_object_or_404(Movie, id=id)
    return render(request, 'movie.html', {'movie': tmp, 'page_title': tmp.title})


@permission_required('app.change_movie')
def edit(request, id):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            a = Movie.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.review = form.cleaned_data['review']
            a.save()
            return redirect('app:movies')
        else:
            return render(request, 'edit.html', {'form': form, 'id': id})
    else:
        a = Movie.objects.get(id=id)
        form = MovieForm(instance=a)
        return render(request, 'edit.html', {'form': form, 'id': id})

@permission_required('app.add_movie')
def new(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            a = Movie(title=form.cleaned_data['title'], review=form.cleaned_data['review'], owner=request.user)
            a.save()
            return redirect('app:movies')
        else:
            return render(request, 'new.html', {'form': form})
    else:
        form = MovieForm()
        return render(request, 'new.html', {'form': form})
