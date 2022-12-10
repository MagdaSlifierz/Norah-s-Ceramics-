from basket.models import Basket


def global_variables(request):
    basket = Basket.get_basket(request)

    context = {
        "total_basket_price": basket.total_basket_price(),
    }
    return context
