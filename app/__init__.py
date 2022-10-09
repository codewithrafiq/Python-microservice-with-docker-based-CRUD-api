from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI() 



register_tortoise(
    app,
    db_url="sqlite://db.db",
    modules={"models": ["app.models.Todo"]},
    generate_schemas=True,
    add_exception_handlers=True,
)



from app.routes.todo_routes import route


app.include_router(route)