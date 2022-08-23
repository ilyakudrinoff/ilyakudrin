from django.contrib import admin
from .models import News, Store, BookShelf


class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description', 'count', 'created_at', 'updated_at', 'name_1', 'name_2', 'name_3',)
    search_fields = ('name', 'description',)
    fieldsets = (
        ("Краткая характеристика книги", {
            'fields': ('name', 'description', 'image', 'count',)
        }),
        ("Ссылки", {
            'fields': ('name_1', 'link_1', 'name_2', 'link_2', 'name_3', 'link_3',)
        })
    )


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'updated_at',)
    search_fields = ('title', 'text',)
    fieldsets = (
        ("Краткая характеристика книги", {
            'fields': ('title', 'text', 'image')
        }),
    )


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'price', 'created_at', 'updated_at',)
    list_filter = ('gender', 'price',)
    search_fields = ('name',)


admin.site.register(BookShelf, BookshelfAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Store, StoreAdmin)
