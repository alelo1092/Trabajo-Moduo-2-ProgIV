from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3307/diccionario")
Base=declarative_base()
class Palabras(Base):
    __tablename__ = 'Palabra'
    Palabra = Column(String(50),primary_key=True)
    Significado = Column(String(50))

Session = sessionmaker(engine)
session= Session()
Base.metadata.create_all(engine)

#Una vez creada la conexión creamos las funciones que aplicaran
#los requirimientos

def insertar(a,b):
    Nueva_Palabra = Palabras(Palabra=a,Significado=b)
    session.add(Nueva_Palabra)
    session.commit()

def mostrarDatos():
    Datos = session.query(Palabras).all()
    for elementos in Datos:
        print("Palabra Español es : " + elementos.Palabra + " su significado es : " + elementos.Significado)

def eliminar(PalabraE):
    session.query(Palabras).filter(Palabras.Palabra == PalabraE).delete()
    session.commit()

def editarSignificado(PalabraV,SignificadoN):
    Editar = session.query(Palabras).get(PalabraV)
    Editar.Significado = SignificadoN
    session.commit()

def significadopalabra(palabrasig):
    PalabraS = session.query(Palabras).filter_by(Palabra = palabrasig)
    for Datos in PalabraS:
        print("La palabra en español es : ",Datos.Palabra)
        print("La palabra en español es : ",Datos.Significado)



#Una vez definidas todas las funciones le damos inicio al programa con un bucle While


print("Inicio del Programa Diccionario Slang Panameño")

while True:
    Respuesta1 = input("Si desea agregar una Palabra al Diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta1 == "1":
        Respuesta11 = "1"
        while Respuesta11 == "1":
            a=input("Introduzca la Palabra : ")
            b = input ("Introduzca su significado : ")
            insertar(a,b)
            Respuesta11= input("Deseas agregar otra palabra?, Si (1), No (2) : ")
            
    Respuesta2 = input("\nSi desea editar el significado de una palabra del Diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta2 == "1":
        PalabraV = input("Introduzca la palabra que desee cambiarle el significado : ")
        SignificadoN = input("Introduzca el nuevo significado de la palabra anterior : ")
        editarSignificado(PalabraV,SignificadoN)

    Respuesta3 = input("\nSi desea ver todas los datos del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta3 == "1":
        mostrarDatos()
        
        
    Respuesta4 = input("\nSi desea ver algun significado de una palabra del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta4 == "1":
        palabrasig= input("\nIntroduzca la palabra que quiere saber su significado : ")
        significadopalabra(palabrasig)
        
    Respuesta5 = input("\nSi desea eliminar alguna palabra del diccionario presione 1, de lo contrario presione otro valor : ")
    if Respuesta5 == "1":
        PalabraE = input("\nIntroduzca la palabra que desea eliminar : ")
        eliminar(PalabraE)
    
    Respuesta6 = input("\nSi desea salir del programa presione 1, de lo contrario presione otro valor : ")
    if Respuesta6 == "1":
        break
    
print("Fin del Programa")


