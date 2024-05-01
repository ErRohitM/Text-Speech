import uvicorn
from os import getenv


if __name__ == '__main__':
    port = int(getenv("PORT", 8000))
    # uvicorn.run("app.app:app", host="192.168.43.1", port = port, reload=True)
    uvicorn.run("app.app:app", host="192.168.171.186", port = port, reload=True )
