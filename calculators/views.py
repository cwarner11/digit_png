from django.shortcuts import render
from .models import Calculator
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url="/accounts/login/")
def calculators_list(request):
	calculator = Calculator.objects.all().order_by('title')
	return render(request, 'calculators/calculators_list.html',{'calculator': calculator})

@login_required(login_url="/accounts/login/")
def calculator_detail(request,slug):
	calcs = Calculator.objects.get(slug=slug)
	
	if calcs.slug == 'producer':
		return render(request, 'calculators/producer.html',{'calcs':calcs})
	elif calcs.slug == 'label':
		return render(request, 'calculators/label.html',{'calcs':calcs})
	elif calcs.slug == 'artist':
		return render(request, 'calculators/artist.html',{'calcs':calcs}) # 'folder_name/html_page'
	elif calcs.slug == 'songs':
		return render(request, 'calculators/song.html',{'calcs':calcs})
	elif calcs.slug == 'genre':
		return render(request, 'calculators/genre.html',{'calcs':calcs})
	elif calcs.slug == 'album':
		return render(request, 'calculators/album.html',{'calcs':calcs})
	else:
		return render(request, 'calculators/calculators_detail.html',{'calcs':calcs})
