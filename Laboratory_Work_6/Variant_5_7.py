from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello World from FastAPI"}

if __name__=="__main__":
    uvicorn.run("Variant_5_7:app", host="127.0.0.1", port=5001, reload=True)