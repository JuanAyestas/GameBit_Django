from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from review_bit.models import Review
from .models import Picture

# Create your views here.

class ReviewPictureDetail(DetailView):
    model = Review
    context_object_name = "review"
    template_name = "picture_bit/picture_detail.html"
    # "review_pics": Picture.objects.filter(review=get_object_or_404(Review, pk=self.kwargs.get("pk")))


class ReviewPictureDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Picture
    context_object_name = "picture"
    success_message = "The picture has been deleted successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "review": get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        }) 
        return context
    
    def test_func(self):
        review = get_object_or_404(Review, pk=self.kwargs.get("review_id"))
        if self.request.user == review.author:
            return True
        return False

    def get_success_url(self):
        review = self.object.review
        return reverse_lazy("gamebit-gallery", kwargs={"pk": review.id})
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

