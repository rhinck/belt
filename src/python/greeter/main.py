from fastapi import FastAPI
import uvicorn

app = FastAPI(debug=True)


@app.get("/")
async def root():
    import pydevd_pycharm
    pydevd_pycharm.settrace('localhost', port=5000, stdoutToServer=True, stderrToServer=True)
    print('Hello World')
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)