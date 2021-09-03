from celery import shared_task, task

@shared_task()
def do_something_async(unscheduled):
    print(unscheduled)

@task
def do_something_scheduled():
    print("Scheduled task")
