import io

from util.jimbofy import jimbofy
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/jimbo",
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },
    response_class=Response         
)
def jimbo(text: str):

    # The following character substitutions are meant for compatibility
    # with the Mudae Discord bot message format
    text = text.replace("*", "")
    text = text.replace("_", " ")

    img = jimbofy(text)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()
    return Response(content=img_bytes, media_type="image/png")
