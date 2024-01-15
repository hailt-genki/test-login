from app.models.domain.rwmodel import RWModel
from pydantic import ConfigDict


class RWSchema(RWModel):
    model_config = ConfigDict(
        from_attributes = True,
    )

