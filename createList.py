"""Crear Grupos de los Hermanos"""
import Lista_hermanos
import random
from datetime import datetime
import printDates
import dateCelebrations
import pandas as pd
from openpyxl.utils import get_column_letter


def createGruop(hermanos: dict):
    grupsPala1 = {"number":0, "value":0, "hermanos":[]}
    grupsPala2 = {"number":1, "value":0, "hermanos":[]}
    grupsPala3 = {"number":2, "value":0, "hermanos":[]}
    grupsPala4 = {"number":3,"value":0, "hermanos":[]}
    grupsPala5 = {"number":4,"value":0, "hermanos":[]}
    grupsPala6 = {"number":5,"value":0, "hermanos":[]}
    grupos = [grupsPala1, grupsPala2, grupsPala3, grupsPala4, grupsPala5, grupsPala6]
    sw = {0: True, 1: True, 2: True, 3: True, 4:True, 5:True}

    for nombre_hermano, sizehermano in hermanos.items():
      numbergroup = choiceGroup(sw)
      if numbergroup == None:
         grupos[0]['hermanos'].append(nombre_hermano) 

      else:
         grupos[numbergroup]['value'] = sizehermano + grupos[numbergroup]['value']
         grupos[numbergroup]['hermanos'].append(nombre_hermano) 
         if grupos[numbergroup]['value']>=5:
            sw[numbergroup] = False

    return grupos

def choiceGroup(sw: dict):
    numberlist = []
    for number, value in sw.items():
        if value:
            numberlist.append(number)
    if numberlist:
      numberFinal = random.choice(numberlist)
      return numberFinal
    else: 
     return None

def guardar_grupos_en_excel(grupos: list, dates: list, salida_excel: str = "Grupos_Hermanos.xlsx"):
    """
    Guarda una lista de grupos (lista de diccionarios) en un archivo Excel,
    donde cada grupo se escribe en una hoja distinta.

    Parámetros:
    -----------
    grupos : list
        Lista de diccionarios. Cada elemento debe tener las claves:
        'number' (int), 'value' (int), 'hermanos' (list[str])
    salida_excel : str
        Nombre del archivo Excel de salida (por defecto 'Grupos_Hermanos.xlsx')

    Retorna:
    --------
    bool : True si el proceso fue exitoso, False en caso de error
    """
    try:
        # Validar que realmente sea una lista
        if not isinstance(grupos, list):
            raise TypeError("El parámetro 'grupos' debe ser una lista.")

        # Crear el Excel con varias hojas (una por grupo)
        with pd.ExcelWriter(salida_excel, engine="openpyxl") as writer:
            today = datetime.today()
            year = today.year
            for grupo in grupos:
                numero = grupo.get("number", "SinNúmero")
                #print(numero)
                value = grupo.get("value", 0)
                hermanos = grupo.get("hermanos", [])

                # Crear DataFrame con los datos del grupo
                df = pd.DataFrame({
                    "Hermanos": hermanos,
                    "Fecha": f"{dates[numero]}/{year}",
                    "Total": value
                })

                # Guardar cada grupo en una hoja diferente
               # Guardar hoja
                if(numero<=3):
                   hoja_nombre = f"Palabra_{numero+1}"
                else:
                   hoja_nombre = f"Eucaristia_{numero-3}"
                df.to_excel(writer, sheet_name=hoja_nombre, index=False)

                # === Ajustar el ancho de columnas ===
                # Accedemos al workbook y worksheet
                worksheet = writer.sheets[hoja_nombre]
                for i, col in enumerate(df.columns, 1):
                    # Calcula el ancho según la longitud máxima del contenido
                    max_len = max(
                        df[col].astype(str).map(len).max(),
                        len(col)  # también cuenta el nombre de la columna
                    ) + 2  # margen extra
                    worksheet.column_dimensions[get_column_letter(i)].width = max_len


        print(f"✅ Archivo '{salida_excel}' creado correctamente con {len(grupos)} hojas.")
        return True

    except Exception as e:
        print(f"⚠️ Error al crear el Excel: {e}")
        return False



grupos = createGruop(Lista_hermanos.hermanos)
dates = dateCelebrations.datesCelebrationList()
guardar_grupos_en_excel(grupos, dates, 'Grupos_Celebraciones.xlsx')
