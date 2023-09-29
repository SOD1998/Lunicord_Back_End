from ..models.usuario_model import Usuario
from flask import request

class UsuarioController:
    """Controlador de clase Usuario"""
    @classmethod
    def get(cls, id_usuario):
        """Obtener usuario por id"""
        usuario = Usuario(id_usuario=id_usuario)
        result = Usuario.get(usuario)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Obtener todos los usuarios"""
        usuarios_objects = Usuario.get_all()
        usuarios = []
        for usuario in usuarios_objects:
            usuarios.append(usuario.serialize())
        return usuarios, 200
    
    @classmethod
    def create(cls):
        """Crear un nuevo usuario"""
        data = request.json
        # TODO: Validate data
        usuario = Usuario(**data)
        Usuario.create(usuario)
        return {'mensaje': 'Usuario registrado exitosamente'}, 201

    @classmethod
    def update(cls, id_usuario):
        """Actualizar un usuario"""
        data = request.json
        # TODO: Validate data
        data['id_usuario'] = id_usuario
        usuario = Usuario(**data)
        # TODO: Validate user exists
        Usuario.update(usuario)
        return {'mensaje': 'Usuario actualizado exitosamente'}, 200
    
    @classmethod
    def delete(cls, id_usuario):
        """Eliminar un usuario"""
        usuario = Usuario(id_usuario=id_usuario)
        # TODO: Validate user exists
        Usuario.delete(usuario)
        return {'mensaje': 'Usuario eliminado exitosamente'}, 204