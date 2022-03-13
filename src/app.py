from typing import List
from fastapi import FastAPI
from starlette.responses import StreamingResponse
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import io


def generate_template(filename):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(filename)
    return template


items = [{"column_1": "Hello", "column_2": "World"}, {"column_1": "Hello", "column_2": "World"}]

name = "Parth"

template = generate_template("pdf_template.html")

html_out = template.render(name=name, items=items)

html_byte_array = HTML(string=html_out).write_pdf()

app = FastAPI()


@app.get("/")
async def get_pdf():
    return StreamingResponse(
        io.BytesIO(html_byte_array),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment;filename=export.pdf"},
    )
