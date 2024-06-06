from typing import Optional

from pydantic import BaseModel, Field, constr, conint, create_model


class SchemaDeHerramienta(BaseModel):
    nombre: constr(strict=True) = Field(...)
    descripcion: constr(strict=True) = Field(...)
    plan: constr(strict=True) = Field(...)
    vencimiento: constr(strict=True) = Field(...)
    cliente: constr(strict=True) = Field(...)
    sitio: constr(strict=True) = Field(...)
    administrador: constr(strict=True) = Field(...)
    activo: bool = Field(...)
    renovacion: bool = Field(...)

    class config:
        schema_extra = {
            "ejemplo": {
                "nombre": "Slack",
                "descripcion": "Chat grupal",
                "plan": "Anual",
                "vencimiento": "2021-01-13",
                "cliente": "Natura",
                "sitio": "https://www.slack.com",
                "administrador": "maximo.ospital@gmail.com",
                "activo": True,
                "renovacion": True
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
    nombre: Optional[constr(strict=True)]
    descripcion: Optional[constr(strict=True)]
    plan: Optional[constr(strict=True)]
    vencimiento: Optional[conint(strict=True)]
    cliente: Optional[constr(strict=True)]
    sitio: Optional[constr(strict=True)]
    administrador: Optional[constr(strict=True)]
    activo: Optional[bool]
    renovacion: Optional[bool]
    
    class Config:
        schema_extra = {
            "ejemplo": {
                "nombre": "Slack",
                "descripcion": "Chat grupal",
                "plan": "Anual",
                "vencimiento": "2021-01-13",
                "cliente": "Natura",
                "sitio": "https://www.slack.com",
                "administrador": "maximo.ospital@gmail.com",
                "activo": True,
                "renovacion": True
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