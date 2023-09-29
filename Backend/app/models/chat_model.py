from ..database import DatabaseConnection

class Chat:
    """Modelo de la clase Chat"""
    def __init__(self, id_chat = None, mensaje = None, fecha = None, id_canal = None):
        """Constructor"""
        self.id_chat = id_chat
        self.mensaje = mensaje
        self.fecha = fecha
        self.id_canal = id_canal
    
    def serialize(self):
        """Serializar representación del objeto
        Returns: dict: Representación del objeto
        Note: El atributo fecha es convertido a string
        """
        return {
            "id_chat": self.id_chat,
            "mensaje": self.mensaje,
            "fecha": str(self.fecha),
            "id_canal": self.id_canal
        }

    @classmethod
    def get(cls, chat):
        """Obtener un chat por su id
        Args: chat (Chat): Objeto chat con el atributo id.
        Returns: Objeto Chat.
        """
        query = """SELECT id_chat, mensaje, fecha, id_canal
        FROM lunicord.chat WHERE id_chat = %s"""
        params = chat.id_chat,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        """Obtener lista con todos los chats.
        Returns: Lista de Objeto Chats.
        """
        query = """SELECT id_chat, mensaje, fecha, id_canal
        FROM lunicord.chat"""
        results = DatabaseConnection.fetch_all(query)
        chats = []
        if results is not None:
            for result in results:
                chats.append(cls(*result))
        return chats
    
    @classmethod
    def create(cls, chat):
        """Crea un nuevo chat.
        Args: chat (Chat): Objeto Chat
        """
        query = """INSERT INTO lunicord.chat (mensaje, fecha, id_canal) 
        VALUES (%s, %s, %s)"""
        params = chat.mensaje, chat.fecha, chat.id_canal
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def update(cls, chat):
        """Actualiza un chat.
        Args: chat (Chat): Objeto Chat
        """
        allowed_columns = {'mensaje', 'fecha', 'id_canal'}
        query_parts = []
        params = []
        for key, value in chat.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(chat.id_chat)

        query = "UPDATE lunicord.chat SET " + ", ".join(query_parts) + " WHERE id_chat = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, chat):
        """Borrar un chat
        Args: chat (Chat): Objeto chat con el atributo id.
        """
        query = "DELETE FROM lunicord.chat WHERE id_chat = %s"
        params = chat.id_chat,
        DatabaseConnection.execute_query(query, params=params)
