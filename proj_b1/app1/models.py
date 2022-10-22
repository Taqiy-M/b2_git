from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Author(models.Model):
    MILLAT = (
        ["O'zbek", "O'zbek"],
        ["Ingliz", "Ingliz"],
        ["Turk", "Turk"],
        ["Arab", "Arab"],
        ["Rus", "Rus"]
    )
    ism = models.CharField(max_length=30)
    yosh = models.PositiveIntegerField()
    tirik = models.BooleanField(default=True)
    millat = models.CharField(max_length=30, choices=MILLAT)

    def __str__(self):
        return self.ism


class Book(models.Model):
    JANR = (
        ['Ilmiy', "Ilmiy"],
        ['Badiiy', "Badiiy"],
        ["Detektiv", "Detektiv"],
        ["Psixologik", "Psixologik"],
        ["Fantastik", "Fantastik"]
    )

    nom = models.CharField(max_length=40)
    yil = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30, choices=JANR, null=True, blank=True, default=None)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Talaba(models.Model):
    JINS = (
        ['Erkak', 'Erkak'],
        ['Ayol', 'Ayol'],
    )

    CITIES = (
        ['Andijon', "Andijon"],
        ["Farg'ona", "Farg'ona"],
        ["Marg'ilon", "Marg'ilon"],
        ['Toshkent', "Toshkent"],
    )

    ism = models.CharField(max_length=40)
    yosh = models.PositiveIntegerField(blank=True, null=True)
    kurs = models.PositiveSmallIntegerField()
    jins = models.CharField(max_length=20, null=True, default=None, choices=JINS)
    universitet = models.CharField(max_length=40, null=True, blank=True, default=None)
    shahar = models.CharField(max_length=30, choices=CITIES, null=True, blank=True, default=None)

    def __str__(self):
        return self.ism


class Record(models.Model):
    HAYOQ = (
        ['Ha', 'Ha'],
        ["Yo'q", "Yo'q"]
    )
    student = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    berilgan_sana = models.DateTimeField(auto_created=True)
    qaytardi = models.CharField(max_length=10, choices=HAYOQ)
    qaytarilgan_sana = models.DateTimeField(null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.student.ism

class Tadbirkor(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)


class Hello_World(models.Model):
    berilgan_sana = models.DateTimeField(auto_created=True)
    qaytardi = models.CharField(max_length=10, choices=HAYOQ)
    qaytarilgan_sana = models.DateTimeField(null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.ism


class Hello_ZED(models.Model):
    berilgan_sana = models.DateTimeField(auto_created=True)
    qaytardi = models.CharField(max_length=10, choices=HAYOQ)
    qaytarilgan_sana = models.DateTimeField(null=True, blank=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.ism




# class User:
#     username
#     password
#     email
#     is_active
#     is_staff
#     is_superuser
#

