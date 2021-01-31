from django.shortcuts import render
from .forms import DictForm
import requests

# Create your views here.

def home(request):
	if request.method == "POST":
		w = request.POST.get('word')
		try:
			a1 = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
			a2 = w
			wa = a1+a2

			res = requests.get(wa)


			data = res.json()
			meaning = data[0]['meanings'][0]['definitions'][0]['definition']
			msg ="Meaning: " + str(meaning)
			fm = DictForm()
			return render(request, 'home.html', {'fm':fm,'msg':msg,'words':w})
		except Exception as e: 		
			fm = DictForm()
			return render(request, 'home.html', {'fm':fm,'err':'Word Does Not Exists','words':w})
	else:
		fm = DictForm()
		return render(request, 'home.html', {'fm':fm})