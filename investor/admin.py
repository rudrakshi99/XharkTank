from django.contrib import admin
from .models import Investor

# Register your models here.
class InvestorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "investor",
        "amount",
        "equity",
        "comment",
        "created_at",
        "updated_at",
    )
    list_filter = ("investor", "created_at", "updated_at")
    search_fields = ("investor", "created_at", "updated_at")
    ordering = ("-created_at",)


admin.site.register(Investor, InvestorAdmin)
