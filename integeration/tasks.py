from config import celery_app

@celery_app.task(serializer='json')
def test_task():
    for i in range(100000):
        if i%100:
            print(i)

