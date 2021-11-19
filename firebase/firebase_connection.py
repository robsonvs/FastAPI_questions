import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebase/firestorekey.json")
firebase_admin.initialize_app(cred)

def firebase_connect(collection):
    try:
        firebase = firestore.client()
        return firebase.collection(collection)
    except Exception as ex:
        print(ex)