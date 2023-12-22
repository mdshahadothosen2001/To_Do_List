# To_Do_List

This project is made to manage the daily tasks.

Tech stack: Python, Django, Docker.


## Local development installation
1. At first pull the repository.


2. Create a virtual environment then activate it.

```bash
py -m venv venv
```
```bash
venv/Scripts/activate.bate
```

3. Install the required packages.

```bash
pip install -r backend/requirements/development.txt
```


4. Run docker containers:

```bash
docker-compose up --build
```

click here [URL](http://localhost:8000/)  for check this project working or not
If you see home interface then it is working.

## Access APIs

## For user account:
1. http://localhost:8000/user/register/ api hit for user account register.
2. http://localhost:8000/user/login/ api hit for user login.

## For Task application:
3. http://localhost:8000/task/ api hit for see task list.
4. http://localhost:8000/task/1/ api hit for see task detail.
5. http://localhost:8000/task/create/ api hit for create a new task.
6. http://localhost:8000/task/update/1/ api hit for modify particular task.
7. http://localhost:8000/task/delete/1/ api hit for task delete.

## For Study Plan application:
9. http://localhost:8000/study-plan/ api hit for study plans list.
10. http://localhost:8000/study-plan/create/ api hit for make new study plan.
11. http://localhost:8000/study-plan/delete/ api hit for delete specific study plan.

## For Note
12. http://localhost:8000/note/ api hit for list of note.
13. http://localhost:8000/note/create/ api hit for make note.
14. http://localhost:8000/note/update/1/ api hit for modify the note.
15. http://localhost:8000/note/detail/1/ api hit for detail of note.
16. http://localhost:8000/note/delete/1/ api hit for delete the note.

## For user logout:
17. http://localhost:8000/user/logout/ api hit for user logout.
