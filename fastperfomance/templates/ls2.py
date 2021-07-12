import random

from locust import HttpUser, task, constant

class WebsiteTasks(HttpUser):
    wait_time = constant(0)
    host = ''

    url = "https://open-pre.shiguangkey.com/api/content/content/myContentList"
    method = "GET"
    params = None
    data = "{'pageIndex': '1', 'pageSize': '10'}"
    headers = "{'terminaltype': '4', 'token': '0x779dab06a0a5db1bc24b63931e2034', 'content-type': 'application/json;charset=UTF-8'}"
    assertstr = None
    json = None
    cookie = None


    @task
    def test_single(self):
        with self.client.request(method=self.method,url=self.url,headers=eval(self.headers),data=eval(self.data), json=self.json,params = self.params,catch_response=True) as response:
            if "success" not in response.text:
                response.failure(response.text)
