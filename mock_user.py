from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    host = "http://192.168.128.157:8080/"
    wait_time = between(2, 5)
    
    def on_start(self):
        self.client.get("/")
    
    @task(100)
    def index(self):
        self.client.get("/")

    # write a task for download endpoint
    @task(100)
    def download(self):
        self.client.post("/download", data={"download-code": "T6L9V4"})
