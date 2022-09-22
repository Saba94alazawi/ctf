from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import IPcheck



def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(IPcheck, 'interval', seconds=120)
    scheduler.start()