from typing import Optional, Tuple
import requests
import shutil
from os import listdir, path, remove, makedirs

from celery import Celery
from celery.exceptions import SoftTimeLimitExceeded
from celery.utils.log import get_task_logger

from config import settings

makedirs('downloads/', exist_ok=True)

download_path = 'downloads/'
downloaded_files = set(listdir(download_path))

app = Celery('downloads', 
             broker=settings.broker)

logger = get_task_logger(__name__)

@app.task(soft_time_limit=90, task_time_limit=95, max_retries=10)
def save_file(url: str, filename: str) -> Tuple[bool, str]:

    if filename in downloaded_files:
        logger.info(f'Already downloaded file: {filename}, skipping.')
        return (False, filename)
    
    try:
        with requests.get(url, stream=True) as r:
            with open(path.join(download_path, filename), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
    except SoftTimeLimitExceeded:
        remove(path.join(download_path, filename))

    return (True, filename)
