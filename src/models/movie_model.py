import datetime
from pydantic import BaseModel, Field, validator


class Movie(BaseModel):
    id: int
    title: str
    author: str
    year: int
    category: str

class MovieCreate(BaseModel):
    id: int
    title: str
    author: str = Field(min_length=3, max_length=30)
    year: int = Field(le=datetime.date.today().year, ge=1900)
    category: str = Field(min_length=3, max_length=20)

    model_config = {
        "json_schema_extra": {
            "example": {
                'id': 1,
                'title': 'my title',
                'author': 'John',
                'year': 2020,
                'category': 'action'
            }
        }
    }

    ## custom validations
    @validator('title')
    def validate_title(cls, value):
        if len(value) < 5:
            raise ValueError('Title field muts have a minimun lenght of 5 caharacters')
        if len(value) > 20:
            raise ValueError('Title field muts have a maximun lenght of 15 caharacters')
        return value

class MovieUpdate(BaseModel):
    title: str
    author: str
    year: int
    category: str