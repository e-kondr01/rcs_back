from django.contrib import admin

from .models import ContainersTakeoutRequest, TakeoutCondition, TankTakeoutRequest


class ContainersTakeoutRequestAdmin(admin.ModelAdmin):
    readonly_fields = [
        "mass",
        "unconfirmed_containers",
        "emptied_containers_match"
    ]


class TankTakeoutRequestAdmin(admin.ModelAdmin):
    readonly_fields = [
        "wait_time",
        "fill_time",
        "mass",
        "confirmed_mass_match",
        "mass_difference"
    ]


admin.site.register(ContainersTakeoutRequest, ContainersTakeoutRequestAdmin)
admin.site.register(TankTakeoutRequest, TankTakeoutRequestAdmin)
admin.site.register(TakeoutCondition)
