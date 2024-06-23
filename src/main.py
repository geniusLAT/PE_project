import uvicorn

if __name__ == "main":
    try:
        rl = False
        p = 8081
        host = "0.0.0.0"
        uvicorn.run("fa:app", host=host, port=p, reload=rl, log_level="debug")
    except Exception as e:
        print("Error on running uvicorn: " + str(e))
