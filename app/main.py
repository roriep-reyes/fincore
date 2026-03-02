from fastapi import FastAPI

app = FastAPI (
    title="FinCore",
    version="0.1.0",
    description="Double-entry ledger and payments API"
)


@app.get("/health")
def health():
    return {"status": "ok"}
