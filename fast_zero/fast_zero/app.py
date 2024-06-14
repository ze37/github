from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Nosso ola Mundo</title>
        </head>
        <body>
            <h1>Olá Mundo</h1>
        </body>
    </html>
    """
