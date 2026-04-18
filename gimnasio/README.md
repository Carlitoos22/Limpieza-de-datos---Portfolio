#  Limpieza de Datos — Gimnasio

> Script de limpieza, normalización y análisis de datos para la gestión de socios de un gimnasio. Transforma un Excel con datos sucios en un archivo limpio y un reporte ejecutivo con los KPIs del negocio.

---

##  Tabla de Contenidos

- [Descripción](#-descripción)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Proceso de Limpieza](#-proceso-de-limpieza)
- [Resultados](#-resultados)
- [Notas Técnicas](#-notas-técnicas)

---

##  Descripción

Este script realiza un pipeline completo de limpieza y análisis sobre el archivo de gestión del gimnasio. El proceso está dividido en tres niveles de complejidad progresiva:

| Nivel | Descripción |
|-------|-------------|
| **Nivel 1** | Limpieza base: filas vacías, nombres, actividades, montos y fechas |
| **Nivel 2** | Limpieza avanzada: emails, estados, métodos de pago y duplicados |
| **Nivel 3** | Reportes: KPIs de facturación, socios y métodos de pago |

---

##  Requisitos

- Python 3.8+
- pip

### Dependencias

```txt
pandas>=1.3.0
numpy>=1.20.0
openpyxl>=3.0.0
```

---

##  Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Carlitoos22/limpieza-gimnasio.git
cd limpieza-gimnasio

# 2. (Opcional) Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## ▶️ Uso

Colocá el archivo `ejercicio_gimnasio_SUCIO.xlsx` en la raíz del proyecto y ejecutá:

```bash
python3 limpieza_gimnasio.py
```

### Salida esperada en consola

```
✅ Archivo guardado: gimnasio_LIMPIO.xlsx
   Registros limpios: 174
   Total facturado:   $2,326,137.45
   Activos / Inactivos / Suspendidos: 54 / 72 / 48
   Actividad top: Musculación ($829,404.57)
   Método más usado: Transferencia (50 usos)
```

El archivo `gimnasio_LIMPIO.xlsx` se genera con dos hojas:

- **Datos Limpios** — todos los registros normalizados con formato de tabla
- **Resumen Ejecutivo** — dashboard con KPIs del negocio

---

##  Estructura del Proyecto

```
limpieza-gimnasio/
│
├── limpieza_gimnasio.py          # Script principal
├── ejercicio_gimnasio_SUCIO.xlsx # Archivo de entrada (no incluido en el repo)
├── gimnasio_LIMPIO.xlsx          # Archivo de salida (generado al ejecutar)
├── requirements.txt              # Dependencias
└── README.md                     # Este archivo
```

---

##  Proceso de Limpieza

### Nivel 1 — Limpieza Base

- Eliminación de filas completamente vacías o con valores de basura
- Normalización de nombres de socios a **Title Case**
- Unificación de actividades con distintas mayúsculas/tildes

  ```
  musculacion  →  Musculación
  crossfit     →  CrossFit
  pilates      →  Pilates
  ```

- Limpieza de montos: remoción de `$`, comas y espacios, conversión a `float`
- Normalización de fechas a `dd/mm/yyyy`, incluyendo años cortos

  ```
  19/07/25  →  19/07/2025
  2025-08-11  →  11/08/2025
  ```

### Nivel 2 — Limpieza Avanzada

- Emails normalizados a **minúsculas**
- Valores inválidos en emails reemplazados por `NaN`

  ```
  "N/A"  →  NaN
  "-"    →  NaN
  ```

- Montos con texto convertidos a `NaN`

  ```
  "PENDIENTE"  →  NaN
  "gratis"     →  NaN
  ```

- Métodos de pago unificados

  ```
  MP / mercadopago / MERCADO PAGO  →  Mercado Pago
  transf / TRANSFERENCIA           →  Transferencia
  tarjeta / tarjeta debito         →  Tarjeta
  ```

- Estados normalizados

  ```
  ACTIVO / activo / Activo  →  Activo
  ```

- Eliminación de filas duplicadas exactas con `.drop_duplicates()`

### Nivel 3 — Reportes

- Total facturado (suma de montos válidos)
- Conteo de socios por estado (Activo / Inactivo / Suspendido)
- Facturación total por actividad, ordenada de mayor a menor
- Método de pago más utilizado

---

##  Resultados

| Indicador | Valor |
|-----------|-------|
| Registros originales | 192 |
| Registros limpios | 174 |
| Total facturado | $2,326,137.45 |
| Socios activos | 54 |
| Socios inactivos | 72 |
| Socios suspendidos | 48 |
| Actividad más rentable | Musculación ($829,404.57) |
| Método de pago más usado | Transferencia (50 usos) |

---

##  Notas Técnicas

- **Montos pendientes**: Los valores `PENDIENTE` y `gratis` se conservan como `NaN` para no distorsionar el total facturado. Estos registros quedan visibles en el archivo pero no se suman al total.

- **Emails en blanco**: Las celdas vacías en la columna Email corresponden a registros donde el dato no existía en la fuente original (`NaN`, `"N/A"` o `"-"`). No es un error del script.

- **Fechas**: La normalización cubre múltiples formatos (`YYYY-MM-DD`, `DD/MM/YYYY`, `DD-MM-YYYY`) y convierte años cortos (`/25` → `/2025`) antes del parseo.

- **Duplicados**: `.drop_duplicates()` compara filas completas **después** de la limpieza, por lo que variantes sucias del mismo registro (ej: `"ACTIVO"` vs `"activo"`) quedan consolidadas en una sola fila.

---

## 📦 requirements.txt

```txt
pandas>=1.3.0
numpy>=1.20.0
openpyxl>=3.0.0
```