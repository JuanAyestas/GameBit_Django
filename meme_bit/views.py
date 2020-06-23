from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.contrib import messages
from .models import Meme

# Create your views here.

class MemeListView(ListView):
    model = Meme
    context_object_name = "memes"
    ordering = ["-date_updated"]
    paginate_by = 10


class MemeDetailView(DetailView):
    model = Meme
    context_object_name = "meme"


class MemeCreateView(LoginRequiredMixin, CreateView):
    model = Meme
    fields = ["caption", "meme"]
    success_message = "The meme has been uploaded successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class MemeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Meme
    fields = ["caption", "meme"]
    success_message = "The meme has been updated successfully!"

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)
    
    def test_func(self):
        meme = self.get_object()
        if self.request.user == meme.author:
            return True
        return False


class MemeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Meme
    context_object_name = "meme"
    success_url = "/memes"
    success_message = "The meme has been deleted successfully!"
    
    def test_func(self):
        meme = self.get_object()
        if self.request.user == meme.author:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class MemeSearchResult(ListView):
    model = Meme
    ordering = ["-date_updated"]
    template_name = "meme_bit/meme_search.html"

    def get_queryset(self):
        search = self.request.GET.get("meme")
        meme_list = Meme.objects.filter(
            Q(caption__icontains=search)
        )
        return meme_list
