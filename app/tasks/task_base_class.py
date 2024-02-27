import celery


class BaseTaskWithRetry(celery.Task):
    autoretry_for = (Exception, KeyError)
    retry_kwargs = {"max_retries": 7, "countdown": 5}
    retry_backoff = True
    soft_time_limit = 60
    time_limit = 180
