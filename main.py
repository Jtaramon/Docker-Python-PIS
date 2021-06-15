from fastapi import FastAPI

app = FastAPI()

@app.get("/datos")
def read_root():
    return {
    "Universidad": "UTPL",
    "Curso": "Procesos de Ingeniería de Software",
    "Alumno": "Juan Andres Ramon Zhigui",
    "Período": "Abr/Ago 2021",
    "Lenguaje de programación preferido": "JavaScript",
    "Aspiración PostGraduación": "Me interesa, lo que es el desarrolo y gestion de proyecto, asi que me capacitaria más, para poder conseguir un buen trabajo"
}
