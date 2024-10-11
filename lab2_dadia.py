from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

task_db = [
    {"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False}
]

class Task(BaseModel):
    task_title: str
    task_desc: str
    is_finished: Optional[bool] = False

@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    task = next((task for task in task_db if task["task_id"] == task_id), None)
    if task:
        return {"status": "ok", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
async def create_task(task: Task):
    if not task.task_title or not task.task_desc:
        raise HTTPException(status_code=400, detail="Title and description cannot be null.")
    
    new_task_id = len(task_db) + 1
    new_task = {
        "task_id": new_task_id,
        "task_title": task.task_title,
        "task_desc": task.task_desc,
        "is_finished": task.is_finished
    }
    task_db.append(new_task)
    return {"status": "ok", "task": new_task}

@app.patch("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    task_to_update = next((task_item for task_item in task_db if task_item["task_id"] == task_id), None)
    if not task_to_update:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task.task_title:
        task_to_update["task_title"] = task.task_title
    if task.task_desc:
        task_to_update["task_desc"] = task.task_desc
    if task.is_finished is not None:
        task_to_update["is_finished"] = task.is_finished
    
    return {"status": "ok", "task": task_to_update}

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task_index = next((index for index, task in enumerate(task_db) if task["task_id"] == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task_db.pop(task_index)
    return {"status": "ok", "message": "Task deleted successfully"}
