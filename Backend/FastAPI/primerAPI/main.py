
from typing import Optional
from enum import Enum

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#importamos status para verificar los estados http, se agregan en el decorador
#importar HTTPException para manejar estado de error HTTP, se eleva con Rise
from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, File, UploadFile

######
# En este curso se aprendio a leer (con formato), los Query, los Path, los Body http
# los Formularios, los header http, y cookies

# ademas utilizar el base model, para el modelo relacional
# Field, para validacion de los campos
# 
# por ultimo, utilizar las variables Optionales y clases enumeradas
######
# Path Parameters
# Query Parameters
# Request Body
# Forms
# Headers
# Cookies
# Files (File - Upload File(Filename - content type - File))

app = FastAPI()

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

#Se crea una clase base para el response model y el esquema
class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        lt=115
    )

    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

#se crea la clase que se pasara al response model
class PersonOut(PersonBase):
    pass

#se crea el esquema de persona
class Person(PersonBase):
    password: str = Field(...,min_length=8)
    

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Eduardo",
                "last_name": "Espinoza",
                "age": 35,
                "hair_color":"black",
                "is_married":True,
                "password": "12345678"
            }
        }


class Location(BaseModel):
    city: str
    state: str
    country: str    

class LoginOut(BaseModel):
    username: str = Field(..., max_length=20, example = "eduardoespinoza")
    message: str = Field(default="Login Successfully!")



@app.get(
    path = "/",
    status_code=status.HTTP_200_OK,
    #DEPRECATE UNA FUNCION. deprecate o rechazar, cuando una funcion es antigua
    #en vez de borrarla se le suele "drepecar", en swagger aparecera tachado
    deprecated=True
    )
def home():
    return {"Hello":"Wold"}

##Response Model -> para evitar enviar datos sensibles del usuario, se crea una clase
#con datos que se puedan enviar y se lo envia en al decorador como respinse model
#sin response model, devuelve el password, con response model no devuelve el password
@app.post(
    path = "/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    #el tag sirve para clasificar los metodos en Swagger, documentacion interactiva
    tags=["Person"],
    ##summry sirve para titular los metodos en Swagger, documentacion interactiva
    summary="Create person in the app"
    )
def create_person(person: Person = Body(...)):
    #hay que poner el docstream en este lugar para que Swagger lo entienda y explicar la funcion
    """
    -Titulo: Create Person

    -Descripcion: This path operation creates a peson in the app an save the information in the database
    
    -Parametros: Parameters:
        -Request body parameter:
            - **person: Person** -> a person model with first name, last name, age, hair color and marital status
    
    -Resultado: Returns a person model with first name, last name, age, hair color and marital status
    """
    return person

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Person"]
    )
def show_person(
    name: Optional[str] = Query(None, min_length=1,max_length=50,example="eduardo"),
    age: int = Query(...,example=35)    
):
    return {name: age}


persons = [1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Person"]
    )
def  show_person(

    person_id: int = Path(
        ...,
        gt=0,
        title="Id del usuario",
        description="This is the ID, It's required and greater than 0",
        example=15
        )
):
    if person_id not in persons:
        #si se verifica que el usuario no existe, se devolvera una excepcion http
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This persons doesn't exist!"
        )
    return {person_id: "It exist!"}

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Person"]
    )
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

    results = person.dict()
    results.update(location.dict())
    return results


@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)


@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=5,
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)

):
    return user_agent


#Status code principales:
#100 - information
#200 - ok
#--201 - created
#--204 - no content
#300 - Redirecting
#400 - Client error
#--404 - no exist - no existe la pagina
#--422 - validation error - el valor enviado no es correcto
#500 - Server Error


@app.post(
    path="/post_image"
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024,ndigits=2) 
    }