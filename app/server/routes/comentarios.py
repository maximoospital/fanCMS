from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_comentario,
    delete_comentario,
    retrieve_comnts,
    retrieve_all_comnts
)
from server.models.comentario import (
    ErrorResponseModel,
    ResponseModel,
    SchemaDeComentario,
)

router = APIRouter();


@router.post("/", response_description="comentario agregada a la base de datos")
async def add_comentario_data(comentario: SchemaDeComentario = Body(...)):
    comentario = jsonable_encoder(comentario)
    print("Este es el herramienta que llega al router: ")
    print(comentario)
    new_comentario = await add_comentario(comentario)
    return ResponseModel(new_comentario, "comentario agregada exitosamente.")

@router.get("/{herramienta_id}", response_description="comnts obtenidas de la base de datos")
async def get_comnts(herramienta_id):
    comnts = await retrieve_comnts(herramienta_id)
    if comnts:
        return ResponseModel(comnts, "comnts obtenidas exitosamente.")
    return ResponseModel(comnts, "No se encontraron comnts.")

@router.get("/todos/", response_description="todos los comnts obtenidas de la base de datos")
async def get_comnts():
    comnts = await retrieve_all_comnts()
    if comnts:
        return ResponseModel(comnts, "comnts obtenidas exitosamente.")
    return ResponseModel(comnts, "No se encontraron comnts.")

@router.delete("/comment/{commentid}", response_description="comentario eliminada de la base de datos")
async def delete_comentario_data(commentid: str):
    deleted_comentario = await delete_comentario(commentid)
    if deleted_comentario:
        return ResponseModel("comentario con ID: {} eliminada exitosamente.".format(commentid),"comentario eliminada exitosamente.")
    return ErrorResponseModel("No se encontró un comentario con ese id.", 404, "comentario no encontrada.")