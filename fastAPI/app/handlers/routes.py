import structlog
from databases import Database
from fastapi import APIRouter, Request, Depends
from fastapi import HTTPException

from db.database import get_database
from db.tables import tasks
from payload.task import TaskRequest, TaskResponse

router = APIRouter()

log = structlog.get_logger()


@router.post("/task", response_model=TaskResponse, status_code=201)
async def post_task(request: Request, task: TaskRequest, db: Database = Depends(get_database)):
	"""Post a task"""

	log.info("POST /task", body=task.body, request_id=request.state.request_id)
	
	query = tasks.insert().values(body=task.body)
	task_id = await db.execute(query)

	return {"id": task_id, "body": task.body}


@router.get("/task/{task_id}", response_model=TaskResponse, status_code=200)
async def post_task(request: Request, task_id: int, db: Database = Depends(get_database)):
	"""Get specified task"""

	log.info(f"GET /task/{task_id}", request_id=request.state.request_id)

	query = tasks.select().where(tasks.c.id == task_id)
	task = await db.fetch_one(query)

	if task is None:
		raise HTTPException(status_code=409, detail="task does not exists")

	return {"id": task.id, "body": task.body}
