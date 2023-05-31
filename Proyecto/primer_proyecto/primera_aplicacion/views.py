from django.shortcuts import render

# Create your views here.
def index_welcome(request):
    print('############## LLEGO ##############')
    return render(request, 'index.html')