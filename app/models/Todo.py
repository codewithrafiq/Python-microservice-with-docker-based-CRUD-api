from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel


class Todo(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)


Todo_Pydantic = pydantic_model_creator(Todo, name='Todo')
TodoIn_Pydantic = pydantic_model_creator(
    Todo, name='TodoIn', exclude_readonly=True)


class Status(BaseModel):
    message: str
