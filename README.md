

<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/hecho_en-Python-blue?style=flat-square&logo=python&logoColor=white">
  <img alt="Static Badge" src="https://img.shields.io/badge/compatible_con-Windows-magenta?style=flat-square">
  <img alt="Static Badge" src="https://img.shields.io/badge/compatible_con-Linux-green?style=flat-square">
  <img alt="Static Badge" src="https://img.shields.io/badge/multihilo-optimizado-orange?style=flat-square">
</p>

<h1 align="center">
  <img src="https://i.postimg.cc/R0Fw9cP8/logo.png" alt="WebRaptor Logo" width = 500>
  <br>WebRaptor
</h1>

**Herramienta avanzada de fuzzing web para descubrir rutas ocultas y subdominios no documentados**

## 🔍 Características principales

- ✅ **Fuzzing de directorios** - Descubre rutas ocultas mediante diccionarios personalizados
- 🌐 **Detección de subdominios** - Busca subdominios activos con el parámetro `-sd`
- ⚡ **Paralelización masiva** - Hasta 16 hilos concurrentes (configurable con `--hilos`)
- 🎨 **Salida inteligente** - Códigos de color según códigos HTTP
- 💾 **Auto-guardado** - Exporta resultados en formato TXT (`--guardar`)
- 🛡️ **Resistente a fallos** - Manejo de timeouts personalizables (`--timeout`)
- 📚 **Soporte multi-diccionario** - Combina varios diccionarios en una ejecución

## ⚙️ Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# Dar permisos de ejecución (Linux/Mac)
chmod +x WebRaptor.py


## 🚀 Uso básico

```bash
./WebRaptor.py --url https://ejemplo.com/ --dic diccionario.txt
```

## 📌 Parámetros avanzados

| Parámetro               | Descripción                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `--url URL`             | **Requerido**: URL objetivo (ej: `https://sitio.com`)                       |
| `--dic RUTA_DICC`       | **Requerido**: Diccionario(s) .txt (separar con comas para múltiples)       |
| `-sd, --subdom`         | Buscar subdominios en lugar de rutas                                        |
| `-g, --guardar`         | Guarda resultados en archivo TXT                                            |
| `-t, --timeout SEG`     | Tiempo máximo de espera por petición (default: 5s)                          |
| `--hilos N`             | Número de hilos concurrentes (default: 16)                                  |
| `-h, --ayuda`           | Muestra el menú de ayuda completo                                           |

## 🎯 Ejemplos de uso

**Buscar rutas con múltiples diccionarios:**
```bash
./WebRaptor.py --url https://ejemplo.com/ --dic common.txt,big.txt --guardar
```

**Buscar subdominios con 32 hilos:**
```bash
./WebRaptor.py --url https://ejemplo.com/ --dic subdomains.txt -sd --hilos 32
```

**Personalizar timeout y guardar resultados:**
```bash
./WebRaptor.py --url https://ejemplo.com/ --dic custom.txt -t 10 -g
```

## 🧠 Sistema de colores en resultados

| Color    | Significado                           | Códigos HTTP comunes |
|----------|---------------------------------------|----------------------|
| **Verde** | Ruta/subdominio accesible             | 200                 |
| **Amarillo** | Redirecciones o acceso restringido    | 301, 302, 401, 403 ...|


## 🖼️ Demostración

<h1 align="center">
  <img src="https://i.postimg.cc/v87xmnh0/demo-wr.png" alt="WebRaptor Logo" width = 700>
  <br>WebRaptor
</h1>

## 🏗️ Estructura de archivos

| Archivo         | Función                                                      |
|-----------------|-------------------------------------------------------------|
| `WebRaptor.py`  | Punto de entrada principal                                  |
| `clases.py`     | Lógica de fuzzing (Url, validación, threads)                |
| `funciones.py`  | Utilidades (lectura diccionarios, mostrar resultados)       |
| `params.py`     | Manejo de parámetros CLI                                    |
| `elementos.py`  | Recursos compartidos (user-agent, lock)                     |
| `status.json`   | Descripciones de códigos HTTP (personalizable)              |

