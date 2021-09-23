import uvicorn
from main import app

if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=5000, use_colors=True, reload=True)
