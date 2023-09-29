from ..models.canal_model import Canal
from flask import request

class CanalController:
    """Controlador de clase Canal"""
    @classmethod
    def get(cls, id_canal):
        """Obtener canal por id"""
        canal = Canal(id_canal=id_canal)
        result = Canal.get(canal)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Obtener todos los canales"""
        canales_objects = Canal.get_all()
        canales = []
        for canal in canales_objects:
            canales.append(canal.serialize())
        return canales, 200
    
    @classmethod
    def create(cls):
        """Crear un nuevo canal"""
        data = request.json
        # TODO: Validate data
        canal = Canal(**data)
        Canal.create(canal)
        return {'mensaje': 'Canal creado exitosamente'}, 201

    @classmethod
    def update(cls, id_canal):
        """Actualizar un canal"""
        data = request.json
        # TODO: Validate data
        data['id_canal'] = id_canal
        canal = Canal(**data)
        # TODO: Validate user exists
        Canal.update(canal)
        return {'mensaje': 'Canal actualizado exitosamente'}, 200
    
    @classmethod
    def delete(cls, id_canal):
        """Eliminar un canal"""
        canal = Canal(id_canal=id_canal)
        # TODO: Validate user exists
        Canal.delete(canal)
        return {'mensaje': 'Canal eliminado exitosamente'}, 204