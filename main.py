from fastapi import FastAPI

from router import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def root():
    return [{route.path: route.description} for route in router.routes]
