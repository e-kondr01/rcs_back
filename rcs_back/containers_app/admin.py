from django.contrib import admin

from .models import *


class ContainerAdmin(admin.ModelAdmin):
    readonly_fields = [
        "mass",
        "activated_at",
        "avg_fill_time",
        "avg_takeout_wait_time",
        "cur_fill_time",
        "cur_takeout_wait_time",
        "last_full_report",
        "last_emptied_report",
        "ignore_reports_count",
        "is_full",
        "is_reported_just_enough",
        "check_time_conditions",
        "needs_takeout",
        "get_mass_rule_trigger",
    ]


class BuildingAdmin(admin.ModelAdmin):
    readonly_fields = [
        "current_mass",
        "meets_mass_takeout_condition",
        "meets_time_takeout_condition",
        "needs_takeout",
        "containers_for_takeout",
        "public_days_condition",
        "office_days_condition",
        "is_mass_condition_commited",
        "collected_mass"
    ]


class FullContainerReportAdmin(admin.ModelAdmin):
    readonly_fields = [
        "takeout_wait_time"
    ]


admin.site.register(Container, ContainerAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingPart, BuildingAdmin)
admin.site.register(FullContainerReport, FullContainerReportAdmin)
