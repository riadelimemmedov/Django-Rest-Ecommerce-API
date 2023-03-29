#!Python modules
import uuid

# Django modules and function
from django.utils.text import slugify


#!random_code
def random_code() -> str:
    generated_number = str(uuid.uuid4())[:12].replace("-", "").upper()
    return generated_number


#!returnFlugFormats
def returnFlugFormat(title):
    return slugify(title)
