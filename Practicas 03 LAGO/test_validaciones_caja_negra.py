import pytest
from validaciones import validar_contrasena, validar_correo

# -------------------------
# PARTICIÓN DE EQUIVALENCIA
# -------------------------

@pytest.mark.parametrize("contra,usuario,resultado", [
    ("Usuario123!", "Usuario", True),   # válida
    ("abc", "user", False),             # longitud inválida
    ("Password!", "user", False),       # falta número
    ("Password1", "user", False),       # falta especial
    ("password1!", "user", False),      # falta mayúscula
    ("PASSWORD1!", "user", False),      # falta minúscula
])
def test_contra_equivalencia(contra, usuario, resultado):
    assert validar_contrasena(contra, usuario) == resultado


# -------------------------
# VALORES LÍMITE CONTRASEÑA
# -------------------------
def test_contra_min_long_exacta():
    assert validar_contrasena("Aa1!user", "user") == True  # 8 exactos


# -------------------------
# EMAIL
# -------------------------
@pytest.mark.parametrize("correo,resultado", [
    ("usuario123@dominio.com", True),  # válido
    ("abcde@dom.com", False),          # usuario límite <6
    ("usuario@dominio", False),        # sin punto
    ("usuario#dom.com", False),        # sin arroba
])
def test_correo_equivalencia(correo, resultado):
    assert validar_correo(correo) == resultado
