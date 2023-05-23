from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product, Category


def bag_contents(request):
    """
    To display the content in the shopping cart.
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})   

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)

        if product.category.name == 'clearance':
            product.price = product.price - (product.price * Decimal(10 / 100))

        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if (total != 0) and (total < settings.FREE_DELIVERY_THRESHOLD):
        delivery = settings.STANDARD_DELIVERY_COST
        # delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,        
    }

    return context
