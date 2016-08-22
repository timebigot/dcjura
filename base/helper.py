from base.models import Coupon
import string
import random
import os
import urllib.request
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def url_coder(size=7, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    url_code = ''.join(random.choice(chars) for _ in range(size))
    while True:
        try:
            i = Coupon.objects.get(url_code=url_code)
        except Coupon.DoesNotExist:
            return url_code
        else:
            continue

def thumb_maker(url):
    image = urllib.request.urlopen(url)
    img_ext = os.path.splitext(url)[1].lower()
    img_filename = url_coder(11) + img_ext
    img_path = os.path.join('test' + img_filename)
    default_storage.save(img_path, ContentFile(image.read()))

    """
    thumb = Image.open(img_db.img_item)
    W = thumb.size[0] / 2
    H = thumb.size[1] / 2

    if W > H:
        thumb = thumb.crop((W-H, H-H, W+H, H+H))
        thumb = thumb.resize((350,350))
    elif W < H:
        thumb = thumb.crop((W-W, H-W, W+W, H+W))
        thumb = thumb.resize((350,350))

    thumb_path = 'thumb_' + img_filename
    f_thumb = default_storage.open(thumb_path, 'w')
    thumb.save(f_thumb, 'png')
    f_thumb.close()
    """
