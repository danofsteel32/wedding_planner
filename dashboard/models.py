from django.db import models


class Party(models.Model):
    description = models.CharField(max_length=200, unique=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    zip_code = models.CharField(max_length=32, blank=True)
    phone_number = models.CharField(max_length=32, blank=True, unique=True)
    sent = models.BooleanField(default=False)
    rsvp_id = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.description

    def address_string(self):
        return '%s %s %s %s' % (self.street.upper(), self.city.upper(),
                                self.state.upper(), self.zip_code)


class Guest(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, blank=True)
    plus_ones = models.IntegerField(default=0)
    rsvp = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
