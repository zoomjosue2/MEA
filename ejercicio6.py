#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 60
# 
# Josué Antonio Isaac García Barrera - 24918
# Ejercicio individual 6
# 10/05/24
#==========================================================

#Se importan las librerias que necesitaremos
import pandas as pd
import matplotlib.pyplot as plt

#Se lee el archivo csv
vuelos = pd.read_csv("flights50.csv")

#Se crea un diccionario con las definiciones de cada columna
definiciones = {'YEAR': 'Dice el año en el que sucedio el vuelo', 'MONTH': 'Dice el mes en el que sucedio el vuelo', 'DAY':'Dice el día del mes en el cual sucedio el vuelo', 'DAY_OF_WEEK':'Dice el día de la semana en la cual sucedio el vuelo','AIRLINE':'Identifica la aeroline del vuelo','FLIGHT_NUMBER':'Indica el número que identifica al vuelo','TAIL_NUMBER':'Indica el número que identifica el avión','ORIGIN_AIRPORT':'El nombre del aeropuerto de donde sale el vuelo','DESTINATION_AIRPORT':'El nombre del aeropuerto a donde tenia que llegar el vuelo','SCHEDULED_DEPARTURE':'Indica el horario planeado de salida','DEPARTURE_DELAY':'Indica el delay que tuvo la salda del vuelo','TAXI_OUT':'Indica el tiempo que pasa entre la salida del aeropuerto y el inivio del viaje','WHEELS_OFF':'Indica el tiempo que el avión tarda en levantar las rueda del suelo','SCHEDULED_TIME':'Indica el tiempo planeado que deberia de durar el vuelo','AIR_TIME':'Indica la duración en que el avión paso en el aire','DISTANCE':'Indica la distancia entre los dos aeropuertos','WHEELS_ON':'Indica el tiempo que se tarda en que las ruedas del avión toquen el suelo','TAXI_IN':'Indica el tiempo que pasa entre el inicio del viaje y la llegada al aeropuerto del destino','SCHEDULED_ARRIVAL':'Indica el tiempo planeado para la llegada','ARRIVAL_TIME':'Indica el tiempo que tarda el vuelo entero en llegar al destino','ARRIVAL_DELAY':'Indica el tiempo que se llego a atrasar el tiempo de llegada del vuelo','DIVERTED':'Indica que el avión aterrizó fuera de lo previsto','CANCELLED':'Indica si algún vuelo fue cancelado'}

#Se crea la nueva columna para poder decidir si el vuelo salio a tiempo o se retraso
vuelos['TIEMPO_VUELO'] = vuelos.apply(lambda row: 'A tiempo' if row['DEPARTURE_DELAY'] <= 0 else 'Retrasado', axis=1)

#Se crea la variable para ver si el vuelo salio a tiempo o tarde
def despegue(DEPARTURE_DELAY):
    DEPARTURE_DELAY = int(DEPARTURE_DELAY)
    if DEPARTURE_DELAY <= 0:
        return "El avión despegó a tiempo"
    else: 
        return "El avión se atrasó"

#variable para elegir la opción del menú
opcion = ""

