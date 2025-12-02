from celery import shared_task
from .models import Institute
import time

@shared_task
def process_form_submission(institute_id):
    # simulate heavy work (e.g., sending email, analytics)
    time.sleep(5)
    institute = Institute.objects.get(id=institute_id)
    print(f'Processed form for Institute ID: {institute.id}')
