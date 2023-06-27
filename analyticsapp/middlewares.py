from .models import Analytics

class TrackIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
       # ip_address = request.META.get('REMOTE_ADDR')
        x_forw_for = request.META.get('HTTP_X_FORWARDED_F0R')
        if x_forw_for is not None:
            ip = x_forw_for.split(',')[0]
        else:
        #    print("the call is working")
            ip = request.META.get('REMOTE_ADDR')
            analytics = Analytics(ip=ip)
            analytics.save()
        # Save the IP address to the database
        response = self.get_response(request)
       # print("response returned")
        return response

