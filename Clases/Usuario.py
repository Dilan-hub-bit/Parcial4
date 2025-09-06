class Usuario:
    def __init__(self, nombre, apellidos, email, nickname, clave):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.nickname = nickname
        self.clave = clave

Usuario = []

def guardarUsuario(nombre, apellidos, email, nickname, clave):
    
    if any(u.nickname == nickname for u in Usuario):
        return False  
    nuevo_usuario = Usuario(nombre, apellidos, email, nickname, clave)
    Usuario.append(nuevo_usuario)
    return True

def validarUsuario(nickname, clave):
    for u in Usuario:
        if u.nickname == nickname and u.clave == clave:
            return u
    return None
