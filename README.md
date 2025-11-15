# 📌 Proyecto de Pruebas de Software

Pruebas de Caja Blanca, Caja Negra y Cobertura con pytest y coverage.py

Este proyecto implementa pruebas de software utilizando técnicas de
**caja blanca**, **caja negra**, **partición de equivalencia**,
**valores límite** y análisis de **cobertura de código** con
*coverage.py*.\
El objetivo es validar el correcto funcionamiento de dos funciones
principales incluidas en `validaciones.py`.

------------------------------------------------------------------------

## 🧪 Funciones Evaluadas

### ✔ validar_contrasena(contra, usuario)

Reglas validadas: - La contraseña no debe ser nula. - Debe tener al
menos 8 caracteres. - Debe contener minúsculas. - Debe contener
mayúsculas. - Debe contener al menos un número. - Debe incluir un
carácter especial. - Debe contener el nombre del usuario.

### ✔ validar_correo(correo)

Reglas validadas: - El correo no debe ser nulo. - Debe contener un
'@'. - El usuario (antes de @) debe tener más de 5 caracteres. - El
dominio debe contener al menos un punto (ej. `.com`).

------------------------------------------------------------------------

## 🧰 Tecnologías utilizadas

-   **Python 3**
-   **pytest**
-   **coverage.py**
-   **pytest-cov**
-   **Virtual Environment (.venv)**

------------------------------------------------------------------------

## 📁 Estructura del proyecto

    Proyecto/
    ├── .venv/
    ├── validaciones.py
    ├── tests/
    │   ├── test_validaciones_caja_blanca.py
    │   └── test_validaciones_caja_negra.py
    └── README.md

------------------------------------------------------------------------

## ⚙️ Instalación

### 1️⃣ Crear entorno virtual

``` bash
python -m venv .venv
```

### 2️⃣ Activar entorno virtual

**Windows:**

``` bash
.venv\Scriptsctivate
```

### 3️⃣ Instalar dependencias

``` bash
pip install pytest coverage pytest-cov
```

------------------------------------------------------------------------

## ▶️ Ejecución de Pruebas

Para ejecutar todas las pruebas:

``` bash
pytest -v
```

------------------------------------------------------------------------

## 📊 Cobertura de Código

Generar cobertura:

``` bash
coverage run -m pytest -v
```

Crear reporte en HTML:

``` bash
coverage html
```

Abrir reporte:

``` bash
start htmlcov/index.html
```

------------------------------------------------------------------------

## 📈 Resultados

El proyecto alcanzó:

    test_validaciones_caja_blanca.py → 100%
    test_validaciones_caja_negra.py  → 100%
    validaciones.py                  → 100%
    Cobertura total                 → 100%

Superando ampliamente el **mínimo requerido del 85%**.

------------------------------------------------------------------------

## 📝 Conclusiones

Las pruebas diseñadas cubren completamente todas las rutas lógicas de
las funciones evaluadas, garantizando su correcto funcionamiento ante
entradas válidas e inválidas.\
El uso de pytest y coverage permitió validar automáticamente el
comportamiento y generar un análisis detallado de la cobertura del
código.

------------------------------------------------------------------------

## 👨‍💻 Autor

Proyecto desarrollado por **TU NOMBRE AQUÍ**\
Materia: *Pruebas de Software*
