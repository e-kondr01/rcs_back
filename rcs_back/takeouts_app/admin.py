from django.contrib import admin

from .models import *


class ContainersTakeoutRequestAdmin(admin.ModelAdmin):
    readonly_fields = [
        "mass"
    ]


admin.site.register(ContainersTakeoutRequest, ContainersTakeoutRequestAdmin)
admin.site.register(TankTakeoutRequest)
admin.site.register(TankTakeoutCompany)
admin.site.register(TakeoutCondition)
admin.site.register(MassTakeoutConditionCommit)
