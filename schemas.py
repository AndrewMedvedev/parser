from pydantic import BaseModel, Field

from constants import (
    MAX_BONUS_POINTS,
    MAX_POINTS,
    MAX_PRIORITY,
    MIN_BONUS_POINTS,
    MIN_POINTS,
    MIN_PRIORITY,
)


class Applicant(BaseModel):
    applicant_id: str
    rating: int
    institute: str
    direction: str
    priority: int = Field(ge=MIN_PRIORITY, le=MAX_PRIORITY)
    points: int = Field(ge=MIN_POINTS, le=MAX_POINTS)
    bonus_points: int = Field(ge=MIN_BONUS_POINTS, le=MAX_BONUS_POINTS)
    original: bool
