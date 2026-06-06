from fastapi import FastAPI
import time

app = FastAPI(title="Granular Service 2 - Users")

@app.post("/users/")
async def create_user(user: dict):
    # Simulate processing
    time.sleep(0.01)
    return {"message": "User created", "data": user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
