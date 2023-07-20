from .models import Analytics


class TrackIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        response = self.get_response(request)
        return response
