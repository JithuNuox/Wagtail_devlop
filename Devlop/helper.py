
from .constants import IND_TIMEZONE

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo

def local_timezone(request,date,format,timezone=None):
    if timezone:
        local_timezone = zoneinfo.ZoneInfo(timezone)
    else:
        local_timezone = zoneinfo.ZoneInfo(request.META.get('HTTP_TIMEZONE', IND_TIMEZONE)) 
    converted_date = date.astimezone(local_timezone)
    return converted_date.strftime(format)