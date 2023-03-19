"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "github",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "github",
        "resume",
        "email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
