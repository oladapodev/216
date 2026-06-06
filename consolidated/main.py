from fastapi import FastAPI
import time

app = FastAPI(title="Consolidated API")

@app.post("/items/")
async def create_item(item: dict):
    # Simulate processing
    time.sleep(0.01)
    return {"message": "Item created", "data": item}

@app.post("/users/")
async def create_user(user: dict):
    # Simulate processing
    time.sleep(0.01)
    return {"message": "User created", "data": user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
