from fastapi import FastAPI
import uvicorn


def main():
    print("Hello from noteapp!")
    uvicorn.run(app,host="127.0.0.1",port=8000)
    
app = FastAPI()


@app.get("/hello")
async def root():
    return{"message":"Hello Shahrukh"}


if __name__ == "__main__":
    main()
