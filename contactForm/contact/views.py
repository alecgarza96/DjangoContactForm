from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def index(request):
	return render(request, "index.html")

def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['alecgarza96@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return redirect('success')
	return render(request, "contact.html", {'form': form})

def success(request):
	return HttpResponse("It was a success!")