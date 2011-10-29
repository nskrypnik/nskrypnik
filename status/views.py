from django.http import HttpResponse
from status.models import Status
from datetime import datetime

def change(request):
    text = request.POST['text']
    if text:
        Status(text=text, date_added=datetime.now()).save()
    else:
        text = Status.objects.all().order_by('-date_added')[0].text
    return HttpResponse(text)
