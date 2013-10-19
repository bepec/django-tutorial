from django.contrib import admin
from taxi.models import TaxiService, PhoneOperator, PhoneNumber


class PhonesInline(admin.StackedInline):
    model = PhoneNumber
    extra = 5


class TaxiServiceAdmin(admin.ModelAdmin):
    inlines = [PhonesInline]


class PhoneNumberAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['number']}),
        ('Taxi', {'fields': ['service']}),
        ('Number info', {'fields': ['operator', 'callback']}),
    ]


admin.site.register(TaxiService, TaxiServiceAdmin)
admin.site.register(PhoneOperator)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
