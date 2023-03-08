# python-jwt-auth
implementation of JWT bearer token in python using fastapi 
I have used fast api with JWT authentication.
## install all dependencies in requirements.txt file using pip cmd and run app under src folder.
```uvicorn main:app --host localhost --port 8000 --reload```

## Natigate to http://localhost:8000/docs url.
## Use below endpoint to generate token
```http://localhost:8000/users/token```
### use below credentials 
 Username:johndoe  
 Password: secret   
 
### now navigate to below url and pass the bearer token to access this end point.
```http://localhost:8000/users/me/```
