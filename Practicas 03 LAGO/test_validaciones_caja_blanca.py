from validaciones import validar_contrasena, validar_correo

# --------------------------
# PRUEBAS CAJA BLANCA CONTRASEÑA
# --------------------------

def test_contra_none():
    assert validar_contrasena(None, "luis") == False

def test_contra_corta():
    assert validar_contrasena("Ab1@", "luis") == False

def test_contra_sin_minuscula():
    assert validar_contrasena("PASSWORD1@", "pass") == False

def test_contra_sin_mayuscula():
    assert validar_contrasena("password1@", "pass") == False

def test_contra_sin_numero():
    assert validar_contrasena("Password@", "pass") == False

def test_contra_sin_especial():
    assert validar_contrasena("Password1", "pass") == False

def test_contra_no_contiene_usuario():
    assert validar_contrasena("Password1@", "luis") == False

def test_contra_valida():
    assert validar_contrasena("LuisPassword1@", "luis") == True


# --------------------------
# PRUEBAS CAJA BLANCA CORREO
# --------------------------

def test_correo_none():
    assert validar_correo(None) == False

def test_correo_sin_arroba():
    assert validar_correo("usuario.gmail.com") == False

def test_correo_usuario_corto():
    assert validar_correo("luis@correo.com") == False  # "luis" = 4 chars

def test_correo_sin_dominio():
    assert validar_correo("usuario@correo") == False

def test_correo_valido():
    assert validar_correo("usuario123@correo.com") == True
