from pydantic import BaseModel, constr, PositiveInt, ValidationError

class guia(BaseModel):
    Num_guia: PositiveInt
    Nom_remitente: str
    Id_remitente: PositiveInt
    Origen : str
    Nom_destinatario : str
    Id_destinatario: PositiveInt
    Destino : str
    Tipo_mercancia:str
    kilos: int
    flete: float
    total : float



    