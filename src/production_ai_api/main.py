import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Production AI API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


def main() -> None:
    uvicorn.run("production_ai_api.main:app", host="0.0.0.0", port=8000, reload=True)