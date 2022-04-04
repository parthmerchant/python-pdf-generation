from weasyprint import HTML
from jinja2 import FileSystemLoader, Environment
from typing import Any

items = [
    {"column_1": "Hello", "column_2": "World"},
    {"column_1": "Hello", "column_2": "World"},
    {"column_1": "Hello", "column_2": "World"},
    {"column_1": "Hello", "column_2": "World"},
    {"column_1": "Hello", "column_2": "World"},
    {"column_1": "Hello", "column_2": "World"},
]

# Const name
name = 'Parth'

def _generate_template(filename):
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(filename)
    return template

def generate_pdf(template_filepath: str):
        template = _generate_template(template_filepath)
        html_out = template.render(name=name, items=items)
        html_byte_array = HTML(string=html_out).write_pdf(stylesheets=["pdf.css"])
        return html_byte_array
