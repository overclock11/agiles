from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=30)
    passw = models.CharField(max_length=15)
    photo = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return "Usuario " + self.name + ", con email " + self.email

    def to_dictionary(self):
        return {
            'name': self.name,
            'user': self.user,
            'passw': self.passw,
            'photo': self.photo,
            'country': self.country,
            'city': self.city,
            'address': self.address,
            'email': self.email
        }

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Favorito del usuario " + self.user.name + " hacia la categoría " + self.category.name

class Promotion(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()
    description = models.TextField()
    image = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Commentary(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "Comentario de usuario " + self.user + " en promoción " + self.promotion.name