from fastapi import FastAPI
import model

app = FastAPI()


def process(input_text):
    return str(model.analyse(input_text)[0])


@app.get("/process_text/{text}")
async def process_text(text: str):
    result = process(text)
    return {"result": result}
