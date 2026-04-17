import pandas as pd
from gestion_ventas import cargar_ventas

def analizar_ventas():
    # leer las ventas desde el archivo csv utilizando la función cargar_ventas
    #Extraer el dataframe de ventas
    df = cargar_ventas("ventas.csv")
    
    #Transformar
    if df is None:
        print("No se pudieron cargar las ventas para el análisis.")
        return
    
    print ( "\n -- Análisis de Ventas --" )
    
    #crear columnas 
    df["Ingresos"] = df["Cantidad"] * df["Precio"]
    
    total_ingresos = df["Ingresos"].sum()
    print(f"Total de ingresos: ${total_ingresos:.2f}")
    
    #producto más vendido
    producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()
    print(f"Producto más vendido: {producto_mas_vendido}")
    
    #CLIENTE CON MÁS COMPRAS
    cliente_top = df.groupby("Cliente")["Ingresos"].sum().idxmax()
    print(f"Cliente con más compras: {cliente_top}")
    
    print("\n --- Ventas Diarias ---")
    print(df.groupby("Fecha")["Ingresos"].sum().to_string())
if __name__ == "__main__":
    analizar_ventas()