# 🚀 Movilnet - Sistema de Gestión de Proyectos

Sistema de seguimiento y gestión de proyectos desarrollado con **Django** para Movilnet.

## 📋 Descripción

Plataforma interna para gestionar proyectos, tareas (tablero Kanban), reportes y equipos de trabajo.

## 🛠️ Tecnologías

- **Python** 3.x
- **Django** (Framework web)
- **PostgreSQL** (Base de datos)
- **django-unfold** (Admin mejorado)

## ⚙️ Instalación local

### 1. Clonar el repositorio
```bash
git clone https://github.com/crisdux-cell/caramelo_de_chocolate.git
cd caramelo_de_chocolate
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Crear la base de datos PostgreSQL `gestion_de_seguimiento` y ajustar las credenciales en `movilnet_config/settings.py`.

> ⚠️ **Importante:** Para producción, mover las credenciales a variables de entorno (archivo `.env`).

### 5. Aplicar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor
```bash
python manage.py runserver
```

Acceder en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📁 Estructura del Proyecto

```
movilnet_proyect/
├── movilnet_config/    # Configuración principal de Django
├── proyectos/          # App principal (modelos, vistas, admin)
│   ├── models.py       # Proyectos, Tareas, Reportes, etc.
│   ├── views.py        # Lógica de vistas
│   ├── admin.py        # Configuración del admin
│   └── templates/      # Plantillas HTML
├── media/              # Archivos subidos (no incluido en el repo)
├── manage.py
└── requirements.txt
```

## 👤 Admin

El panel de administración está disponible en `/admin/` con diseño mejorado usando **Unfold**.
