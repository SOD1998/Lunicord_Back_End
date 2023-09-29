from ..models.chat_model import Chat
from flask import request

class ChatController:
    """Controlador de clase Chat"""
    @classmethod
    def get(cls, id_chat):
        """Obtener chat por id"""
        chat = Chat(id_chat=id_chat)
        result = Chat.get(chat)
        if result is not None:
            return result.serialize(), 200
        
    @classmethod
    def get_all(cls):
        """Obtener todos los chats"""
        chats_objects = Chat.get_all()
        chats = []
        for chat in chats_objects:
            chats.append(chat.serialize())
        return chats, 200
    
    @classmethod
    def create(cls):
        """Crear un nuevo chat"""
        data = request.json
        # TODO: Validate data
        chat = Chat(**data)
        Chat.create(chat)
        return {'mensaje': 'Chat creado exitosamente'}, 201

    @classmethod
    def update(cls, id_chat):
        """Actualizar un chat"""
        data = request.json
        # TODO: Validate data
        data['id_chat'] = id_chat
        chat = Chat(**data)
        # TODO: Validate user exists
        Chat.update(chat)
        return {'mensaje': 'Chat actualizado exitosamente'}, 200
    
    @classmethod
    def delete(cls, id_chat):
        """Eliminar un chat"""
        chat = Chat(id_chat=id_chat)
        # TODO: Validate user exists
        Chat.delete(chat)
        return {'mensaje': 'Chat eliminado exitosamente'}, 204