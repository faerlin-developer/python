import httpx

BASE_URL = "http://localhost:8000"


def test_end_to_end():
	payload = {"body": "This is the payload body"}

	# POST /task
	response = None
	with httpx.Client() as client:
		response = client.post(f"{BASE_URL}/task", json=payload)

	data = response.json()
	assert response.status_code == 201
	assert "id" in data
	task_id = data["id"]

	# GET /task
	response = None
	with httpx.Client() as client:
		response = client.get(f"{BASE_URL}/task/{task_id}")

	data = response.json()
	assert response.status_code == 200
	assert data["id"] == task_id
