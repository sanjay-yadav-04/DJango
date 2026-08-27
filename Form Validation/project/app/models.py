import re
from django.core.exceptions import ValidationError
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=50)
    
    
    def clean(self):
        errors = {}

        # Name validation
        if not self.name.isalpha():
            errors['name'] = "Name must contain only alphabets"
        elif len(self.name) < 3 or len(self.name) > 10:
            errors['name'] = "Name must be between 3 and 10 characters"

        # Age validation
        if self.age < 18 or self.age > 60:
            errors['age'] = "Age must be between 18 and 60"

        # Email validation
        if not self.email.endswith("@gmail.com"):
            errors['email'] = "Only Gmail email allowed"
        # City validation
        if not self.city.isalpha():
            errors['city'] = "city must contain only alphabets"
        elif len(self.name) < 3 or len(self.city) > 10:
            errors['city'] = "city must be between 3 and 10 characters"

        

        # Raise all errors together
        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        # agar aap clean() ke baad save() override karke usme
        # full_clean() call karte ho, to Model.objects.create() par validation hoga
        super().save(*args, **kwargs)
