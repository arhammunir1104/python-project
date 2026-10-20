# from fastapi import status
# from fastapi import FastAPI, HTTPException, Request
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel

# app = FastAPI()

# class User(BaseModel):
#     name : str
#     age : int
#     hobby  : str

# @app.get("/")
# def home():
#     return({"message": "Welcome to the Fast API"})

# @app.get("/user")
# def user():
#     return({"message" : ["Arham", "Munir","Azam"]})

# @app.get("/about")
# def about():
#     return({"message" : "Welcome to about page"})


# @app.get("/users/{user_id}")
# def get_user(user_id):
#     return({"Users", user_id})

# @app.get("/getname")
# def get_name(name):
#     return({"Names" : name})

# @app.get("/items")
# def get_items(name : str = None, price : float = 0):
#     return({
#         "Name" : name,
#         "Price" : price
#     })

# @app.post("/create-user")
# def create_user(user:dict):
#     return({
#         "message" : "User Created",
#         "data": user
#     })

# @app.post("/create-user2")
# def create_user(user:User):
#     return({
#         "message" : "User Created",
#         "data": user
#     })

# Todo Application 

# class Data(BaseModel) : 
#     id : int
#     title : str
#     completed : bool

# todo = []

# @app.post("/add")
# def add_list(data:Data):
#     todo.append(data)
#     return({"message" : "Data uploaded"})


# @app.get("/get")
# def get_list():
#     return todo

# @app.get("/get/id")
# def getById(id:int = None):
#     for item in todo:
#         if item.id == id:
#             return(item)

# @app.delete("/delete")
# def del_list(id:int = None):
#     for item in todo:
#         if(item.id == id):
#             todo.remove(item)
#             return({"message" : "Deleted",})

# @app.put("/update")
# def update_list(id:int = None, title:str = "", completed:bool = None):
#     for item in todo:
#         if(item.id == id):
#             item.title = title
#             item.completed = completed
#             return({
#                 "message" : "Updated",
#             })


# class UserNotFoundException(Exception):
#     def __init__(self, name : str):
#         self.name = name

# @app.exception_handler(UserNotFoundException)
# def user_not_found_handler(request : Request, exc : UserNotFoundException):
#     return JSONResponse(
#         status_code = 404,
#         content = {
#             "message" : f"User {exc.name} not found",
#         }
#     )

# @app.get("/user")
# def get_user(name : str):
#     if name == "Arham":
#         return {"message" : "User found"}
#     else:
#         raise UserNotFoundException(name)


# from fastapi import Depends, Header, HTTPException

# def verify_token(token:str = Header(None)):
#     if(token != "MyToken"):
#         raise HTTPException(
#             status_code = 401,
#             detail = "Invalid Token",
#         )
#     return({status : True, "user": "Authorize user", "token" : token})

# @app.get("/data")
# def sen_data(token = Depends(verify_token)):
#     print(token)
#     return({
#         "message" : "Data Found"
#         # "token" : token["token"]
#     })


# import sqlite3
# from fastapi import FastAPI

# app= FastAPI()

# conn = sqlite3.connect("test.db", check_same_thread=False)

# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY ,
#     title TEXT NOT NULL,
#     completed TEXT
# )
# """)

# conn.commit()


# @app.get("/")
# def home():
#     return({
#         "message" : "DB Connected Sucecssfully"
#     })



# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import sessionmaker, declarative_base, Session

# from fastapi import FastAPI, Depends

# app = FastAPI()

# DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args = {"check_same_thread" : False}
# )

# sessionLocal = sessionmaker(bind = engine)

# Base = declarative_base()

# class Todo(Base) : 
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index = True)
#     title = Column(String(255))
#     completed = Column(String)


# Base.metadata.create_all(bind=engine)

# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/")
# def home(db : Session = Depends(get_db)):
#     return({"message" : "DB Connected Successfully"})


# from fastapi import FastAPI, HTTPException, Depends, Header
# from jose import jwt
# from datetime import datetime, timedelta, timezone


# app = FastAPI()

# SECRET_KEY = "MySecretKey"
# ALGORITHM = "HS256"


# def create_token(data: dict):
#     to_encode = data.copy() 
#     expire = datetime.now(timezone.utc) + timedelta(minutes=30)
#     to_encode.update({"exp" : expire})

