from django.contrib import admin
from .models import Entrepreneur


class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "entrepreneur",
        "pitchTitle",
        "pitchIdea",
        "askAmount",
        "equity",
        "created_at",
        "updated_at",
    )
    list_filter = ("entrepreneur", "created_at")


admin.site.register(Entrepreneur, EntrepreneurAdmin)
