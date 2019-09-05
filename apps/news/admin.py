import lemon

from .models import NewsItem, NewsItemImage


class NewsItemImageInline(lemon.StackedInline):

    model = NewsItemImage
    extra = 1


class NewsItemAdmin(lemon.ModelAdmin):

    list_display = ['title', 'category', 'publication_date']
    list_filter = ['category']
    date_hierarchy = 'publication_date'
    inlines = [NewsItemImageInline]
    markup_fields = ['preview', 'content']
    tabs = True


lemon.site.register(NewsItem, NewsItemAdmin)
