from fastapi import FastAPI

app = FastAPI(
    title="Product Inventory API",
    description="A learning project for managing product inventory.",
    version="0.1.0",
)


@app.get("/")
def home():
    return {"message": "Product Inventory API is running!"}
