from django.db import models

class Murojaat(models.Model):
    matn = models.TextField()
    def __str__(self):
        return self.matn

class Menu(models.Model):
    nom = models.CharField(max_length=30, null=True, blank=True)
    nomeng = models.CharField(max_length=30, null=True, blank=True)
    nomru = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.nom

class Home_page(models.Model):
    ism = models.CharField(max_length=50, null=True, blank=True)
    ismru = models.CharField(max_length=50, null=True, blank=True)

    matn = models.CharField(max_length=100, null=True, blank=True)
    matneng = models.CharField(max_length=100, null=True, blank=True)
    matnru = models.CharField(max_length=100, null=True, blank=True)

    haqida = models.CharField(max_length=20, null=True, blank=True)
    haqidaeng = models.CharField(max_length=20, null=True, blank=True)
    haqidaru = models.CharField(max_length=20, null=True, blank=True)


    rasm = models.ImageField(blank=True, null=True)


    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=100, null=True, blank=True)
    sarlavhaeng = models.CharField(max_length=100, null=True, blank=True)
    sarlavharu = models.CharField(max_length=100, null=True, blank=True)

    matn = models.TextField(null=True, blank=True)
    matneng = models.TextField(null=True, blank=True)
    matnru = models.TextField(null=True, blank=True)

    sana = models.DateField(auto_now_add=True)
    bosh_sahifa_uchun = models.BooleanField(default=False)
    korilganlik = models.PositiveIntegerField(default=0)

    rasm1 = models.ImageField(null=True, blank=True)
    rasm2 = models.ImageField(null=True, blank=True)
    rasm3 = models.ImageField(null=True, blank=True)
    rasm4 = models.ImageField(null=True, blank=True)
    rasm5 = models.ImageField(null=True, blank=True)
    rasm6 = models.ImageField(null=True, blank=True)
    rasm7 = models.ImageField(null=True, blank=True)
    rasm8 = models.ImageField(null=True, blank=True)
    rasm9 = models.ImageField(null=True, blank=True)
    rasm10 = models.ImageField(null=True, blank=True)
    def __str__(self):
        return  self.sarlavha


class Video(models.Model):
    # sarlavha = models.CharField(max_length=100, null=True, blank=True)
    # sarlavhaeng = models.CharField(max_length=100, null=True, blank=True)
    # sarlavharu = models.CharField(max_length=100, null=True, blank=True)
    #
    # matn = models.TextField(null=True, blank=True)
    # matneng = models.TextField(null=True, blank=True)
    # matnru = models.TextField(null=True, blank=True)

    sana = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    rasm = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.url


class Ijtimoiy_tarmoq_url(models.Model):
    nom = models.CharField(max_length=30)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.nom


class Haqida_toliq(models.Model):
    sarlavha = models.CharField(max_length=50, null=True, blank=True)
    sarlavhaeng = models.CharField(max_length=50, null=True, blank=True)
    sarlavharu = models.CharField(max_length=50, null=True, blank=True)

    matn = models.TextField(null=True, blank=True)
    matneng = models.TextField(null=True, blank=True)
    matnru = models.TextField(null=True, blank=True)

    rasm = models.ImageField(null=True, blank=True)

    hozirgi_orni = models.CharField(max_length=200, null=True, blank=True)
    hozirgi_ornieng = models.CharField(max_length=200, null=True, blank=True)
    hozirgi_orniru = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.sarlavha

class Faoliyat_joy(models.Model):
    nom = models.CharField(max_length=30)
    rasm = models.ImageField()

    def __str__(self):
        return self.nom

class Hamkor(models.Model):
    nom = models.CharField(max_length=50, null=True, blank=True)
    rasm = models.ImageField()

    def __str__(self):
        return self.nom

