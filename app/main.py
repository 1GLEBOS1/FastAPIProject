from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi import FastAPI, File, UploadFile, Form, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
from file_processing import make
from crud.users import create_user, authenticate_user, get_user_by_email, Users
from db import get_db
from sqlalchemy.orm import Session
from security import create_access_token, oauth2_scheme, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import JWTError, jwt
from security import SECRET_KEY, ALGORITHM
from pip._vendor.urllib3 import HTTPResponse
app = FastAPI()

dir_names = []

#async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#    credentials_exception = HTTPException(
#        status_code=status.HTTP_401_UNAUTHORIZED,
#        detail="Could not validate credentials",
#        headers={"WWW-Authenticate": "Bearer"},
#    )
#    try:
#        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#        email: str = payload.get("sub")
#        if email is None:
#            raise credentials_exception
#    except JWTError:
#        raise credentials_exception
#    user = get_user_by_email(db, email=email)
#    if user is None:
#        raise credentials_exception
#    return user

@app.get("/")
async def root():
    return HTMLResponse(content=open("templates/index.html", "r").read(), status_code=200)


#    @app.get("/login")
#    async def login_page():
#        return HTMLResponse(content=open("app/templates/login.html", "r").read(), status_code=200)

#    @app.post("/login/")
#    async def login(
#        email: str = Form(...),
#        password: str = Form(...),
#        db: Session = Depends(get_db)
#    ):
#        user = authenticate_user(db, email, password)
#        if not user:
#            raise HTTPException(
#                status_code=status.HTTP_401_UNAUTHORIZED,
#                detail="Incorrect email or password",
#                headers={"WWW-Authenticate": "Bearer"},
#            )
#        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#        access_token = create_access_token(
#            data={"sub": user.email}, expires_delta=access_token_expires
#        )
#        response = RedirectResponse(url="/", status_code=303)
#        response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
#        return response

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/signup")
async def signup():
    return HTMLResponse(content=open("templates/signup.html", "r").read(), status_code=200)

@app.post("/signup_user/")
async def signup_usersignup_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db:Session = Depends(get_db)
):
    try:
        user = create_user(db, name, email, password)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
        return response
    except Exception as e:
        print(e)
        return HTMLResponse(content=open("templates/error.html", "r").read(), status_code=200)


#@app.get("/protected-route")
#async def protected_route(current_user: Users = Depends(get_current_user)):
#    return {"message": f"Hello {current_user.name}, this is a protected route"}

@app.post("/uploadfile/")
async def create_file(files: list[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        with open(f"../files/downloads/{file.filename}", "wb") as f:
            f.write(contents)
            f.close()
    dir_name = make()
    dir_names.append(dir_name)
    print(dir_name)
    return RedirectResponse(url="/download", status_code=303)

@app.get("/download")
async def make_report(name: str = "User"):

    try:
        f = open(f"../files/downloads/{dir_names[-1]}/report.pdf", "r")
        f.close()
        return HTMLResponse(content=open("templates/download_reports.html", "r").read(), status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content=open("templates/error.html", "r").read(), status_code=200)

@app.get("/download/docx")
async def download_report():
    return FileResponse(f"../files/downloads/{dir_names[-1]}/report.docx", media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename="report.docx")

@app.get("/download/pdf")
async def download_extra():
    return FileResponse(f"../files/downloads/{dir_names[-1]}/report.pdf", media_type="application/pdf", filename="report.pdf")
