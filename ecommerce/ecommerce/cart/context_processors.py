from . models import Cart,CartItems
from . views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return  {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            car_items=CartItems.objects.all().filter(cart=cart[:1])
            for i in car_items:
                item_count += i.quantity
        except Cart.DoesnotExist:
            item_count=0
    return dict(item_count=item_count)