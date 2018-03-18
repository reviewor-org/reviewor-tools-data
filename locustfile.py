from locust import HttpLocust, TaskSet, task

class WPTestTaskSet(TaskSet):
    @task
    def index(self):
        self.client.get("/")

#    @task
#    def page_with_comments(self):
#        self.client.get("/?page_id=155")

class WPLocust(HttpLocust):
    task_set = WPTestTaskSet
    min_wait = 5000
    max_wait = 15000
