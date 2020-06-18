from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User, Group
from django.views.generic import DetailView
from review_bit.models import Review
from meme_bit.models import Meme

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            
            group = Group.objects.get(name="Visitor")
            group.user_set.add(user)
            
            messages.success(
                request, f"The account has been successfully created. You're now able to log in {username}.")
            return redirect("gamebit-login")
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
        "legend": "GameBit - Visitor",
    }
    return render(request, "users_bit/register.html", context)


def staff_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            
            group = Group.objects.get(name="Staff Member")
            group.user_set.add(user)
            
            messages.success(
                request, f"The account has been successfully created. You're now able to log in {username}.")
            return redirect("gamebit-login")
    else:
        form = UserRegistrationForm()
    context = {
        "form": form,
        "legend": "GameBit - Staff",
    }
    return render(request, "users_bit/register.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        up_form = UserUpdateForm(request.POST, instance=request.user)
        pro_form = ProfileUpdateForm(request.POST, request.FILES,
                                     instance=request.user.profile)
        if up_form.is_valid() and pro_form.is_valid():
            up_form.save()
            pro_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("gamebit-profile")
    else:
        up_form = UserUpdateForm(instance=request.user)
        pro_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "up_form": up_form,
        "pro_form": pro_form,
        "legend": "Update your info",
        "reviews": Review.objects.filter(author_id=request.user.id)
    }
    return render(request, "users_bit/profile.html", context)


class SummaryDetailView(DetailView):
    model = User
    template_name = 'users_bit/summary.html'
    context_object_name = 'author'

