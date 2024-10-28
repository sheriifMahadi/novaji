from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.views.decorators.http import require_POST


def register(request):
    print(request.method)
    if request.method != "POST":
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password = form.data['password']
            email = form.data['email']
            try:
                validate_email(email)
            except ValidationError as e:
                print("bad email provided", e)
                messages.error("Bad email provided")
            new_user = form.save(commit=False)
        else:
            messages.error(request, ("An error occured"))
    
    context = {
        "form": form
    }
    return render(request, "registration/register.html", context)
