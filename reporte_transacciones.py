import sys
import csv

# Convierte un monto de dinero real (moneda) a centavos
def convertir_a_centavos(monto):
    return int(round(monto * 100))

# Convierte un monto de centavos a dinero real (moneda)
def convertir_a_moneda(centavos):
    return centavos / 100

#Funcion para procesar el contenido del archivo csv
def procesar_transacciones(archivo):

    # Inicializacion de variables
    total_debitos_cent = 0 # Total acumulado de los montos debito en centavos
    total_creditos_cent = 0 # Total acumulado de los montos credito en centavos
    monto_mayor_cent = 0 # Monto mayor en centavos
    cantidad_creditos = 0
    cantidad_debitos = 0
    id_monto_mayor = None

    # Lectura del archivo csv
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        lector = csv.reader(csvfile)
        next(lector) # Se salta la primera fila, el encabezado

        # Extraccion de informacion fila por fila
        for fila in lector:
            id = fila[0]
            tipo = fila[1]
            monto = float(fila[2])
            monto_centavos = convertir_a_centavos(monto) # Se convierte el monto a centavos para evitar errores de precision con decimales

            # Suma de montos en centavos por tipo de transaccion
            if tipo == 'Crédito':
                total_creditos_cent += monto_centavos
                cantidad_creditos += 1 # Conteo de transacciones por tipo
            elif tipo == 'Débito':
                total_debitos_cent += monto_centavos # Conteo de transacciones por tipo
                cantidad_debitos += 1

            # Calculo de transaccion de monto mayor
            if monto_centavos > monto_mayor_cent:
                monto_mayor_cent = monto_centavos
                id_monto_mayor = id

    # Mostrar reporte de resultados
    print("Reporte de Transacciones")
    print("-----------------------------------------------------")
    print("Balance Final: ", convertir_a_moneda(total_creditos_cent-total_debitos_cent)) # Se convierte el balance final en dinero real debido a que esta en centavos
    print("Transacción de Mayor Monto: ID ",id_monto_mayor," - ", convertir_a_moneda(monto_mayor_cent)) # Se convierte el monto mayor en dinero real debido a que esta en centavos
    print("Conteo de Transacciones: Crédito: ", cantidad_creditos, " Débito: ", cantidad_debitos) 

if __name__ == "__main__":
    #Se verifica que se pase el archivo csv como argumento
    if len(sys.argv) < 2:
        print("Uso Windows: python reporte_transacciones.py data.csv")
        print("Uso Linux: python3 reporte_transacciones.py data.csv")
    else:
        archivo = sys.argv[1]
        procesar_transacciones(archivo)#Se llama a la funcion para procesar el archivo