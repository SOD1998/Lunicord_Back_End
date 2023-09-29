from ..models.servidor_model import Servidor
from flask import request

class ServidorController:
    """Controlador de clase Servidor"""
    @classmethod
    def get(cls, id_servidor):
        """Obtener servidor por id"""
        servidor = Servidor(id_servidor=id_servidor)
        result = Servidor.get(servidor)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Obtener todos los servidores"""
        servidores_objects = Servidor.get_all()
        servidores = []
        for servidor in servidores_objects:
            servidores.append(servidor.serialize())
        return servidores, 200
    
    @classmethod
    def create(cls):
        """Crear un nuevo servidor"""
        data = request.json
        # TODO: Validate data
        servidor = Servidor(**data)
        Servidor.create(servidor)
        return {'mensaje': 'Servidor creado exitosamente'}, 201

    @classmethod
    def update(cls, id_servidor):
        """Actualizar un servidor"""
        data = request.json
        # TODO: Validate data
        data['id_servidor'] = id_servidor
        servidor = Servidor(**data)
        # TODO: Validate user exists
        Servidor.update(servidor)
        return {'mensaje': 'Servidor actualizado exitosamente'}, 200
    
    @classmethod
    def delete(cls, id_servidor):
        """Eliminar un servidor"""
        servidor = Servidor(id_servidor=id_servidor)
        # TODO: Validate user exists
        Servidor.delete(servidor)
        return {'mensaje': 'Servidor eliminado exitosamente'}, 204