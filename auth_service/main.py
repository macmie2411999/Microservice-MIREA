from fastapi import FastAPI
from auth.router import router

app = FastAPI(
    title='BLOG API',
    version='0.1.6'
)

app.include_router(router, prefix='/api')


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True)
