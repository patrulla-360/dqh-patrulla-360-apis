from fastapi import FastAPI
from routers.oficiales import router as oficiales_router

app = FastAPI(
    title="API Oficiales",
    description="API para gestionar los oficiales",
    version="1.0.0"
)

# Registrar rutas
app.include_router(oficiales_router, prefix="/api/v1", tags=["Oficiales"])

@app.get("/")
def root():
    return {"message": "Bienvenido a la API de oficiales"}
