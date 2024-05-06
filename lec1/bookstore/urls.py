from django.urls import path
from bookstore.views import welcome, index, profile,landing,books_index,books_show,books_add, books_delete,book_create_form,book_create_model_form,edit_book,author_list,show_author_page,add_author,edit_author,delete_author



urlpatterns = [
    path('home', welcome, name='bookstore_welcome'),
    path('', index, name='bookstore_index'),
    path('<int:code>', profile, name='bookstore_profile'),
    path('land/',landing,name="bookstore_land"),
    path('index/',books_index,name="bookstore_index"),
    path('index/<int:id>',books_show,name="bookstore_show"),
    path('add',books_add,name="bookstore_add"),
    path('index/<int:id>/delete',books_delete,name="bookstore_delete"),
    path('addform',book_create_form,name='book_create_form'),
    path('forms/model/addform',book_create_model_form,name='book_modeladd'),
    path('forms/edit/<int:id>',edit_book,name='bookstore_edit'),
    # URLs for managing authors
    path('authors/', author_list, name='all_authors'), 
    path('authors/<int:id>/', show_author_page, name='show_author_page'), 
    path('authors/add/', add_author, name='add_author'), 
    path('authors/edit/<int:id>/', edit_author, name='edit_author'),  
    path('authors/delete/<int:id>/', delete_author, name='delete_author'),  # URL to delete an author
]