from pydantic import BaseModel, constr, PositiveInt, ValidationError

class modificar(BaseModel):
    Num_guia : int
    Nuevo_total : float