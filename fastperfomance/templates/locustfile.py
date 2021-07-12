import random

from locust import HttpUser, task, constant

class WebsiteTasks(HttpUser):
    wait_time = constant(0)
    host = ''

    url = None
    method = None
    params = None
    data = None
    headers = None
    assertstr = None
    json = None
    cookie = None

    @task
    def test_single(self):
        with self.client.request(method=self.method, url=self.url, headers=eval(self.headers), data=eval(self.data),
                                 json=self.json, params=self.params, catch_response=True) as response:
            if "success" not in response.text:
                response.failure(response.text)