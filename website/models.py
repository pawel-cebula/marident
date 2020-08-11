from django.db import models


class Procedure(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    # cateory choices
    CONSERVATIVE = 'CONS'
    ENDODONTICS = 'ENDO'
    SURGERY = 'SURG'
    PROSTHETICS = 'PROS'

    CATEGORY_CHOICES = [
        (CONSERVATIVE, 'Stomatologia zachowawcza'),
        (ENDODONTICS, 'Endodoncja'),
        (SURGERY, 'Chirurgia stomatologiczna'),
        (PROSTHETICS, 'Protetyka')
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'inquiries'

    def __str__(self):
        return self.subject
