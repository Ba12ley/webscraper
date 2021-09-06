from celery import shared_task, task
from .scrapers import scrape

# @shared_task()
# def do_something_async(unscheduled):
#     print(unscheduled)
#
# @task
# def do_something_scheduled():
#     print("Scheduled task")

@task
def scrape_defib():
    URL = "https://www.opendatani.gov.uk/dataset?q=defib|AED|defibrilator"
    scrape(URL)
    return
