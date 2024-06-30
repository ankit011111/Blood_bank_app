from django.db import models

class Donate_blood(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.TextField()
    blood_group = models.CharField(
        max_length=30,
        choices=BLOOD_GROUP_CHOICES,
    )
    age = models.TextField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='M',
    )
    address = models.TextField()
    
    def __str__(self):
        return f'{self.name} ({self.blood_group}, {self.gender})'


class Purchase_blood(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.TextField()
    blood_group = models.CharField(
        max_length=30,
        choices=BLOOD_GROUP_CHOICES,
    )
    age = models.TextField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='M',
    )
    address = models.TextField()
    
    def __str__(self):
        return f'{self.name} ({self.blood_group}, {self.gender})'