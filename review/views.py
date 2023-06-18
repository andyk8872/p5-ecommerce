from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import View
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def make_review(request):
    """
    Enables logged on user to create a review.
    """
    if request.method == 'POST':
        review = Review(user=request.user)
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Review posted.'
                )
            return redirect('show_review')

    else:
        form = ReviewForm()
        context = {
            'form': form,
            }
    return render(request, 'review/make_review.html', context)


def show_review(request):
    """
    Displays the reviews.
    """
    reviews = Review.objects.all()
    # Set up pagination
    p = Paginator(Review.objects.all(), 3)
    page = request.GET.get('page')
    reviewed = p.get_page(page)

    context = {
        'reviews': reviews,
        'reviewed': reviewed,
    }
    return render(request, 'review/show_review.html', context)


@login_required
def delete_items(request, review_id):
    """ Delete a review """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('show_review'))


@login_required
def edit_review(request, review_id):
    """
    The review creater can edit the review.
    """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Update successful...'
                )
            return redirect('show_review')
        else:
            messages.error(request, 'Error. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        context = {
            'form': form,
            }
    return render(request, 'review/edit_review.html', context)
