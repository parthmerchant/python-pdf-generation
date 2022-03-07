import jinja2
import pdfkit

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

def render_html():
    """
    Render html page using jinja based on layout.html
    """
    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template_file = "pdf_template.html"
    template = template_env.get_template(template_file)
    output_text = template.render(
        name=name,
        items=items
        )

    html_path = "./name.html"
    html_file = open(html_path, 'w')
    html_file.write(output_text)
    html_file.close()
    print("Now converting to pdf")
    pdf_path = "./Parth.pdf"    
    html2pdf(html_path, pdf_path)   

def html2pdf(html_path, pdf_path):
    """
    Convert html to pdf using pdfkit which is a wrapper of wkhtmltopdf
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.35in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    with open(html_path) as f:
        pdfkit.from_file(f, pdf_path, options=options)

render_html()
