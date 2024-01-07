from fastapi import FastAPI


app = FastAPI()
import model

def process(input_text):
    try:
        payload =str(model.analyse(input_text)[0])
        print("model payload: "+payload)
        return payload
    except Exception as e:
        print("It is error on line 12:" +str(e))
        print("Error inside the model.py")
        return "model.py error"


@app.get("/process_text/{text}")
async def process_text(text: str):
    try:
        result = process(text)
        print("Text prosessed normally.")
        return {"result": result}
    
    except Exception as e:
        print("It is error on line 25:" +str(e))
        print("Error inside the processing")
        return {"result": "None"}

