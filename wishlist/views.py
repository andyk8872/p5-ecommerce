from django.shortcuts import render


def wishlist(request):
    """
        Display the wishlist.
    """    
    # wishlist = Wishlist.objects.filter(user=request.user).all()
    # context = {'wishlist': wishlist}

    return render(request, 'wishlist/wishlist.html')
