import uvicorn
from os import getenv


if __name__ == '__main__':
    port = int(getenv("PORT", 8000))
    # uvicorn.run("app.app:app", host="192.168.193.60", port = port, reload=True)
    uvicorn.run("app.app:app", host="192.168.193.60", port = port, reload=True )
