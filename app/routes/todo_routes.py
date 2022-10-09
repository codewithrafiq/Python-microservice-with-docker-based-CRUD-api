from typing import List
from fastapi import APIRouter
from app.models.Todo import Todo, Todo_Pydantic, TodoIn_Pydantic, Status
from fastapi.responses import HTMLResponse


route = APIRouter(tags=["Routes"])


@route.get("/", response_class=HTMLResponse)
def SwaggerUi():
    return """
    <html>
        <head>
            <title>Home page</title>
        </head>
        <body>
            <h1><a href="/docs">Go Swagger Ui and Test All APIs.</a></h1>
        </body>
    </html>
    """


@route.get("/get-todos", response_model=List[Todo_Pydantic])
async def getTodos():
    return await Todo_Pydantic.from_queryset(Todo.all())


@route.get("/get-single-todo/{id}")
async def getSingleTodo(id: int):
    return await Todo_Pydantic.from_tortoise_orm(await Todo.get(id=id))


@route.post("/add-todo")
async def addTodo(todo: TodoIn_Pydantic):
    todo_obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(todo_obj)


@route.put("/update-todo/{id}", response_model=Todo_Pydantic)
async def Update_Article(id: int, todo: TodoIn_Pydantic):
    await Todo.filter(id=id).update(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(await Todo.get(id=id))


@route.delete("/delete-todo/{id}", response_model=Status)
async def Delete_Article(id: int):
    article_obj = await Todo.get(id=id)
    await article_obj.delete()
    return {"message": f"Todo {id} deleted"}
