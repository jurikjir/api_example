# Description: Main test file for the FastAPI application.

from fastapi.testclient import TestClient
from fastapi import status

from ..app_custom_validations import app
from ..exception_message import (
    INVALID_ID_LENGTH_MSG,
    INVALID_QUESTION_MAX_LENGTH_MSG,
    INVALID_QUESTION_MIN_LENGTH_MSG
    )


# initialize FastAPI test client
client = TestClient(app)


def test_invalid_id_length():
    """
    Test that the API returns a 400 Bad Request response
    with a custom error message when the id length is invalid.
    """
    response = client.post(
        url="/question",
        json={
            "id": "",
            "question": "How are you?"
            }
        )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == INVALID_ID_LENGTH_MSG


def test_invalid_question_max_length():
    """
    Test that the API returns a 400 Bad Request response
    with a custom error message when the question max length is invalid.
    """
    response = client.post(
        url="/question",
        json={
            "id": "123456789",
            "question": "How are you? " * 100
            }
        )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == INVALID_QUESTION_MAX_LENGTH_MSG


def test_invalid_question_min_length():
    """
    Test that the API returns a 400 Bad Request response
    with a custom error message when the question min length is invalid.
    """
    response = client.post(
        url="/question",
        json={
            "id": "123456789",
            "question": ""
            }
        )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == INVALID_QUESTION_MIN_LENGTH_MSG


def test_answer_type():
    """
    Test that the API returns a 200 OK response
    for a valid answer type.
    """
    response = client.post(
        url="/question",
        json={
            "id": "123456789",
            "question": "How are you?"
            }
        )
    assert response.status_code == status.HTTP_200_OK
    assert type(response.json()["answer"]) == str


def test_answer_max_length():
    """
    Test that the API returns a 200 OK response
    for an answer with a length less than 1025.
    """
    MAX_TEARATIONS = 100
    for _ in range(MAX_TEARATIONS):
        response = client.post(
            url="/question",
            json={
                "id": "123456789",
                "question": "How are you?"
                }
            )
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()["answer"]) < 1025