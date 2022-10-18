import datetime
from time import strftime

class DateFormat():
    @classmethod
    def dateFormatter(self, date):

        """Devuelve una fecha en formato día/mes/año"""

        return datetime.datetime.strftime(date, '%d/%m/%Y')