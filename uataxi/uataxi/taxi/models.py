from django.db import models


class TaxiService(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class PhoneOperator(models.Model):
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    service = models.ForeignKey(TaxiService)
    operator = models.ForeignKey(PhoneOperator)
    callback = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number
