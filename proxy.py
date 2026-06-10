import httpx
import config
from fastapi import Request, Response

TARGET = f"http://{config.REDIRECTION_IP}:{config.REDIRECTION_PORT}"


async def proxy_handler(request: Request, path: str):
    url = f"{TARGET}/{path}"

    async with httpx.AsyncClient() as client:
        resp = await client.request(
            method=request.method,
            url=url,
            content=await request.body(),
            headers=dict(request.headers),
            params=request.query_params,
        )

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=dict(resp.headers),
    )