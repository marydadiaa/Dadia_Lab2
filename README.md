<h1>Laboratory Activity 2: Working with HTTP actions and API parameters</h1><br>

<h3>Objectives: </h3><br>

- Identify and differentiate different ways to parameterize an API <br>
- Discuss HTTP methods and their uses based on best practices <br>
- Use the HTTP methods and parameters to create a simple CRUD simulation API <br>

<h3>Instructions: </h3><br>
1. Building on the sample code from the GitHub URL, revise the code to create a To-Do List API. <br>
2. Here are the specifics: <br>
On API run: <br>
task_db = [ <br>
{"task_id": 1, "task_title": "Laboratory Activity", "task_desc": "Create Lab Act 2", "is_finished": False} <br>
] <br>

<h3>Endpoints *: </h3><br>
GET /tasks/{task_id} <br>
POST /tasks <br>
PATCH /tasks/{task_id} <br>
DELETE /tasks/{task_id} <br>
<br>
* Return values should be appropriate to the endpoints created <br>
* For every endpoints created, it should contains {"status": "ok"} for successful transaction, and  <br>
* {"error": <any error message related to the endpoint>} if there are issues on the transaction <br>
* Please use all necessary validation on every data being entered in the API (null check, negative numbers, division by zero, etc.) 

<h3>Importance:</h3><br>
Understanding and using HTTP methods correctly allows you to design an API that adheres to REST principles, where different actions on resources
(like creating, reading, updating, deleting) map to the corresponding HTTP methods.
<br>
<h3>Steps:</h3> <br>
1. Installing dependencies like, ("pip install fastapi uvicorn pydantic"). <br>
2. Begin to run the API using, ("uvicorn main:app --reload"). <br>
3. Perform the GET, POST, PATCH, and DELETE. <br>
- GET http://127.0.0.1:8000/tasks/1 <br>
- POST http://127.0.0.1:8000/tasks <br>
- PATCH http://127.0.0.1:8000/tasks/1 <br>
- DELETE http://127.0.0.1:8000/tasks/1
