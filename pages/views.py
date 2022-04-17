from django.shortcuts import render
from .models import Page
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def pages_list(request):
	page = Page.objects.all().order_by('title')
	return render(request, 'pages/pages_list.html',{'page': page})

@login_required(login_url="/accounts/login/")
def pages_detail(request,slug):
	pages = Page.objects.get(slug=slug)
	
	if pages.slug == 'producer':
		return render(request, 'pages/producer.html',{'pages':pages})
	elif pages.slug == 'label':
		return render(request, 'pages/label.html',{'pages':pages})
	elif pages.slug == 'artist':
		return render(request, 'pages/artist.html',{'pages':pages}) # 'folder_name/html_page'
	elif pages.slug == 'songs':
		return render(request, 'pages/song.html',{'pages':pages})
	elif pages.slug == 'genre':
		return render(request, 'pages/genre.html',{'pages':pages})
	elif pages.slug == 'album':
		return render(request, 'pages/album.html',{'pages':pages})
	else:
		return render(request, 'pages/pages_detail.html',{'pages':pages})
