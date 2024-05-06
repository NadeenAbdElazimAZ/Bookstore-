from django.db import models
from django.shortcuts import reverse, get_object_or_404

class book(models.Model):
    code = models.IntegerField(unique=True, default=0)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='booksimg/images/', null=True)
    price = models.IntegerField(default=0)
    no_of_pages = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self):
        url = reverse(viewname='bookstore_show', args=[self.id])
        return url
    
    @property
    def edit_url(self):
        url = reverse(viewname='bookstore_edit', args=[self.id])
        return url   
    
    @classmethod
    def create_object(cls, title, author, price, no_of_pages, code, image):
        try:
            book = cls(title=title, author=author, price=price, no_of_pages=no_of_pages, code=code, image=image)
            print(title, author, price, no_of_pages, code, image)
            book.save()
        except Exception as e:
            print(e)
            return False
        else:
            return book
        
    @classmethod
    def get_book_by_id(cls, id):
        return get_object_or_404(cls, id=id)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='booksimg/images/', null=True)
    bdate = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
