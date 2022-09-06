import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def code_generator(chars = string.ascii_lowercase + string.digits + string.ascii_uppercase):
    size = SHORTCODE_MIN
    return "".join(random.choice(chars) for _ in range(size))

def create_shortcode(instance):
    new_code = code_generator()
    parent_class = instance.__class__
    code_exist = parent_class.objects.filter(shortcode=new_code).exists()
    if code_exist:
        return create_shortcode()
    return new_code