from operator import index
from time import sleep

from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi import FastAPI, File, UploadFile
from make import make
app = FastAPI()


@app.get("/")
async def root():

    return HTMLResponse(content=open("index.html", "r").read(), status_code=200)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/uploadfile/")
async def create_file(file: UploadFile = File()):
    contents = await file.read()
    with open(f"files/{file.filename}", "wb") as f:
        f.write(contents)
    return RedirectResponse(url="/makepdfreport", status_code=303)

@app.get("/makepdfreport")
async def make_report(name: str = "User"):

    make()

    sleep(30)
    return FileResponse("files/report.docx", media_type="application/docx", filename="report.docx")
