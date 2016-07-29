from django.conf import settings as base_settings
from storages.backends.s3boto import S3BotoStorage

class MediaStorage(S3BotoStorage):
    location = base_settings.MEDIAFILES_LOCATION
