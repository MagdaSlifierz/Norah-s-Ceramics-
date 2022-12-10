from django.contrib import admin

from .models import Order, OrderProduct


class OrderAdmin(admin.ModelAdmin):
    """
    Admin setting to display list of artwork,
    Ordered by name, with a vertical filter and a
    Search box
    Widget to display image thumbnail in list display
    """

    list_display = [
        "user",
        "status",
        "bill_pence",
        "transaction_id",
        "order_no",
    ]


class OrderProductAdmin(admin.ModelAdmin):
    """
    Admin setting to display list of artwork,
    Ordered by name, with a vertical filter and a
    Search box
    Widget to display image thumbnail in list display
    """

    list_display = [
        "order",
        "product",
    ]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
