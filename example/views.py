# example/views.py
from django.http import HttpResponse
from supabase import create_client, Client
import os


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")


def index(request):
    supabase: Client = create_client(url, key)
    response = supabase.table('test').select("id", "name").execute()
    return HttpResponse(response.data, content_type='application/json')
