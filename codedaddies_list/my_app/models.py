from django.db import models

# Create your models here.
class Search(models.Model):
    # in our model called Search, create one field named search, all search takes in an input
    search = models.CharField(max_length=500)
    # timestamp field (created_at)
    created = models.DateTimeField(auto_now=True)

    # To return our search with what was typed instead of an object, in our database
    def __str__(self):
        return '{}'.format(self.search)

    # To put search field plural in our database
    class Meta:
        verbose_name_plural = 'Searches'