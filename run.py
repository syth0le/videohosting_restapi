import uvicorn
from main import app

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=5000)
    uvicorn.run("run:app", host="127.0.0.1", port=5000, use_colors=True, reload=True)