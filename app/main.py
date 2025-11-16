from fastapi import FastAPI
from app.routes.dpr_routes import router as dpr_router
from app.routes.health import router as health_router

app = FastAPI(
    title="DPR Assessment Backend",
    version="0.1"
)

app.include_router(dpr_router, prefix="/dpr")
app.include_router(health_router, prefix="/health")

@app.get("/")
def root():
    return {"message": "DPR Backend Running"}
