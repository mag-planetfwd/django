# example/views.py
from django.http import HttpResponse
from supabase import create_client, Client


def index(request):
    supabase: Client = create_client('https://ymslwfbwjehfifxturei.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inltc2x3ZmJ3amVoZmlmeHR1cmVpIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODAzMDQxOTMsImV4cCI6MTk5NTg4MDE5M30.Xwlun_ySomyoKIF1HgCzHal1tr09e6WsvNY6IQEzTB4')
    response = supabase.table('test').select("id", "name").execute()
    return HttpResponse(response.data, content_type='application/json')
