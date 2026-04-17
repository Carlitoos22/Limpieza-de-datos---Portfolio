import pandas as pd

df = pd.read_excel("ejercicio_veterinaria_SUCIO.xlsx")

print("Filas y Columnas:", df.shape)
print()
print(df.head(10))


df = df.dropna(how="all")
print("Despues de sacar vacias:", df.shape)


df = df[~df['Mascota'].str.contains('---', na=False)]
df = df[df['Mascota'].notna()]
df['Mascota'] = df['Mascota'].str.strip().str.title()
print(df['Mascota'].unique())
df['Precio'] = df['Precio'].astype(str).str.replace('$', '', regex=False).str.replace('ARS', '', regex=False).str.replace(',', '', regex=False).str.strip()
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')
print(df['Precio'].head(10))

print("Total facturado:", df['Precio'].sum())
print(df.groupby('Mascota')['Precio'].count())

# --- Limpieza columna Fecha ---
df['Fecha'] = pd.to_datetime(df['Fecha'], dayfirst=True, errors='coerce')
df['Fecha'] = df['Fecha'].dt.strftime('%d/%m/%Y')
print("Fechas limpias:")
print(df['Fecha'].head(10))

df['Dueño'] = df['Dueño'].str.strip().str.title()
df['Tipo Animal'] = df['Tipo Animal'].str.strip().str.title()
df['Raza'] = df['Raza'].str.strip().str.title()
df['Servicio'] = df['Servicio'].str.strip().str.title()

# --- Reporte de nulos restantes ---
print("\nValores nulos por columna:")
print(df.isnull().sum())

# --- Estadisticas finales ---
print("\nRegistros limpios:", len(df))
print("Animales unicos:", df['Tipo Animal'].nunique())
print("Precio promedio:", round(df['Precio'].mean(), 2))
print("Precio maximo:", df['Precio'].max())
print("Precio minimo:", df['Precio'].min())

df.to_excel('Datos_Ordenados_Veterinaria.xlsx', index=False)
print("\nArchivo exportado: Datos_Ordenados_Veterinaria.xlsx")