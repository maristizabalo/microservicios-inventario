
# 🛠️ Proyecto Microservicios con Python, Django

## 📌 Requisitos Previos

- **Python 3.13.5**  
- **PostgreSQL**  
- Tener creadas previamente las bases de datos vacías en PostgreSQL:

| Microservicio | Base de Datos |
|---------------|---------------|
| Auth          | auth          |
| Inventory     | inventory     |
| Movement      | movement      |

---

## 📂 Estructura del Proyecto
```
/backend/
├── auth/
├── inventory/
├── movement/
├── api_gateway/
├── run_services.py
/postman/
├── collection_api_gateway.json
```

---

## 📄 Descripción General
Este proyecto está basado en arquitectura de **microservicios** utilizando **Django REST Framework** para el backend.

### 🔑 **Microservicios**
| Servicio    | Puerto | Funcionalidad       |
|-------------|--------|---------------------|
| Auth        | 8001   | Registro y login JWT |
| Inventory   | 8002   | Gestión de productos |
| Movement    | 8003   | Entradas y salidas   |
| API Gateway | 8004   | Único punto de acceso |

---

## 🚀 Cómo Ejecutar Localmente

### 1️⃣ Crear las bases de datos en PostgreSQL

Asegúrate de tener las siguientes bases de datos vacías:
- **auth**
- **inventory**
- **movement**

No es necesario crear tablas, solo las bases de datos.

### 2️⃣ Ejecutar el Script Automático
Desde la carpeta `/backend`:
```bash
python run_services.py
```

Este script realiza lo siguiente para cada microservicio:
- Crea entorno virtual si no existe.
- Instala `requirements.txt`.
- Ejecuta `makemigrations` y `migrate`.
- Levanta cada microservicio en su puerto correspondiente.

Cada servicio se abrirá en una ventana nueva de Powershell.

---

## 📤 Colección Postman
Dentro de la raíz del proyecto hay una carpeta llamada `/postman/` que contiene un archivo `api_gateway_collection.json`.  
Puedes importar esta colección en Postman para consultar y probar todos los endpoints del **API Gateway** fácilmente.

---

## 💡 Consideraciones Técnicas

### 🔐 Tokenización y Seguridad:
- Se utiliza JWT para la autenticación entre microservicios.
- El API Gateway controla todo acceso hacia los microservicios.

### 📊 Inventario:
- Permite gestionar productos (crear, listar, actualizar stock).

### 📦 Movimiento:
- Permite registrar entradas y salidas de productos.
- Valida que no se puedan retirar más productos de los disponibles.

---

## 📚 Tecnologías

### Backend:
- Django REST Framework
- PostgreSQL
- Python 3.13.5

### Otros:
- JWT Authentication (SimpleJWT)
- API Gateway personalizado con proxy en Django

---

## 👨‍💻 Autor
Maicol Jacobo Aristizabal Obando

**Prueba Técnica Desarrollador Senior Python**
