from typing import List
from fastapi import FastAPI
from starlette.responses import FileResponse
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader


def _generate_template(filename):
    template_loader = FileSystemLoader(searchpath="./")
    template_env = Environment(loader=template_loader)
    template = template_env.get_template(filename)
    return template
    

items = [
    {
        "column_1": "Hello",
        "column_2": "World"
    },
    {
        "column_1": "Hello",
        "column_2": "World"
    }
]

name = "Parth"

template = _generate_template("pdf_template.html")

html_out = template.render(name=name,items=items)

html_byte_array = HTML(string=html_out).write_pdf()

app = FastAPI()

@app.get("/")
def get_pdf():

    return FileResponse(
        html_byte_array,
        media_type="application/pdf",
        filename="ticket.pdf"
    )
