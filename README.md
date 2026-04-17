#  Limpieza de datos — Veterinaria Luciana

Proyecto de limpieza, normalización y análisis de datos reales de una veterinaria ficticia usando **Python** y **pandas**.

---

## 📋 Descripción

El archivo original (`ejercicio_veterinaria_SUCIO.xlsx`) contenía datos inconsistentes típicos de registros ingresados manualmente: nombres en mayúsculas y minúsculas mezcladas, precios con símbolos de moneda (`$`, `ARS`), filas completamente vacías, valores nulos y separadores de miles incorrectos.

Este proyecto aplica un pipeline de limpieza completo y exporta un archivo Excel prolijo y listo para análisis.

---

##  ¿Qué hace el script?

| Paso | Acción |
|------|--------|
| 1 | Lee el archivo Excel sucio con `pandas` |
| 2 | Elimina filas completamente vacías (`dropna(how="all")`) |
| 3 | Filtra filas con valores inválidos en la columna `Mascota` (ej: `---`) |
| 4 | Elimina filas donde `Mascota` es nula |
| 5 | Normaliza texto en `Mascota`, `Dueño`, `Tipo Animal` y `Raza` con `.str.strip().str.title()` |
| 6 | Limpia la columna `Precio`: elimina `$`, `ARS`, comas y espacios, luego convierte a numérico |
| 7 | Parsea fechas en múltiples formatos a formato uniforme `DD/MM/YYYY` |
| 8 | Genera estadísticas finales (total facturado, precio promedio, máximo y mínimo) |
| 9 | Exporta el resultado limpio a `Datos_Ordenados_Veterinaria.xlsx` |

---

##  Estructura del proyecto

```
veterinaria-luciana/
│
├── ejercicio_veterinaria_SUCIO.xlsx      # Dataset original (datos sucios)
├── Datos_Ordenados_Veterinaria.xlsx      # Dataset limpio exportado
├── limpieza.py                           # Script principal de limpieza
└── README.md
```

---

##  Problemas encontrados en los datos originales

- **Nombres de mascotas** con formatos mixtos: `LUNA`, `luna`, `Luna`
- **Columna Precio** con múltiples formatos: `$14,446`, `ARS 18509`, `$5822`, `10086.79`
- **Filas completamente vacías** entre registros
- **Filas con `---`** usadas como separadores visuales en `Mascota`
- **Dueños y razas** con espacios extra y capitalización inconsistente
- **Tipo Animal** mezclado: `perro`, `Perro`, `GATO`, `gato`
- **Fechas** en 4 formatos distintos: `28/07/25`, `04/01/2025`, `2025-03-11`, `15-01-2025`

---

##  Resultado final

El archivo limpio `Datos_Ordenados_Veterinaria.xlsx` contiene todos los registros normalizados con formato profesional.

### Columnas del dataset limpio

| Columna | Tipo | Descripción |
|---------|------|-------------|
| `Mascota` | Texto | Nombre de la mascota (Title Case) |
| `Tipo Animal` | Texto | Especie (Perro, Gato, Loro, Conejo) |
| `Raza` | Texto | Raza del animal |
| `Dueño` | Texto | Nombre del propietario |
| `Servicio` | Texto | Tipo de atención veterinaria |
| `Precio` | Numérico | Precio en pesos argentinos |
| `Fecha` | Fecha | Fecha de la atención (DD/MM/YYYY) |

---

##  Estadísticas del dataset

- **Registros originales**: 127 filas (con basura y duplicados)
- **Registros limpios**: ~115 atenciones válidas
- **Mascotas únicas**: 10 (Luna, Milo, Bella, Coco, Thor, Max, Nina, Simba, Lola, Rocky)
- **Tipos de animales**: Perro, Gato, Loro, Conejo
- **Servicios registrados**: Consulta general, Cirugía menor, Radiografía, Ecografía, Desparasitación, Vacunación, Limpieza dental, Castración, Análisis de sangre, Control post-operatorio
- **Período**: Enero 2025 – Diciembre 2025
- **Total facturado**: $2,138,217 ARS

---

##  Tecnologías utilizadas

- **Python 3.x**
- **pandas** — limpieza y manipulación de datos
- **openpyxl** — exportación con formato a Excel

---

##  Instalación y uso

```bash
# Clonar el repositorio
git clone https://github.com/Carlitoos22/Limpieza-de-datos---Portfolio.git
cd Limpieza-de-datos---Portfolio

# Instalar dependencias
pip install pandas openpyxl

# Ejecutar el script de limpieza
python limpieza.py
```

El archivo de salida se generará en el mismo directorio como `Datos_Ordenados_Veterinaria.xlsx`.

---

##  Contacto

Si necesitás un servicio de limpieza o análisis de datos, podés contactarme:

- **GitHub**: [Carlitoos22](https://github.com/Carlitoos22)
- **Fiverr**: *(próximamente)*

---

##  Contribuciones

Este es un proyecto de práctica educativa. Si encontrás errores o querés proponer mejoras al pipeline de limpieza, podés abrir un issue o un pull request.

---

*Proyecto realizado con fines educativos — Análisis de datos con Python y pandas*
