from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from firebase.firebase_connection import firebase_connect
from models.question import Question
import services.questions as question_db

app = FastAPI()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

category_collection = firebase_connect("categories")


@app.get("/")
def root():
    return {"message" : "Hello Word"}


@app.get("/id/{id}")
def get_by_id(id: int, query: Optional[str] = None):
    return {"id" : id, "query": query}


@app.get("/categories")
def get_gategories():
    collection = category_collection.get()
    categories = []
    
    for doc in collection:
        category = doc.to_dict()
        category["id"] = doc.id
        categories.append(category)
    
    return {"categories" :categories}


@app.get("/questions")
def get_questions():

    questions = question_db.get_questions()
    return questions


@app.get("/question/{id}")
def get_question_by_id(id: str):

    question = question_db.get_by_id(id)
    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Question with the id: {id}, was not found!")

    return {"question" : question}


@app.post("/question", status_code=status.HTTP_201_CREATED)
def create_question(question: Question):

    question = question_db.create(question)
    return {"Status_OK" : question}


@app.put("/question/{id}", status_code=status.HTTP_201_CREATED)
def update_question(question: Question, id):

    question = question_db.update(question, id)
    return {"Status_OK" : question}


@app.delete("/question/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_question(id):
    
    question_db.delete(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)