import multiprocessing

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_check():
    """Electron can poll this endpoint to verify the server is ready."""
    return {"status": "ok", "message": "FastAPI server is running"}


@app.get("/users/{user_id}")
def get_user(user_id: int, include_details: bool = False):
    """A sample endpoint demonstrating path and query parameters."""
    return {"user_id": user_id, "include_details": include_details}


if __name__ == "__main__":
    # Required for packaging with Nuitka/PyInstaller and running via Electron
    # MANDATORY on Windows: prevents the executable from repeatedly spawning itself
    multiprocessing.freeze_support()
    uvicorn.run(app, host="127.0.0.1", port=8000)
