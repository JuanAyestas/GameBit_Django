from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from users_bit.decorators import allowed_users
from picture_bit.models import Picture
from picture_bit.forms import PictureForm
from .forms import ReviewForm
from .models import Review

admin_decorator = allowed_users(allowed_roles=["Staff Member", "Dynamic Duo"])
meme_decorator = allowed_users(allowed_roles=["Staff Member", "Dynamic Duo", "Visitor"])

# Create your views here.

class ReviewListView(ListView):
    model = Review
    context_object_name = "reviews"
    ordering = ["-date_updated"]
    paginate_by = 4


@login_required
@allowed_users(allowed_roles=["Staff Member", "Dynamic Duo"])
def ReviewCreate(request):
    if request.method == "POST":
        form = ReviewForm(request.POST or None,
                          request.FILES or None, instance=request.user)
        form_pic = PictureForm(request.FILES or None)
        files = request.FILES.getlist("picture_files")
        if form.is_valid() and form_pic.is_valid():
            user = request.user
            title = form.cleaned_data["title"]
            platform = form.cleaned_data["platform"]
            thumbnail = form.cleaned_data["thumbnail"]
            summary = form.cleaned_data["summary"]
            content = form.cleaned_data["content"]
            review_obj = Review.objects.create(title=title, platform=platform, thumbnail=thumbnail,
                                               summary=summary, content=summary, author=user)
            rev_id = review_obj.id
            for f in files:
                Picture.objects.create(review=review_obj, picture_files=f)
            messages.success(request, f"Your review has been posted!")
            return redirect("gamebit-detail", pk=rev_id)
    else:
        form = ReviewForm()
        form_pic = PictureForm()
    context = {
        "form": form,
        "form_pic": form_pic,
        "brand": "Gamebit Council"
    }
    return render(request, "review_bit/review_form.html", context)


class ReviewDetailView(DetailView):
    model = Review
    context_object_name = "review"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"brand": "Gamebit Council"})
        return context


@method_decorator(admin_decorator, name="dispatch")
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    success_message = "The review has been updated successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"brand": "Gamebit Council"})
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False


@method_decorator(admin_decorator, name="dispatch")
class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    context_object_name = "review"
    success_url = "/reviews"
    success_message = "The review has been deleted successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"brand": "Gamebit Council"})
        return context

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.author:
            return True
        return False
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class ReviewSearchResult(ListView):
    model = Review
    ordering = ["-date_updated"]
    template_name = "review_bit/review_search.html"
    
    def get_queryset(self):
        search = self.request.GET.get("review")
        review_list = Review.objects.filter(
            Q(title__icontains=search) | Q(platform__icontains=search)
        )
        return review_list


# class ReviewCreateView(LoginRequiredMixin, CreateView):
#     model = Review
#     fields = ["title", "platform", "thumbnail", "summary", "content"]
#     success_message = "The review has been posted successfully!"

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         messages.success(self.request, self.success_message)
#         return super().form_valid(form)
