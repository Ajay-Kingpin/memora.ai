from fastapi import FastAPI
from src.api.chat import router as chat_router
from src.api.memories import router as memories_router
from src.api.learning import router as learning_router
from src.api.habits import router as habits_router
from src.api.decisions import router as decisions_router
from src.api.voice import router as voice_router

app = FastAPI(title="Memora Layer 4 API")

app.include_router(chat_router)
app.include_router(memories_router)
app.include_router(learning_router)
app.include_router(habits_router)
app.include_router(decisions_router)
app.include_router(voice_router)

@app.get("/")
def root():
    return {"status": "ok"}
