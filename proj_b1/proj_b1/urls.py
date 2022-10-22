from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all-students/', all_students),
    path('student/<int:pk>/', single_student),
    path('all-authors/', all_authors),
    path('muallif/<int:a>/', single_author),
    path('delete-student/<int:a>/', delete_student),
    path('add-author/', add_author),
    path('all-books/', all_books),
    path('add-book/', add_book),
    path('edit-book/<int:a>/', edit_book),
    path('login/', login_s),
    path('logout/', logout_s)
]
