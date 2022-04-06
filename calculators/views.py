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
	
	if calcs.slug == 'weight-calculator':
		return render(request, 'calculators/weight.html',{'calcs':calcs})
	elif calcs.slug == 'temperature-calculator':
		return render(request, 'calculators/temp.html',{'calcs':calcs})
	elif calcs.slug == 'length-calculator':
		return render(request, 'calculators/length.html',{'calcs':calcs})
	else:
		return render(request, 'calculators/calculators_detail.html',{'calcs':calcs})
