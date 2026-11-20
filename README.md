# Prediction API — Servicio de Inferencia con FastAPI

Microservicio web desarrollado en **FastAPI** para la predicción de valores inmobiliarios mediante validación de esquemas con **Pydantic** y documentación interactiva con **Swagger UI** y **Scalar**.

## Estructura del Proyecto
```text
├── data/
│   ├── dataset_v1.0.0.csv    # Dataset versionado (v1.0.0)
│   └── dataversion.json      # Metadatos y trazabilidad de versiones
├── main.py                   # Aplicación FastAPI y endpoint /predict
├── requirements.txt          # Dependencias del proyecto
├── .gitignore                # Exclusión de archivos temporales
└── README.md                 # Guía de reproducibilidad
```

## Instalación y Reproducibilidad

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Negocios
   ```

2. **Crear y activar entorno virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## Versionado de Datos
Los datos de referencia se gestionan bajo versionado semántico en `data/`:
* **Versión actual:** `v1.0.0` (`data/dataset_v1.0.0.csv`)
* **Registro de cambios:** Documentado en `data/dataversion.json` con esquema de columnas y fecha de creación.

## Ejecución y Pruebas
Iniciar el servidor local:
```bash
uvicorn main:app --reload
```
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **Scalar:** `http://127.0.0.1:8000/scalar`