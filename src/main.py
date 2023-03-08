from fastapi import FastAPI
from routes import user
app = FastAPI(title='fast apis demo',version='0.0.1',description='this is demo apis using fast api.')
app.include_router(user.router)
@app.get('/',tags=['Home'])
def home():
    return "{'data':'this is default route'}"
