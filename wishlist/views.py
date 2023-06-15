from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Wishlist
from products.models import Product
from django.contrib import messages


def wishlist(request):
    """
        Display the wishlist.
   """
    wishlist = Wishlist.objects.filter(user=request.user).all()
    context = {'wishlist': wishlist}

    return render(request, 'wishlist/wishlist.html', context)


def add_to_wish_list(request):
    '''
        Adds a product to the user's
        wish list
    '''
    if request.method == 'POST':
        product_id = request.POST.get('product-id')
        product = Product.objects.get(id=product_id)
        try:
            wish_item = Wishlist.objects.get(
                                             user=request.user,
                                             product=product
                                             )
            if wish_item:
                messages.info(
                              request,
                              f'{wish_item.product.name }\
                              already in wish list.')
        except Wishlist.DoesNotExist:
            Wishlist.objects.create(user=request.user, product=product)
            messages.success(request, f'Item added to wish list')
        finally:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_item(request):
    '''
        Removes product item from user's wishlist
    '''
    if request.method == 'POST':
        item_id = request.POST.get('item-id')
        wishlist = get_object_or_404(Wishlist, id=item_id)
        wishlist.delete()
        messages.info(
            request,
            f'You have deleted the {wishlist.product.name} from your wishlist'
            )
        return HttpResponseRedirect(reverse('wishlist:wishlist'))
