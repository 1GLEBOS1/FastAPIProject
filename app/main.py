from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi import FastAPI, File, UploadFile, Form, Depends
from file_processing import make
from crud.users import create_user
from db import get_db
from sqlalchemy.orm import Session
app = FastAPI()

dir_names = []

@app.get("/")
async def root():
    return HTMLResponse(content=open("templates/index.html", "r").read(), status_code=200)

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
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        print(e)
        return HTMLResponse(content=open("templates/error.html", "r").read(), status_code=200)

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
