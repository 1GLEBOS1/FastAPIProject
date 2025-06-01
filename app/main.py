from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi import FastAPI, File, UploadFile
from make import make
app = FastAPI()


@app.get("/")
async def root():
    #
    return HTMLResponse(content=open("templates/index.html", "r").read(), status_code=200)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/uploadfile/")
async def create_file(files: list[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        with open(f"../files/{file.filename}", "wb") as f:
            f.write(contents)
            f.close()
    return RedirectResponse(url="/download", status_code=303)

@app.get("/download")
async def make_report(name: str = "User"):
    make()
    try:
        f = open("../files/report.pdf", "r")
        f.close()
        return HTMLResponse(content=open("templates/download_reports.html", "r").read(), status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content=open("templates/error.html", "r").read(), status_code=200)
@app.get("/download/docx")
async def download_report():
    return FileResponse("../files/report.docx", media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document", filename="report.docx")

@app.get("/download/pdf")
async def download_extra():
    return FileResponse("../files/report.pdf", media_type="application/pdf", filename="report.pdf")
