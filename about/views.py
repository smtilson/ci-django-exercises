from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about(request):
    if request.method == 'POST':
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_request = collaborate_form.save(commit=True)
            message = "Collaboration request submitted. I will get back to "\
                        "you as soon as I can."
            messages.add_message(request, messages.SUCCESS, message)

    
    about = About.objects.order_by("date_updated").first()
    collaborate_form = CollaborateForm()
    
    context = {'about':about, 'collaborate_form':collaborate_form}

    return render(request, "about/about.html", context)