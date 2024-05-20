from fastapi import APIRouter, Request

router = APIRouter()

request_counts = {
    "version": {"GET": 0},
    "posts": {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0},
}

@router.middleware("http")
async def count_requests(request: Request, call_next):
    if request.url.path.startswith("/version"):
        request_counts["version"]["GET"] += 1
    elif request.url.path.startswith("/posts"):
        request_counts["posts"][request.method] += 1
    
    response = await call_next(request)
    return response

@router.get("/")
async def get_stats():
    return request_counts
