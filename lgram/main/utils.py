# utils.py
from .models import ContentView

def log_content_view(request, content_type, object_id):
    ip = request.META.get('REMOTE_ADDR', '')
    ContentView.objects.create(
        content_type=content_type,
        object_id=object_id,
        ip_address=ip
    )
