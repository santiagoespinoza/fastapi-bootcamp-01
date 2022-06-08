from email.policy import HTTP
from fastapi import FastAPI, Depends, HTTPException
from .auth import AuthHandler
from .schemas import AuthDetails

app = FastAPI()

auth_handler = AuthHandler()
users = []

@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    # We check if user already exists
    if any(x['username']==auth_details.username for x in users):
        # If so we raise exception
        raise HTTPException(status_code='400', detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username':auth_details.username,
        'password':hashed_password
    })
    return

@app.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in user:
        if x['username']==auth_details.username:
            user=x
            break
    
    if (user in None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail="Invalid Username and/or password")
    
    token =  auth_handler.encode_token(user['username'])
    return {'token':token}

@app.get('/unprotected')
def unprotected():
    return {'hello':'world'}

@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return {'name':username}