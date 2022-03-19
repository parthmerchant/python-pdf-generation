import io

from fastapi import FastAPI
from starlette.responses import StreamingResponse

from pdf import generate_pdf

app = FastAPI()


@app.get("/")
async def get_pdf():
    pdf_bytes = generate_pdf('pdf_template.html')
    return StreamingResponse(
        io.BytesIO(pdf_bytes),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment;filename=export.pdf"},
    )
