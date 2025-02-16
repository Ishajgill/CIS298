from django.db import models

class Search(models.Model):
    departure = models.CharField(max_length=10, blank=True, null=True)
    arrival = models.CharField(max_length=10, blank=True, null=True)
    flight_number = models.CharField(max_length=20, blank=True, null=True)
    airline = models.CharField(max_length=50, blank=True, null=True)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.departure} to {self.arrival} - {self.flight_number or 'No Flight Number'}"
