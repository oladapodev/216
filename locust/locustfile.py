from locust import HttpUser, task, between

class ConsolidatedUser(HttpUser):
    wait_time = between(0.1, 0.5)
    
    @task(1)
    def create_item(self):
        self.client.post("/items/", json={"name": "test item"})
        
    @task(1)
    def create_user(self):
        self.client.post("/users/", json={"name": "test user"})

class GranularUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task(1)
    def create_item(self):
        # Note: In a real scenario, these might be behind a gateway.
        # Here we hit the services directly using their docker-compose service names.
        self.client.post("http://service_1:8000/items/", json={"name": "test item"})
        
    @task(1)
    def create_user(self):
        self.client.post("http://service_2:8000/users/", json={"name": "test user"})
