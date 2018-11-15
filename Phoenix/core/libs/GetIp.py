from django.template.context_processors import request


class GetIp(object):
    
    def get_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            Ip = x_forwarded_for.split(',')[-1].strip()
        else:
            Ip = request.META.get('REMOTE_ADDR')
        return Ip