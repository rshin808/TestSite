from datetime import datetime, timedelta
from .models import Temperature

class ChartData(object):
    @classmethod
    def get_tempF(cls):
        #tempFs = Temperature.tempF()
        tempFs = [10, 20, 30, 40]
        data = {'dates' : [],
                'values' : [],}
        
        count = 0
        for tempF in tempFs:
            data['dates'].append(str(count))
            data['values'].append(tempF)
            count += 1
        return data
