from django.db import models

class Zaman(models.Model):
    zaman = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u"%s" % self.zaman