from fastapi import FastAPI
from pydantic import BaseModel, Field
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(
    title="Prediction API",
    version="1.0.0",
    description="Endpoint mínimo de inferencia de Machine Learning",
    docs_url="/docs",  # Swagger UI automático
)

# 1. Esquema de entrada con validación y ejemplos para la documentación
class FeaturesPayload(BaseModel):
    area_m2: float = Field(..., gt=0, json_schema_extra={"example": 85.5}, description="Superficie en m²")
    habitaciones: int = Field(..., ge=1, json_schema_extra={"example": 3}, description="Número de dormitorios")
    antiguedad_anios: int = Field(..., ge=0, json_schema_extra={"example": 5}, description="Años desde la construcción")

# 2. Esquema de salida
class PredictionResponse(BaseModel):
    predicted_value: float
    unit: str
    model_version: str

# 3. Endpoint de predicción
@app.post("/predict", response_model=PredictionResponse, tags=["Inferencia"])
def predict(data: FeaturesPayload):
    # Aquí cargarías tu modelo entrenado (ej. model.predict(...))
    # Para este ejemplo se simula un cálculo de estimación de precio:
    base_price = 50000
    estimacion = base_price + (data.area_m2 * 1200) + (data.habitaciones * 5000) - (data.antiguedad_anios * 800)
    
    return PredictionResponse(
        predicted_value=round(estimacion, 2),
        unit="USD",
        model_version="v1.0.0"
    )

# 4. Integración de Scalar
@app.get("/scalar", include_in_schema=False)
async def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )