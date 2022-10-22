from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def all_students(request):
    if request.method == 'POST':
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(username=a, password=b)
        if user == None:
            return redirect('/login/')
        else:
            login(request, user)

    if request.user.is_authenticated:
        data = {
            'students': Talaba.objects.all(),
            'ism': "Ali",
            'yosh': 40
        }
        return render(request, 'talabalar.html', data)
    else:
        return redirect('/login/')


def logout_s(request):
    logout(request)
    return redirect('/login/')


def login_s(request):
    return render(request, 'login.html')


def single_student(request, pk):
    data = {
        'talaba': Talaba.objects.get(id=pk)
    }
    return render(request, 'bitta_talaba.html', data)

def all_authors(request):
    if request.user.is_authenticated:
        data = {
            "mualliflar": Author.objects.all()
        }
        return render(request, 'mualliflar.html', data)
    else:
        return redirect('/login/')


def single_author(request, a):
    data = {
        'muallif': Author.objects.get(id=a)
    }
    return render(request, 'bitta_muallif.html', data)


def delete_student(request, a):
    Talaba.objects.get(id=a).delete()
    return redirect('/all-students/')


def add_author(request):
    a = request.POST.get('name')
    b = request.POST.get('age')
    c = request.POST.get('nation')
    Author.objects.create(ism=a, yosh=b, millat=c)
    return redirect('/all-authors/')

def all_books(request):
    data = {
        'kitoblar': Book.objects.all(),
        'mualliflar': Author.objects.all()
    }

    return render(request, 'kitoblar.html', data)

def add_book(request):
    nom = request.POST.get('name')
    yil = request.POST.get('year')
    janr = request.POST.get('genre')
    sahifa = request.POST.get('page')
    muallif_id = request.POST.get('author')

    muallif = Author.objects.get(id=muallif_id)
    Book.objects.create(nom= nom,
                        yil=yil,
                        sahifa=sahifa,
                        janr=janr,
                        muallif=muallif)
    return redirect('/all-books/')


def edit_book(request, a):
    if request.method == "POST":
        nom = request.POST.get('nom')
        yil = request.POST.get('yil')
        janr = request.POST.get('janr')
        sahifa = request.POST.get('sahifa')
        id_muallif = request.POST.get('muallif')
        muallif = Author.objects.get(id=id_muallif)
        Book.objects.filter(id=a).update(nom=nom, yil=yil, janr=janr, sahifa=sahifa, muallif=muallif)



    kitob = Book.objects.get(id=a)
    mualliflar = Author.objects.all()

    data = {
        'book': kitob,
        'authors': mualliflar
    }

    return render(request, 'edit_book.html', data)











