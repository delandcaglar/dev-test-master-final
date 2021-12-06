from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200,unique=True)

    def __str__(self) -> str:
        return self.name

class OldHandles(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, verbose_name="seller", related_name='seller')
    name = models.CharField(max_length=200)
    old_handle = models.CharField(max_length=200,unique=True)


