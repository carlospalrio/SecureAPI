
# Link Video: https://monlaues-my.sharepoint.com/:v:/g/personal/carlospalrio_campus_monlau_com/EaFe53gcLbFEsgv71QBU160B66fF9Cs5T6Yy9RWSNGvMGA?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=wBb9HO







import os
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware

# Obtener la clave secreta de una variable de entorno
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "clave_por_defecto")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

app = FastAPI()

# Habilitar CORS para evitar problemas de conexión
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para crear un token JWT
def create_jwt(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Endpoint para obtener un token (simulación de login)
@app.post("/token")
async def login():
    try:
        system_user = os.getlogin()  # Obtener el usuario del sistema operativo
    except Exception:
        system_user = "unknown_user"  # Fallback si no se puede obtener el usuario

    user_data = {"sub": system_user}  # Incluye el usuario del sistema operativo
    token = create_jwt(user_data, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": token, "token_type": "bearer"}

# Endpoint protegido que requiere un JWT válido
@app.get("/protected")
async def protected(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Acceso permitido", "user": payload["sub"]}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
