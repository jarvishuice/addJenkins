from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def saludar():
    return {"mensaje": "¡Hola, mundo!"}

@app.get("/saludar/{nombre}")
async def saludar_persona(nombre: str):
    
    return {"mensaje": f"¡Hola, {nombre}!"}