#     token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return token

# # Login 
# @app.post("/login")
# def login(username:str, password:str):
#     if(username != "Arham" or password != "123"):
#         raise HTTPException(status_code=401, detail="Invalid username or password")
    
#     token = create_token({"user_name" : username})

#     return({"access_token" : token, "token_type" : "bearer"})

# #Verify Token

# def verify_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
#         return payload
#     except:
#         raise HTTPException(status_code=401, detail="Invalid username or password")


# # Admin Data 
# @app.get("/data")
# def send_data(user = Depends(verify_token)):

#     return({"message": "Secure Data Accessed", "user" : user})





# from fastapi import FastAPI, HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import jwt
# from datetime import datetime, timedelta, timezone
# from passlib.context import CryptContext


# app = FastAPI()

# SECRET_KEY = "MySecretKey"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTE = 30


# # PASSWORD HASHING  
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

# # DUMMY USER DB 
# fake_user_db={
#     'admin' : {
#         "username" : "admin",
#         "hashed_password" : pwd_context.hash("1234")
#     }
# }

# #HASH PASSWORD 
# def hash_password(password: str):
#     return pwd_context.hash(password)


# # VERIFY PASSWORD 
# def verify_password(plain_password, hash_password):
#     return pwd_context.verify(plain_password, hash_password)

# def create_token(data: dict):
#     to_encode = data.copy() 
#     expire = datetime.now(timezone.utc) + timedelta(minutes=30)
#     to_encode.update({"exp" : expire})

#     token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return token

# # Login 
# @app.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = fake_user_db.get(form_data.username)

#     if not user or not verify_password(form_data.password, user["hashed_password"]):
#         raise HTTPException(status_code=400, detail="Invalid username or password")

    
#     access_token = create_token({"sub" : form_data.username})

#     return({"access_token" : access_token, "token_type" : "bearer"})



# #Verify Token

# def verify_token(token: str = Depends(oauth2_schema)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
#         username = payload.get("sub")

#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid username")

#         return username
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")


# # Admin Data 
# @app.get("/data")
# def send_data(username = Depends(verify_token)):

#     return({"message": "Secure Data Accessed", "user" : username})


# FILES HANDLING 

# from fastapi import FastAPI, HTTPException, File, UploadFile
# import os
# import shutil
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# UPLOAD_DIR = "uploads"
# if not os.path.exists(UPLOAD_DIR):
#     os.makedirs(UPLOAD_DIR)

# # STATIC FILE SETUP 
# app.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


# # UPLOAD FILE PATH 
# @app.post("/upload")
# def upload(file : UploadFile= File(...)):
#     filename = file.filename
#     file_path = os.path.join(UPLOAD_DIR, filename)

#     if not filename:
#         raise HTTPException(status_code = 400, detail = "No file was uploaded")
    
#     with open(file_path, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     return({"message" : "File uploaded successfully", "filename" : filename, "file_url" : f"http://127.0.0.1:8000/files/{filename}"})


# # GET FILE URL API : 
# @app.get("/file/{filename}")
# def getFileName(filename : str):
#     file_path = os.path.join(UPLOAD_DIR,filename)

#     if not os.path.exists(file_path):
#         raise HTTPException(status_code = 400, detail="File don't eists")
    
#     return({"file_url" : f"http://127.0.0.1:8000/files/{filename}"})





# CORS SETUP 
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware


# app = FastAPI()

# # CORS SETUP 
# origins = [
#     "http://localhost:5173"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"]
# )


# # ENV SETUP
# import os
# from dotenv import load_dotenv

# load_dotenv()

# print(os.getenv("SECRET_KEY"))




# RATE LIMITING

from fastapi import Request
from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app = FastAPI()

# Limiter Setup 
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Error Handler 

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request : Request, exc : RateLimitExceeded):
    return JSONResponse(
        status_code= 429,
        content = {
            "detail" : "Too many Requests"
        }
    )


@app.get("/")
def home():
    return({"message" : "API Running properly"})


# Rate Limiter API 
@app.get("/data")
@limiter.limit("5/minute")
def getData(request : Request):

    return({"message" : "Fetched data successfully"})
