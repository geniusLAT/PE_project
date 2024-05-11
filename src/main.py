
import os
import uvicorn

if __name__ == "__main__":
    try:
        uvicorn.run("fa:app", host="0.0.0.0", port=8081, reload=False, log_level="debug")
    except Exception as e:
        print("Error on running uvicorn: "+str(e))
