import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/api/integrate?lower=0&upper=3.141597")
