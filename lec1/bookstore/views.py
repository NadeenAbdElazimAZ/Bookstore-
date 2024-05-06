from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse
from bookstore.models import  book,Author
from bookstore.forms import  bookForm,bookModelForm,AuthorForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def welcome(request):
        return render(request,
                     template_name="welcome.html",
                    )
        


books = [
        {"code":1,"name":"idiot brain part 1","price":200,"author":"Dean Buenett","no_of_papers":400,"image":"img1.jpg"},
        {"code":2,"name":"idiot brain part 2","price":250,"author":"Dean Buenett","no_of_papers":500,"image":"img2.jpg"},
        {"code":3,"name":"idiot brain part 3","price":300,"author":"Dean Buenett","no_of_papers":600,"image":"img3.jpg"}


]
def index(request):
        return HttpResponse(books)


def profile(request,code):
        #print(type(code))
        #for bk in books:
        #       if bk['code']==code:
        filtered_books=filter(lambda book:book['code']==code,books)
        filtered_books=list(filtered_books)
        if filtered_books:
                      # return HttpResponse(filtered_books[0].values())
                 return render(request, 
                            template_name='bookStoreHome.html',
                            context={"book":filtered_books[0]})
        
        return HttpResponse("book not found")



def landing(request):
        return render(request,
                     template_name="landing.html",
                     context={"books":books})
        #print(books)
       # return HttpResponse("heloo")

def books_index(request):
    books = book.objects.all()
    return render(request, template_name="index.html", context={"books": books})

def books_show(request, id):
    try:
        book_instance = book.objects.get(id=id)
        return render(request, template_name="show.html", context={"book": book_instance})
    except book.DoesNotExist:
        return HttpResponse("Book not found")

@login_required(login_url='/users/login')
def books_add(request):
     print(request)
     if request.method=='POST':
             
             print(request.FILES)
             print(request.POST)
             title = request.POST["title"]
             code = request.POST["code"]
             #image = request.POST["image"]
             author = request.POST['author']
             price = request.POST["price"]
             no_of_pages = request.POST["no_of_pages"]


             new_book = book()
             new_book.title =  title
             new_book.author = author
             #----------------------------------------------------
             if request.POST["code"]:
                new_book.code = request.POST["code"]
             if request.POST["price"]:
                new_book.price = request.POST["price"]
             if request.POST["no_of_pages"]:
                new_book.no_of_pages = request.POST["no_of_pages"]
                                    
             
             try:
                new_book.image = request.FILES['image']
             except Exception as e:
                pass
            

             
             new_book.save()            
             #return HttpResponse("POST request resived")

             #return redirect("/bookstore/index")
             url = reverse("bookstore_index")
             return redirect(url )
     return render(request, template_name="add.html")
 
        
def books_delete(request,id):
      delbk=book.objects.get(id=id)
      delbk.delete()
      url=reverse("bookstore_index")
      return redirect(url) 



@login_required
def book_create_form(request):
    form = bookForm()
    if request.method == 'POST':
        form = bookForm(request.POST, request.FILES)
        if form.is_valid():
            
            bookss = book.create_object(
                request.POST['title'],
                request.POST['author'], 
                request.POST['price'], 
                request.POST['price'], 
                request.POST['no_of_pages'],
                request.FILES['image'])
         
            if bookss:
               
                url = reverse("bookstore_index")
                return redirect(url)
        # print(request.POST,request.FILES)
            return HttpResponse("data submitted")

    return render(request, template_name='addform.html',
                  context={"form":form})

def book_create_model_form(request):
     form= bookModelForm()

     if request.method=='POST':
           form = bookModelForm(request.POST,request.FILES)
           if form.is_valid():
            book=form.save()
        #     return HttpResponse(book.id)
            return redirect(book.show_url)
 
     return render(request, template_name='addform.html',context={"form":form})


def edit_book(request,id):
     book_instance= book.get_book_by_id(id)
     form = bookModelForm(instance=book_instance) 
     if request.method=='POST': 
          form=bookModelForm(request.POST,request.FILES,instance=book_instance)
          if form.is_valid():
               form.save()
               return redirect(book_instance.show_url)
     return render(request,template_name='edit.html',context={"form":form})
##################3

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/list.html', {'authors': authors})

def show_author_page(request, id):
    author = get_object_or_404(Author, id=id)
    books_by_author = book.objects.filter(author=author)
    return render(request, 'authors/show.html', {'author': author, 'books_by_author': books_by_author})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_authors')
    else:
        form = AuthorForm()
    return render(request, 'authors/add.html', {'form': form})

def edit_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('all_authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/edit.html', {'form': form, 'author': author})

def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('all_authors')
    return render(request, 'authors/delete.html', {'author': author})

def author_create_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('author_index')
    else:
        form = AuthorForm()
    return render(request, 'authors/add.html', {'form': form})