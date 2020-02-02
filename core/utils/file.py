import os
from uuid import uuid4
from datetime import date


def get_path_class(instance, filename):
    extension = os.path.splitext(filename)[1][1:]
    class_directory = instance.__class__.__name__
    path = os.path.join(class_directory)
    filename = '{}.{}'.format(date.today().strftime("%Y-%m-%d") + "_" + uuid4().hex, extension)
    return os.path.join(path, filename)
