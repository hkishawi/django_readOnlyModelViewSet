from django.db import models

# Create your models here.
DESCRIPTIONS = (
    (0, "sunny"),
    (1, "Rain"), 
    (3, "Cloudy"),
    (4, "Snow")
)
class Description(models.Model):
    """model to describe the weather"""
    weather_description = models.IntegerField(choices=DESCRIPTIONS, default=0)
    temperature = models.FloatField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    """returns string respresenation of objecct that was created"""
    def __str__(self):
        return str(self.created_on)