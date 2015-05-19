from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
	return HttpResponse('This is a working example!<br/><h1>Django</h1><br/>')

from contact_app.models import Contact

def contact_list(request):
	my_contact=Contact.objects.all()
	res = "<h1>List of Contact</h1>"
	for c in my_contact:
		res+=c.firstname+"<br/> "+c.lastname + "<br/>"
	return HttpResponse(res)

def test_template (request):
	my_contact = Contact.objects.all()
	var = {}
	var['title'] = 'the title of my page from the context variable'
	var['contacts'] = my_contact
	return render(request, 'home.html', var)


def index (request):

	return render(request, 'index.html')

def contact_list_gender(request):
	details=Contact.objects.all()
	b = "<h1>Contacts</h1>"
	for d in details:
		b+=d.firstname+"<br/> "+d.lastname + "<br/>"+d.gender+"<br/>"
	return HttpResponse(b)
