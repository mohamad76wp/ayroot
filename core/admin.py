from django.contrib import admin
from .models import Post, Category

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "display_category", "update_at", "create_at", "slug")
    list_filter = ("category",)
    readonly_fields = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_title", "parent", "slug")
    readonly_fields = ("slug",)
    list_filter = ("parent",)
