from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


pass  "hello world"

dfgd
ah1
DeprecationWarning
say_hellog

say_hello
DeprecationWarning