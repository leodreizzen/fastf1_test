from fastapi import FastAPI
import fastf1
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    year = 2023
    gp = 1
    event = 1

    session_event = fastf1.get_session(year, gp, event)
    session_event.load()

    return {"message": str(session_event.laps.pick_fastest().get_telemetry())}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
