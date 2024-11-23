from locust import HttpUser, between, task


class LoadTesting(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_health_endpoint(self):
        self.client.get("/api/health")

    @task
    def test_feedback_submission(self):
        self.client.post(
            "/submit-feedback",
            {
                "model-response": "Example response to rate",
                "rating": "5",
                "comments": "Great response!",
            },
        )
