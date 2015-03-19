from django.shortcuts import render
from .htmltopdf import render_to_pdf

def pdf(request):
	return render_to_pdf('index.html', {'title':'Reports with PDF'})