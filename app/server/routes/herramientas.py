from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_herramienta,
    delete_herramienta,
    retrieve_herramienta,
    retrieve_herramientas,
    update_herramienta,
    delete_all,
    retrieve_latest_id,
)
from server.models.herramienta import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeHerramienta,
)

router = APIRouter();


@router.post("/", response_description="Herramienta agregada a la base de datos")
async def add_herramienta_data(herramienta: SchemaDeHerramienta = Body(...)):
    herramienta = jsonable_encoder(herramienta)
    print("Este es el herramienta que llega al router: ")
    print(herramienta)
    new_herramienta = await add_herramienta(herramienta)
    return ResponseModel(new_herramienta, "Herramienta agregada exitosamente.")

@router.get("/", response_description="Herramientas obtenidas de la base de datos")
async def get_herramientas():
    herramientas = await retrieve_herramientas()
    if herramientas:
        return ResponseModel(herramientas, "Herramientas obtenidas exitosamente.")
    return ResponseModel(herramientas, "No se encontraron herramientas.")

@router.get("/{id}", response_description="Herramienta obtenida de la base de datos")
async def get_herramienta_data(id):
    herramienta = await retrieve_herramienta(id)
    if herramienta:
        return ResponseModel(herramienta, "Herramienta obtenida exitosamente.")
    return ErrorResponseModel("No se encontró un herramienta con ese id.", 404, "Herramienta no encontrada.")

@router.put("/{id}")
async def update_herramienta_data(id: str, req: SchemaDeHerramienta = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_herramienta = await update_herramienta(id, req)
    if updated_herramienta:
        return ResponseModel("Herramienta con ID: {} actualizada exitosamente.".format(id),"Herramienta actualizada exitosamente.")
    return ErrorResponseModel("No se encontró un herramienta con ese id.", 404, "Herramienta no encontrada.")

@router.delete("/{id}", response_description="Herramienta eliminada de la base de datos")
async def delete_herramienta_data(id: str):
    deleted_herramienta = await delete_herramienta(id)
    if deleted_herramienta:
        return ResponseModel("Herramienta con ID: {} eliminada exitosamente.".format(id),"Herramienta eliminada exitosamente.")
    return ErrorResponseModel("No se encontró un herramienta con ese id.", 404, "Herramienta no encontrada.")

# route that deletes all herramientas
@router.delete("/", response_description="Herramientas eliminadas de la base de datos")
async def delete_all_herramientas():
    deleted_herramientas = await delete_all()
    if deleted_herramientas:
        return ResponseModel("Herramientas eliminadas exitosamente.")
    return ErrorResponseModel("No se encontraron herramientas.", 404, "Herramientas no encontradas.")

# route that retrieves the latest id from the herramientas table using it's name
@router.get("/latest/{name}", response_description="Latest id from herramientas table")
async def retrieve_latest(name: str):
    print("NOMBRE:")
    print(name)
    id = await retrieve_latest_id(name)
    if id:
        return ResponseModel(id, "Latest id retrieved successfully.")
    return ErrorResponseModel("No se encontró un id con ese nombre.", 404, "Id no encontrado.")
    