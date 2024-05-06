from django.contrib import admin

from electronics_store.models import Supplier, Contact, Product


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Отображение контактных данных в административной панели. """
    list_display = ('id', 'country', 'city',)
    list_display_links = ['id', 'country']
    list_filter = ('country', 'city',)


@admin.action(description='Очистить задолженность')
def set_null_debts(modeladmin, request, queryset):
    """ Действие очищает задолженность (ставит поле debt=0). """
    queryset.update(debt=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """ Отображение поставщиков в административной панели. """
    list_display = (
        'id', 'company_name', 'supplier_name', 'debt',
        'link_type', 'contacts',
    )
    list_filter = ('contacts__city', 'contacts__country',)
    list_display_links = ['id', 'supplier_name']
    search_fields = ('id', 'company_name', 'link_type',)
    actions = [set_null_debts]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ Отображение товара в административной панели. """
    list_display = ('id', 'title', 'supplier')
    list_filter = ('supplier__contacts__city', 'supplier__contacts__country',)
    list_display_links = ['title']
