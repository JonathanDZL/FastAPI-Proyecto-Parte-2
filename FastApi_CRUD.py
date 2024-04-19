from fastapi import FastAPI, HTTPException
from flask import jsonify
import uvicorn
from ConexionBD import * 
from ValidacionGuias import guia, ValidationError
from Validacionnumguia import num_guia
from Validarusuario import Usuario
from Validaredicion import modificar
app = FastAPI()


@app.post('/guia/crear')
async def guardar_guia_post(guia_data: guia):
    try:
        connection = get_connection()
        cursor = connection.cursor() 
            
        insert_query = """
        INSERT INTO guias (Num_guia, Nom_remitente, Id_remitente, Origen, Nom_destinatario, Id_destinatario, Destino, Tipo_mercancia, kilos, flete, total)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        guia_values = (guia_data.Num_guia, guia_data.Nom_remitente, guia_data.Id_remitente, guia_data.Origen, guia_data.Nom_destinatario, guia_data.Id_destinatario, guia_data.Destino, guia_data.Tipo_mercancia, guia_data.kilos, guia_data.flete, guia_data.total)
        cursor.execute(insert_query, guia_values)
        
        connection.commit()
        
        created_fields = {
            "Num_guia": guia_data.Num_guia,
            "Nom_remitente": guia_data.Nom_remitente,
            "Id_remitente": guia_data.Id_remitente,
            "Origen": guia_data.Origen,
            "Nom_destinatario": guia_data.Nom_destinatario,
            "Id_destinatario": guia_data.Id_destinatario,
            "Destino": guia_data.Destino,
            "Tipo_mercancia": guia_data.Tipo_mercancia,
            "kilos": guia_data.kilos,
            "flete": guia_data.flete,
            "total": guia_data.total
        }
        
        return {"mensaje": "Datos de guía válidos, se han guardado en la base de datos", "campos_creados": created_fields}, 201
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor al procesar la solicitud")
    
@app.delete('/guia/eliminar')
async def validar_numeroguia(guia: num_guia):
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        sql = "DELETE FROM guias WHERE Num_guia = %s"
        guia_values = (guia.Num_guia,)  
        cursor.execute(sql, guia_values)
        connection.commit()
       
        return {"mensaje": "Guia eliminada exitosamente"}

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    

@app.get('/guia/consulta')
async def validar_numeroguia(guia: num_guia):
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        sql = "SELECT * from guias WHERE Num_guia = %s"
        guia_values = (guia.Num_guia,)  
        cursor.execute(sql, guia_values)
        result = cursor.fetchall()

        return {
            'data': result
        }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post('/guia/modificar_total')
async def modificar_total_guia(modi: modificar):
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        sql = "UPDATE guias SET Total = %s WHERE Num_guia = %s"
        guia_values = (modi.Nuevo_total, modi.Num_guia)
        cursor.execute(sql, guia_values)
        connection.commit()
        
        return {"mensaje": "Total de la guía editado exitosamente"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor al procesar la solicitud")

@app.post('/usuario/crear')
async def guardar_usuario(usuario: Usuario):
    try:
        connection = get_connection()
        cursor = connection.cursor() 
        insert_query = "INSERT INTO usuarios (Correo, Contraseña) VALUES (%s, %s)"
        usuarios_values = (usuario.Correo, usuario.Contraseña)
        cursor.execute(insert_query, usuarios_values)

        connection.commit()
        
        return {"mensaje": "Datos de usuario, se han guardado en la base de datos"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno del servidor al procesar la solicitud")


if __name__=="__main__":
    uvicorn.run("FastApi_CRUD",port=8000,reload=True)
    
    

    

