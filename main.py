import logging
from fastapi import FastAPI

# ---- Logging setup ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("lumos")

# ---- App ----
app = FastAPI(title="Lumos")

@app.on_event("startup")
async def startup_event():
    logger.info("Lumos starting 🚀")

@app.get("/health")
async def health():
    logger.info("Health check requested")
    return {"status": "ok"}