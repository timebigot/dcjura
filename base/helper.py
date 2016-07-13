import string
import random
def url_coder(size=7, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    url_code = ''.join(random.choice(chars) for _ in range(size))
    return url_code
    """
    while True:
        try:
            i = Coupon.objects.get(url_code=url_code)
        except Coupon.DoesNotExist:
            return url_code
        else:
            continue
    """
