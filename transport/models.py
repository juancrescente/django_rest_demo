from django.contrib.gis.db import models


class Language(models.Model):
    short_name = models.CharField(max_length=4)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.short_name


class Currency(models.Model):
    symbol = models.CharField(max_length=4)
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.symbol


class Provider(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=40)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    poly = models.PolygonField()

    def __str__(self):
        return "%s: Service area [id=%i] " % (self.provider, self.pk)
