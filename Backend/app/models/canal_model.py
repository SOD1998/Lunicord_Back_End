from ..database import DatabaseConnection

class Canal:
    """Modelo de la clase Canal"""
    def __init__(self, id_canal = None, nombre = None, descripcion = None, id_servidor = None):
        """Constructor"""
        self.id_canal = id_canal
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_servidor = id_servidor
    
    def serialize(self):
        """Serializar representación del objeto
        Returns: dict: Representación del objeto
        """
        return {
            "id_canal": self.id_canal,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "id_servidor": self.id_servidor
        }

    @classmethod
    def get(cls, canal):
        """Obtener un canal por su id
        Args: canal (Canal): Objeto canal con el atributo id.
        Returns: Objeto Canal.
        """
        query = """SELECT id_canal, nombre, descripcion, id_servidor
        FROM lunicord.canales WHERE id_canal = %s"""
        params = canal.id_canal,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        """Obtener lista con todos los canales.
        Returns: Lista de Objeto Canales.
        """
        query = """SELECT id_canal, nombre, descripcion, id_servidor
        FROM lunicord.canales"""
        results = DatabaseConnection.fetch_all(query)
        canales = []
        if results is not None:
            for result in results:
                canales.append(cls(*result))
        return canales
    
    @classmethod
    def create(cls, canal):
        """Crea un nuevo canal.
        Args: canal (Canal): Objeto Canal
        """
        query = """INSERT INTO lunicord.canales (nombre, descripcion, id_servidor) 
        VALUES (%s, %s, %s)"""
        params = canal.nombre, canal.descripcion, canal.id_servidor
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def update(cls, canal):
        """Actualiza un canal.
        Args: canal (Canal): Objeto Canal
        """
        allowed_columns = {'nombre', 'descripcion', 'id_servidor'}
        query_parts = []
        params = []
        for key, value in canal.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(canal.id_canal)

        query = "UPDATE lunicord.canales SET " + ", ".join(query_parts) + " WHERE id_canal = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, canal):
        """Borrar un canal
        Args: canal (Canal): Objeto canal con el atributo id.
        """
        query = "DELETE FROM lunicord.canales WHERE id_canal = %s"
        params = canal.id_canal,
        DatabaseConnection.execute_query(query, params=params)