from fastapi import FastAPI
from routers import version, posts, stats

app = FastAPI()

app.include_router(version.router, prefix="/version", tags=["version"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(stats.router, prefix="/stats", tags=["stats"])
