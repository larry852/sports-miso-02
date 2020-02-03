from django.utils.formats import date_format


def datetime_format(datetime):
    return date_format(datetime, 'DATETIME_FORMAT')
