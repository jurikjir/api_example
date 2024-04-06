from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from .answers import generate_answer


app = FastAPI()

class Payload(BaseModel):
    """
    A Pydantic model that contains the id and question.
    
        Attributes:
            id (str): a unique identifier of length greater than 0
            question (str): a question of length between 1 and 512
    """
    id: str = Field(
        title="ID",
        description="A unique identifier",
        min_length=1
        )
    question: str = Field(
        title="Question",
        description="A question",
        min_length=1,
        max_length=512
        )

@app.post("/question")
async def root(payload: Payload) -> dict:
    """
    A function that generates an answer to a question.
        Parameters:
            payload (Payload): a Pydantic model that contains the id and question

        Returns:
            dict: a dictionary that contains the answer
    """
    answer = generate_answer()
    return JSONResponse(content={"answer": answer})

