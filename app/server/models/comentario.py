from typing import Optional

from pydantic import BaseModel, Field, constr, create_model


class SchemaDeComentario(BaseModel):
    herramienta_id: constr(strict=True) = Field(...)
    texto: constr(strict=True) = Field(...)

    class config:
        schema_extra = {
            "ejemplo": {
                "herramienta_id": "60",
                "texto": "Chat grupal"
            }
        }

    @classmethod
    def as_optional(cls):
        annonations = cls.__fields__
        fields = {
            attribute: (Optional[data_type.type_], None)
            for attribute, data_type in annonations.items()
        }
        OptionalModel = create_model(f"Optional{cls.__name__}", **fields)
        return OptionalModel


class UpdateHerramientaModel(BaseModel):
    herramienta_id: Optional[constr(strict=True)]
    texto: Optional[constr(strict=True)]
    
    class Config:
        schema_extra = {
            "ejemplo": {
                "herramienta_id": "60",
                "texto": "Chat grupal"
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}