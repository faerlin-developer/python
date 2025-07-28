from pydantic import BaseModel


class TaskRequest(BaseModel):
	body: str


class TaskResponse(TaskRequest):
	id: int
