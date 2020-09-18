from django.db import models

# Create your models here.
class DailyStateData(models.Model):
    state_id = models.IntegerField(blank=True)
    state_name = models.TextField(blank=True)
    total_corona_cases = models.IntegerField(blank=True)
    confirmed_corona_cases = models.IntegerField(blank=True)
    recovered_corona_cases = models.IntegerField(blank=True)
    deaths_corona_cases = models.IntegerField(blank=True)
    date = models.DateField(blank=True)
    def serialize(self):
        return {
            "id": self.id,
            "state_id": self.state_id,
            "total_corona_cases": self.total_corona_cases,
            "confirmed_corona_cases": self.confirmed_corona_cases,
            "recovered_corona_cases": self.recovered_corona_cases,
            "deaths_corona_cases": self.deaths_corona_cases,
            "date": self.date,
            "state_name": self.state_name
        }


class DailyTotalcases(models.Model):
    date = models.DateField(blank=True)
    total_corona_cases = models.IntegerField(blank=True)
    confirmed_corona_cases = models.IntegerField(blank=True)
    recovered_corona_cases = models.IntegerField(blank=True)
    deaths_corona_cases = models.IntegerField(blank=True)
    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "total_corona_cases": self.total_corona_cases,
            "confirmed_corona_cases": self.confirmed_corona_cases,
            "recovered_corona_cases": self.recovered_corona_cases,
            "deaths_corona_cases": self.deaths_corona_cases
        }