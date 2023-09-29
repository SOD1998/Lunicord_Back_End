from ..database import DatabaseConnection

class Usuario:
    """Modelo de la clase Usuario"""
    def __init__(self, id_usuario = None, usuario = None, nombre = None,
                 apellido = None, clave = None, fecha_nacimiento = None,
                 imagen = None, email = None):
        """Constructor"""
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.clave = clave
        self.fecha_nacimiento = fecha_nacimiento
        self.imagen = imagen
        self.email = email
    
    def serialize(self):
        """Serializar representación del objeto
        Returns: dict: Representación del objeto
        Note: El atributo fecha_nacimiento es convertido a string
        """
        return {
            "id_usuario": self.id_usuario,
            "usuario": self.usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "clave": self.clave,
            "fecha_nacimiento": str(self.fecha_nacimiento),
            "imagen": self.imagen,
            "email": self.email
        }

    @classmethod
    def get(cls, usuario):
        """Obtener un usuario por su id
        Args: usuario (Usuario): Objeto usuario con el atributo id.
        Returns: Objeto Usuario.
        """
        query = """SELECT id_usuario, usuario, nombre, apellido,
        clave, fecha_nacimiento, imagen, email
        FROM lunicord.usuarios WHERE id_usuario = %s"""
        params = usuario.id_usuario,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(*result)
        return None
    
    @classmethod
    def get_all(cls):
        """Obtener lista con todos los usuarios.
        Returns: Lista de Objeto Usuario.
        """
        query = """SELECT id_usuario, usuario, nombre, apellido,
        clave, fecha_nacimiento, imagen, email
        FROM lunicord.usuarios"""
        results = DatabaseConnection.fetch_all(query)
        usuarios = []
        if results is not None:
            for result in results:
                usuarios.append(cls(*result))
        return usuarios
    
    @classmethod
    def create(cls, usuario):
        """Crea un nuevo usuario.
        Args: usuario (Usuario): Objeto Usuario
        """
        query = """INSERT INTO lunicord.usuarios (usuario, nombre,
        apellido, clave, fecha_nacimiento, imagen, email) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        params = usuario.usuario, usuario.nombre, usuario.apellido, \
                 usuario.clave, usuario.fecha_nacimiento, \
                 usuario.imagen, usuario.email
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def update(cls, usuario):
        """Actualiza un usuario.
        Args: usuario (Usuario): Objeto Usuario
        """
        allowed_columns = {'usuario', 'nombre', 'apellido',
                           'clave', 'fecha_nacimiento',
                           'imagen', 'email'}
        query_parts = []
        params = []
        for key, value in usuario.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(usuario.id_usuario)

        query = "UPDATE lunicord.usuarios SET " + ", ".join(query_parts) + " WHERE id_usuario = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, usuario):
        """Borrar un usuario
        Args: usuario (Usuario): Objeto usuario con el atributo id.
        """
        query = "DELETE FROM lunicord.usuarios WHERE id_usuario = %s"
        params = usuario.id_usuario,
        DatabaseConnection.execute_query(query, params=params)