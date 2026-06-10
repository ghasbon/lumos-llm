import logging
from fastapi import FastAPI, Request
from proxy import proxy_handler

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

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def proxy(request: Request, path: str):
    return await proxy_handler(request, path)
