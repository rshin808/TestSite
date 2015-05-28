from django.db import models
from django.utils.encoding import smart_unicode
import time

class Temperature(models.Model):
    timestamp =  models.DateTimeField(auto_now_add = True, auto_now = False)
    value = models.DecimalField(max_digits = 7, decimal_places = 3)    
    
    def __unicode__(self):
        return smart_unicode(self.timestamp)

    def get_tempF(self):
        return self.value

    def get_tempC(self):
        return float("%.3f" % ((float(self.value) - 32.0) * 5.0 / 9.0))

    def get_tempK(self):
        return float("%.3f" % ((float(self.value) + 459.67) * 5.0 / 9.0))

    def get_epoch(self):
        return int(time.mktime(self.timestamp.timetuple()) * 1000)
