from rest_framework.pagination import LimitOffsetPagination

class VideoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 50
