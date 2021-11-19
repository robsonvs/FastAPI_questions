from firebase.firebase_connection import firebase_connect
from models.question import Question
from datetime import datetime


question_ref = firebase_connect("questions")


def get_questions():
    
    #collection = question_ref.order_by("created").get()
    collection = question_ref.get()
    questions = []
    
    for doc in collection:
        question: Question = doc.to_dict()
        question["id"] = doc.id
        questions.append(question)
    
    return questions


def get_by_id(id):
    
    question: Question = question_ref.document(id).get().to_dict()
    if question:
        question["id"] = id
    
    return question


def create(question: Question):

    question.created = datetime.now()
    question_ref.add(question.dict())
    return question


def update(question: Question, id):

    question.updated = datetime.now()
    question_ref.document(id).update(question.dict())
    return question


def delete(id):

    question = question_ref.document(id).delete()
    return question