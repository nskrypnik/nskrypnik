from status.models import Status

def status(request):
    status = Status.objects.all().order_by('-date_added')[0]
    return {'status': status}
