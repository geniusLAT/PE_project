import uvicorn
import os  # noqa: F401

if __name__ == "__main__":
    try:
        uvicorn.run("fa:app", host="0.0.0.0", port=int(os.environ['PORT']), reload=False, log_level="debug")
    except Exception as e:
        print("Error on running uvicorn: "+str(e))
