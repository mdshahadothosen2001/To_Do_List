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

click here [URL](http://localhost:8000/task/)  for check this project working or not
If you see login interface then it is working.

## Access token and authentication

1. http://localhost:8000/user/register/ api hit for user account register.
2. http://localhost:8000/user/login/ api hit for user login.
3. http://localhost:8000/task/ api hit for see task list.
4. http://localhost:8000/task/1/ api hit for see task detail.
5. http://localhost:8000/task/create/ api hit for create a new task.
6. http://localhost:8000/task/update/1/ api hit for modify particular task.
7. http://localhost:8000/task/delete/1/ api hit for task delete.
9. http://localhost:8000/user/logout/ api hit for user logout.