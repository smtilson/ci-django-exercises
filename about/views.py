from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    about = About.objects.order_by("date_updated").first()
    context = {'about':about}
    return render(request, "about/about.html",context)