from django.contrib import admin
from .models import News, Store, BookShelf


class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at', 'link_1', 'link_2', 'link_3',)
    search_fields = ('name', 'description',)
    fieldsets = (
        ("Краткая характеристика книги", {
            'fields': ('name', 'description',)
        }),
        ("Ссылки", {
            'fields': ('link_1', 'link_2', 'link_3',)
        })
    )


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'updated_at',)
    search_fields = ('title', 'text',)
    fieldsets = (
        ("Краткая характеристика книги", {
            'fields': ('title', 'text', 'image')
        }),
        ("Ссылки", {
            'fields': ('link_1', 'link_2', 'link_3',)
        })
    )


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'price', 'created_at', 'updated_at',)
    list_filter = ('gender', 'price',)
    search_fields = ('name',)


admin.site.register(BookShelf, BookshelfAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Store, StoreAdmin)
