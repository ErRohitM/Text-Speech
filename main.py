import uvicorn
from os import getenv


if __name__ == '__main__':
    port = int(getenv("PORT", 8000))
    uvicorn.run("app.app:app", host="10.0.2.2", port = port, reload=True )
