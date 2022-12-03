from django.db import models


class Currency(models.Model):
    symbol = models.TextField()


class Country(models.Model):
    symbol = models.TextField()


class Account(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
