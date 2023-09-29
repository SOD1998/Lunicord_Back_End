from ..database import DatabaseConnection

class Servidor:
    """Modelo de la clase Servidor"""
    def __init__(self, id_servidor = None, nombre = None):
        """Constructor"""
        self.id_servidor = id_servidor
        self.nombre = nombre
    
    def serialize(self):
        """Serializar representación del objeto
        Returns: dict: Representación del objeto
        """
        return {
            "id_servidor": self.id_servidor,
            "nombre": self.nombre
        }

    @classmethod
    def get(cls, servidor):
        """Obtener un servidor por su id
        Args: servidor (Servidor): Objeto servidor con el atributo id.
        Returns: Objeto Servidor.
        """
        query = """SELECT id_servidor, nombre
        FROM lunicord.servidores WHERE id_servidor = %s"""
        params = servidor.id_servidor,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        """Obtener lista con todos los servidores.
        Returns: Lista de Objeto Servidor.
        """
        query = """SELECT id_servidor, nombre
        FROM lunicord.servidores"""
        results = DatabaseConnection.fetch_all(query)
        servidores = []
        if results is not None:
            for result in results:
                servidores.append(cls(*result))
        return servidores
    
    @classmethod
    def create(cls, servidor):
        """Crea un nuevo servidor.
        Args: servidor (Servidor): Objeto Servidor
        """
        query = """INSERT INTO lunicord.servidores (nombre) 
        VALUES (%s)"""
        params = servidor.nombre
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def update(cls, servidor):
        """Actualiza un servidor.
        Args: servidor (Servidor): Objeto Servidor
        """
        allowed_columns = {'nombre'}
        query_parts = []
        params = []
        for key, value in servidor.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(servidor.id_servidor)

        query = "UPDATE lunicord.servidores SET " + ", ".join(query_parts) + " WHERE id_servidor = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, servidor):
        """Borrar un servidor
        Args: servidor (Servidor): Objeto servidor con el atributo id.
        """
        query = "DELETE FROM lunicord.servidores WHERE id_servidor = %s"
        params = servidor.id_servidor,
        DatabaseConnection.execute_query(query, params=params)