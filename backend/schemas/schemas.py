from pydantic import BaseModel, Field
from typing import List, Optional


class PredictionRequest(BaseModel):
    company_name: Optional[str] = None
    machine_id: Optional[str] = None

    machine_type: str

    air_temperature: float = Field(gt=0)
    process_temperature: float = Field(gt=0)
    rotational_speed: int = Field(gt=0)
    torque: float = Field(ge=0)
    tool_wear: int = Field(ge=0)


class RootCause(BaseModel):
    factor: str
    severity: str
    value: float
    contribution: float
    message: str


class FeatureImportance(BaseModel):
    feature: str
    contribution: float


class PredictionResponse(BaseModel):
    company_name: Optional[str] = None
    machine_id: Optional[str] = None
    machine_type: Optional[str] = None

    prediction: str
    failure_probability: float
    risk_level: str
    health_score: int

    root_causes: List[RootCause]
    feature_importance: List[FeatureImportance]