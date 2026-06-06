from fastapi import FastAPI
import time

app = FastAPI(title="Granular Service 1 - Items")

@app.post("/items/")
async def create_item(item: dict):
    # Simulate processing
    time.sleep(0.01)
    return {"message": "Item created", "data": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
