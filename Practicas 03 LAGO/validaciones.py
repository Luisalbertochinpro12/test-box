import re

def validar_contrasena(contra, usuario):
    if contra is None or usuario is None:
        return False
    
    if len(contra) < 8:
        return False
    
    if not re.search(r"[a-z]", contra):
        return False
    
    if not re.search(r"[A-Z]", contra):
        return False
    
    if not re.search(r"[0-9]", contra):
        return False
    
    if not re.search(r"[\W_]", contra):
        return False
    
    if usuario.lower() not in contra.lower():
        return False
    
    return True


def validar_correo(correo):
    if correo is None:
        return False
    
    partes = correo.split("@")
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes

    if len(usuario) <= 5:
        return False

    if "." not in dominio:
        return False
    
    return True
