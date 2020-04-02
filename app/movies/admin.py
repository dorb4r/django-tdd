from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from movies.models import CustomUser, Movie


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    """
    List view of the CustomUser model
    """

    pass


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    List view of the Movie model
    """

    fields = (
        "title",
        "genre",
        "year",
        "created_date",
        "updated_date",
    )
    list_display = (
        "title",
        "genre",
        "year",
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )
