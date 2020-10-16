peticionSoap = None
reintentos = 0

while reintentos < 3:
        try:
            #peticion al Soap, si puedo recuperar la info, necesito cortar el ciclo del while
            if reintentos == 2:
                peticionSoap = {"Rut": 19134180, "dv": 3, "nombre": "jose"}

            if peticionSoap is not None:
                break
            raise Exception('Peticion Soap no es correcta')
        except Exception:
            reintentos += 1

print(reintentos,peticionSoap)