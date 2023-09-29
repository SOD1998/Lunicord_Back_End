from flask import Blueprint
from ..controllers.usuario_controller import UsuarioController
from ..controllers.servidor_controller import ServidorController
from ..controllers.canal_controller import CanalController
from ..controllers.chat_controller import ChatController
# Para usuario:
usuario_bp = Blueprint('usuario_bp', __name__)
usuario_bp.route('/', methods=['GET'])(UsuarioController.get_all)
usuario_bp.route('/<int:id_usuario>', methods=['GET'])(UsuarioController.get)
usuario_bp.route('/', methods=['POST'])(UsuarioController.create)
usuario_bp.route('/<int:id_usuario>', methods=['PUT'])(UsuarioController.update)
usuario_bp.route('/<int:id_usuario>', methods=['DELETE'])(UsuarioController.delete)
# Para servidor:
servidor_bp = Blueprint('servidor_bp', __name__)
servidor_bp.route('/', methods=['GET'])(ServidorController.get_all)
servidor_bp.route('/<int:id_servidor>', methods=['GET'])(ServidorController.get)
servidor_bp.route('/', methods=['POST'])(ServidorController.create)
servidor_bp.route('/<int:id_servidor>', methods=['PUT'])(ServidorController.update)
servidor_bp.route('/<int:id_servidor>', methods=['DELETE'])(ServidorController.delete)
# Para canal:
canal_bp = Blueprint('canal_bp', __name__)
canal_bp.route('/', methods=['GET'])(CanalController.get_all)
canal_bp.route('/<int:id_canal>', methods=['GET'])(CanalController.get)
canal_bp.route('/', methods=['POST'])(CanalController.create)
canal_bp.route('/<int:id_canal>', methods=['PUT'])(CanalController.update)
canal_bp.route('/<int:id_canal>', methods=['DELETE'])(CanalController.delete)
# Para chat:
chat_bp = Blueprint('chat_bp', __name__)
chat_bp.route('/', methods=['GET'])(ChatController.get_all)
chat_bp.route('/<int:id_chat>', methods=['GET'])(ChatController.get)
chat_bp.route('/', methods=['POST'])(ChatController.create)
chat_bp.route('/<int:id_chat>', methods=['PUT'])(ChatController.update)
chat_bp.route('/<int:id_chat>', methods=['DELETE'])(ChatController.delete)