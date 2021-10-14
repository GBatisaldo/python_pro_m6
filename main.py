from fastapi import FastAPI 

from pydantic import BaseModel

app = FastAPI()


class Value(BaseModel):
    valor1: int
    valor2: int
    operador: str

    def operation(self):
        if self.operador == '+':
            result = self.valor1 + self.valor2
            return {
                'resultado': result
            }
        elif self.operador == '-':
            result = self.valor1 - self.valor2
            return {
                'resultado': result
            }
        elif self.operador == '*':
            result = self.valor1 * self.valor2
            return {
                'resultado': result
            }
        elif self.operador == '/':
            result = self.valor1 / self.valor2 
            return {
               "resultado": result
            }

# Rota Raiz
@app.get("/")
def raiz():
    return{"ola":"Mundo"}


@app.post("/operador/")
def operacao(value:Value):
    return value.operation()