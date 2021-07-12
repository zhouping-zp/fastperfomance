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
        with self.client.request(method="GET", url="https://open-pre.shiguangkey.com/api/content/content/myContentList", headers=eval("{'terminaltype': '4', 'token': '1f45a60c06408c98e4a140bba543f8d0', 'content-type': 'application/json;charset=UTF-8'}"), data=eval("{'pageIndex': '1', 'pageSize': '10'}"),
                                 json=self.json, params=self.params, catch_response=True) as response:
            if "success" not in response.text:
                response.failure(response.text)