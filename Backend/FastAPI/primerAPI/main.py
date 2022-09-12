#Python
##todas la verificaciones se realizan desde el localhost/docs (swagger)
#http://127.0.0.1:8000/docs
#ahi se pueden realizar pruebas manuales
#si se desea automatizar las pruebas, se crearan clases nuevas dentro de las clases declaradas
#ver mas abajo en la Clase Person

#importaciones de python para utilizar declaracion de variables
#Optional para cargar variables opcionales
#Enum, para poder generar listas enumerables
from typing import Optional
from enum import Enum

#Pydantic
#importacion de pydantic para utilizar el modelo relacional
#importar Filed para el modelo (formato y validacion) 
from pydantic import BaseModel
from pydantic import Field

#FastAPI
#importacion de FastApi, para ejecutar una aplicacion y poder utilizar los decoradores en los paths
#importacion de Body, para dar formato del body html (formato y validacion)
#importacion del query, para extraer la infomacion del (path) query parameter (formato y validacion)
#importacion del Path, para extraer la informacon del path parameter (formato y validacion)
from fastapi import FastAPI
from fastapi import Body, Query, Path

#se crea una instancia app de la clase FastAPI
app = FastAPI()

#Models

#creando enumeradores
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

#se crea la clase Person que hereda de la clase BaseModel
class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        #para los ejemplos de swagger se pueden crear como clases, ver lineas abajo
        #pero tambien se puede agregar el elemento example
        #a mi gusto, es mejor crear la clase, ver lineas abajo
        #example = "Eduardo"
        )
    last_name: str
    age: int = Field(
        ...,
        gt=0,
        lt=115
    )
    #sin listas enumerables
    #hair_color: Optional[str] = None
    #is_married: Optional[bool] = None
    #con listas enumarables
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

    #Se puede crear una clase interna, dentro de la clase Person, solo para pruebas
    #swagger cargara el ejemplo y ya no tendremos que estar rellenando manualmente
    #se puede generar todos los ejemplos que necesitemos
    #swagger no soporta ciertas cosas mas modernas como el ingreso del doble JSON, ejemplo del PUT
    class Config:
        schema_extra = {
            "example": {
                "first_name": "Eduardo",
                "last_name": "Espinoza",
                "age": 35,
                "hair_color":"black",
                "is_married":True
            }
        }



#se crea la clase Location que se hereda de la clase BaseModel
class Location(BaseModel):
    city: str
    state: str
    country: str    

#PATH OPERATION DECORATOR
#se crea el decorador de la app, metodo get
@app.get("/")
#PATH OPERATION FUNCTION
#Al solitar un GET al servidor con path /, se devuelve la funcion home
#esta funcion retorna el JSON {"Hello":"Wold"}
def home():
    return {"Hello":"Wold"}

#se crea el decorador de la app, metodo post
@app.post("/person/new")
#Body(...) se le pasa tres puntos para indicar que person es obligatorio
#pero ya no es obligatorio agregarlo, se deja vacio y es obligatorio por defecto
#al solicitar el post al servidor, la funcion create_person solicita un body
#se solicita una person de la clase Person, que sera igual Body(formato) 
def create_person(person: Person = Body()):
#se responde con la misma informacion que recibe, person
    return person

#se crea el decorador de la app, metodo get, para path query
@app.get("/person/detail")
#al solicitar el get al servidor, se solicita el path query, con informacion
#name, opcional que sera igual a Query(formato)
#age, obligatorio que sera igual a Query(formato)
def show_person(
    #validaciones para strings en Query: min_length,max_length, regex(exp regulares)
    #para los ejemplos de swagger, tambien se puede definir los valores para el path
    name: Optional[str] = Query(None, min_length=1,max_length=50,example="eduardo"),
    #el año se desea que sea obligatorio, se podria indicar Query(...) pero ya no es necesario
    #validaciones para integer en Query: ge(>=), le(<=), gt(>0), lt(<)
    #para los ejemplos de swagger, tambien se puede definir los valores para el path
    age: int = Query(...,example=35)
    #en query se puede utilzar parametros como title y description
    
):
#Se devolvera el JSON {name: age}
    return {name: age}

#se crea otro path con la misma ruta q el anterior, pero para path parameter
# verificar si se ejecutara el get anterior o este get (segun comentarios el primero, segun profe el segundo)
@app.get("/person/detail/{person_id}")
def  show_person(
#se solicita al path entrante una variable que tiene que ser del mismo nombre del definido adelante    
#se puede el titulo y la descripcion
    person_id: int = Path(
        ...,
        gt=0,
        title="Id del usuario",
        description="This is the ID, It's required and greater than 0",
        #para los ejemplos de swagger, tambien se puede definir los valores para el path
        example=15
        )
):
#se devuelve el JSON {person_id: "It exist!"}
    return {person_id: "It exist!"}

#se crea el decorador de la app, metodo put(actualizar), para path parameter
@app.put("/person/{person_id}")
#esta vez se solicita la variable del path y el contenido del body
#se hace una modificacion para se solicite dos JSON (las llaves son las variables) dentro de otro
def update_person(
    person_id: int = Path(
        ...,
        tittle = "Person ID",
        description="This is the person ID",
        gt = 0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
#se devuelve la misma inforacion que se recibio del body, FASTAPI se encarga de convertilo en diccionario
#    return person
#pero para devolver los dos JSON que queremos, tenemos que juntarlos en un solo diccionario
#se debe de hacer de manera explicita
    results = person.dict()
    results.update(location.dict())
#se podria haber juntado la siguiente manera, pero FASTAPI no soporta esa sintanxis aun
# person.dict()&location.dict()    
    return results

#Tipos de datos clasicos
#str, int, float, bool
#tipos de datos especiales
#Enum
#HttpUrl: www.platzi.com / http://miproject.com
#FilePath: c:/windows/system/archivo.txt
#DirectoryPath /windows/system/archivo.txt
#EmailStr
#Payment Card Number
#IPvAnyAddress
#NegativeFloat
#PositiveFloat
#NegativeInt
#PositiveInt
#https://pydantic-docs.helpmanual.io/usage/types/#pydantic-types
