from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

"""admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)'
admin.site.register(Genre)
admin.site.register(Language)"""

"""admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)'
admin.site.register(Genre)
admin.site.register(Language)"""

admin.site.register(Genre)
admin.site.register(Language)

"""admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)'
admin.site.register(Genre)
admin.site.register(Language)"""

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """creating Administration  .
    Defines:
     - fields to be displayed in list view (list_display)
     - feilds in detail,
       horizontally grouping the fields
     - inline addition of author
    """
    list_display = ('last_name',
                    'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    """Format instertion in book instance (Inline)"""
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    """Administration object for Book models.
    Defines:
     - Display of fields in List view (list_display)
     - this also add the book object  (inlines)
    """
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


admin.site.register(Book, BookAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """object administration for bookistance.
    this defines the following:
     - List view display in fields (list_display)
     - Sidebar filter display (list_filter)
     - firlds to sections grouping (fieldsets)
    """
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