#Se hace el menú
while opcion != "12":
    print("""Elige una de las opciones del menú indicando el número de la función que quieres ejecutar
    (1) Tamaño de los datos
    (2) Cuanto fue la distancia recorrida
    (3) El día de la semana que se vuela más
    (4) Cual es el top 5 de aeropuertos
    (5) Estado de tiempo del avión
    (6) Gráfica de porcentajes de los vuelos que salieron a tiempo o retrasados
    (7) Donde pasan más tiempo los viajeros TAXI_IN o TAXI_OUT  
    (8) Aerolinea que más vuelos cancela
    (9) Mes que más pasa en el aire
    (10) Crear csv con los 1500 vuelos más cortos
    (11) Gráfica promedio de horas de salida y llegada por día
    (12) Salir"""    )
    opcion = input("\nElija una opción: ")
    

    if opcion == "1":
        #Se cuenta cuantas filas hay en el csv
        filas = len(vuelos)
        #Se cuenta cuantas columnas hay en el csv
        contador_columna = len(vuelos.columns)
        #Se imprimen las cantidades
        print(f"La cantidad de columnas que tiene: {contador_columna}")
        print(f"La cantidad de filas que tiene: {filas}\n")
        #Se vuelven las columnas una lista
        columnas = vuelos.columns.tolist()
        #Se imprimen las columnas
        print("Columnas")
        #Se imprimen las definiciones de cada columna
        for columna in columnas:
            if columna in definiciones:
                print(f"- {columna}: {definiciones[columna]}\n")

    elif opcion == "2":
        #Se suma todos los valores de la columna DISTANCE
        print(f"La distancia recorrida en total fue: {vuelos['DISTANCE'].sum()}\n")
   
    elif opcion == "3":
        #Se cuentan cuantos valores hay en la columna DAY_OF_WEEK
        diafrecuente = vuelos['DAY_OF_WEEK'].value_counts()
        #Se elimina el header y se imprime solo el dia semana que se vuela más
        print(f"El día de la semana que se suele volar más es el : {diafrecuente.head(1).to_string(header=False)} veces se viajo este día\n")
    
    elif opcion == "4":
        #Se cuentan cuantos valores hay en la columna ORIGIN_AIRPORT
        aeropuertos = vuelos['ORIGIN_AIRPORT'].value_counts()
        #Se elimina el header y se imrpime los 5 aeropuertos en donde salen más vuelos
        print(f"Los 5 aeropuertos en los que más vuelos salen son: \n{aeropuertos.head(5).to_string(header=False)}\n")
    
    elif opcion == "5":
        #Se le pide que escriba el delay que hubo
        delay = input("Escibre los minutos en los que el avión se atraso (coloca un número negativo si salio antes de la hora y positivo si se atrasó): ")
        #Se llama a la función
        print(despegue(delay))
        print("\n")

    elif opcion == "6":
        #Se responde a la pregunta
        print("Para crear la nueva columna para determinar si los vuelos salieron a tiempos o no el tiempo de ejecución fue practicamente nada, lo que quiere decir que pandas tiene muy buena eficacia a la hora de tratar con archivos muy pesados")
        #Se cuentan cuantos valores de a tiempo y retraso hay en la columna que se creo       
        conteo = vuelos['TIEMPO_VUELO'].value_counts()
        #Se crea la grafica
        plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=90)
        #Se pone el titulo que aparecera
        plt.title('Porcentaje de vuelos que llegaron a tiempo vs retrasados')
        #Se pone para lograr que la gráfica sea circular
        plt.axis('equal')  
        #Se muestra la gráfica
        plt.show()

    elif opcion == "7":
        #Se saca el promedio de TAXI_IN
        promedioin = vuelos['TAXI_IN'].mean()
        #Se saca el promedio de TAXI_OUT
        promedioout = vuelos['TAXI_OUT'].mean()
        #Se imprime lo que significa la columna de cada uno
        print("\n(TAXI_IN): El tiempo transcurrido entre el inicio del viaje y la llegada a la puerta del aeropuerto de destino es.")
        print("(TAXI_OUT): El tiempo transcurrido entre la salida de la puerta del aeropuerto de origen y el inicio del viaje.")
        #Se crea un sistema para que dependiendo del porcentaje que me de se muestre un mensaje o otro para saber en que pasan más tiempo 
        if promedioin > promedioout:
            print("Los viajeros pasan más tiempo entre el incio del viaje y la llegada a la puerta del aeropuerto del destino es mayor")
        elif promedioout > promedioin:
            print("Los viajeros pasa más tiempo entre la salida de la puerta del aeropuerto de origen y el inicio del viaje.\n") 
    
    elif opcion == "8":
        #Se agrupan las dos columas y se cuenta la cantidad de valores que son iguales a 1 es decir donde se cancelaron los vuelos
        mayorcancelos = vuelos[vuelos['CANCELLED'] == 1].groupby('AIRLINE').size()
        #Se ordena de mayor a menor y se saca solo el primer dato
        mayorcancelos_final = mayorcancelos.sort_values(ascending = False).head(1)
        #Se imprime la aerolinea donde se cancelas más vuelos y se elimina el header
        print(f"\nLa aerolinea que más vuelos cancela es: {mayorcancelos_final.to_string(header=False)} veces \n")
    
    elif opcion == "9":
        #Se agrupan las dos columnas y se suma la cantidad de tiempo que se estuvo en el aire durante cada meses
        mesvstiempo = vuelos.groupby('MONTH')['AIR_TIME'].sum()
        #Se imprime el mes que más tiempo se pasa en el aire y se quita el header
        print(f"\nEl mes que más tiempo se pasa en el aire es: {mesvstiempo.to_string(header=False)} tiempo total\n")
        #Se crea la gráfica de barras
        mesvstiempo.plot(kind="bar", title="Cantidad de tiempo en el aire por mes", grid=True, stacked=False, rot=0)
        #Se coloca en el eje x que diga los meses
        plt.xlabel('Meses')
        #Se coloca que en el eje y sea el tiempo
        plt.ylabel('Tiempo')
        #Se pone un limite de intervalo entre cada marca en el eje y
        plt.ylim(0, 100000)
        #Se muestra la gráfica
        plt.show()
        #Se responden a las preguntas 
        print("Se utilizo una gráfica de bara por que era la más adecuada, pero al ser un número extremadamente grande lo que succede es que la gráfica no es suficiente para mostrarla completa.")
        print("Se utilizaron opciones como kind, title, grid, stacked y rot, tambien se utilizo una función lim para indicarle a la grafica los intervalos en los valores y, pero este tiene un limite.\n")

    elif opcion == "10":
        #Se le pregunta al usuario si quiere crear un archivo csv 
        pregunta = input(print("\n¿Quieres crear un arhcivo csv con los 1,500 vuelos más cortos si/no: ")).lower()

        #Si el usuario responde si se crea el archivo
        if pregunta == "si":
            #Se utiliza la función .nsmallest para decir que nos de los 1500 valores minimos de la columna ELAPSED_TIME
            vueloscortos = vuelos.nsmallest(1500,'ELAPSED_TIME')
            #Se crea el csv
            vueloscortos.to_csv('vuelos_con_menor_duracion.csv', index=False)
            #Se imprime un mensaje para que el usuario sepa que se creo el archivo
            print("Se creo con exito el archivo csv.\n")

        #Si el usuario responde no, solo le avisa que no se creara nada
        elif pregunta == "no":
            #Se imprime un mensaje para que el usuario sepa que no se creara nada
            print("No se creara ningun archivo csv nuevo\n")

        #Se pone un else para que si el usuario pone algo más que si o no no de error el programa
        else:
            print("Ingrese una opción valida.")
    
    elif opcion == "11":
        #Se agrupan las columnas y se saca el promedio del tiempo de salida por cada día
        promediohoras_salida = vuelos.groupby('DAY_OF_WEEK')['DEPARTURE_TIME'].mean()
        #Se agrupan las columnas y se saca el promedio del tiempo de llegada por cada día
        promediohoras_llegada = vuelos.groupby('DAY_OF_WEEK')['ARRIVAL_TIME'].mean()
        #Se crea un plot para cada una de los promedios
        promediohoras_salida.plot(kind="line", title="Promedio de salida y llegada por día de la semana", grid=True, stacked=False, rot=0)
        promediohoras_llegada.plot(kind="line", title="Promedio de salida y llegada por día de la semana", grid=True, stacked=False, rot=0)
        #En el eje x saldran los días
        plt.xlabel('Días')
        #En el eje y saldran los promedios
        plt.ylabel('Promedio')
        #Se muestra la gráfica
        plt.show()

    elif opcion == "12":
        #Se imprime un mensaje para indicar que el programa terminó
        print("El programa terminó.")
    
    else:
        #Por si el usuario elige una opcion no valida le pide que coloqué otra opción
        print("Elija una opción correcta")
    
#Se guarda la columna que se creo
vuelos.to_csv('flights50.csv', index= False)
        