from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from .answers import generate_answer
from .request_validators import (
    valid_id_length,
    valid_question_max_length,
    valid_question_min_length
    )
from .exception_message import (
    INVALID_ID_LENGTH_MSG,
    INVALID_QUESTION_MAX_LENGTH_MSG,
    INVALID_QUESTION_MIN_LENGTH_MSG
    )


# initialize FastAPI app
app = FastAPI()

# Define pydantic model
class Payload(BaseModel):
    """
    A Pydantic model that contains the id and question.
    
        Attributes:
            id (str): a unique identifier
            question (str): a question
    """
    id: str
    question: str


@app.post("/question")
async def root(payload: Payload) -> dict:
    """
    A function that generates an answer to a question.

        Parameters:
            payload (Payload): a Pydantic model that contains the id and question

        Returns:
            dict: a dictionary that contains the answer
    """
    # Check if the id length is valid
    if not valid_id_length(id=payload.id):
        # If not, return an HTTP 400 Bad Request response
        # and custom error message
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_ID_LENGTH_MSG
            )

    # Check if the question max length is valid
    if not valid_question_max_length(question=payload.question):
        # If not, return an HTTP 400 Bad Request response
        # and custom error message
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_QUESTION_MAX_LENGTH_MSG
            )

    # Check if the question min length is valid
    if not valid_question_min_length(question=payload.question):
        # If not, return an HTTP 400 Bad Request response
        # and custom error message
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=INVALID_QUESTION_MIN_LENGTH_MSG
            )

    # If all checks pass, generate and return the answer
    answer = generate_answer()
    return JSONResponse(content={"answer": answer})

