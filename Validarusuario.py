from pydantic import BaseModel, constr, PositiveInt, ValidationError

class Usuario(BaseModel):
    Correo : str
    Contraseña : str