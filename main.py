# Importação das bibliotecas necessárias
# fastapi para inicialização da Api
from fastapi import FastAPI, HTTPException, status
# uuid para geração de ids únicos para cada User
from uuid import UUID, uuid4

# Importação das classes de models.py
from models import Gender, Role, User, UpdateUser

# Instância FastApi
app = FastAPI()


# Banco de dados in-memory
db: list[User] = [
    User(
        id=uuid4(),
        first_name="Antonio",
        last_name="Vinicius",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="João",
        last_name="Emanuel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Hellen",
        last_name="Christina",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Ana",
        last_name="Leticia",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Gustavo",
        last_name="Sales",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]


# Endpoints
@app.get('/')
async def root():
    return {"Hello": "World"}


@app.get("/api/v1/users", status_code=status.HTTP_200_OK)
async def get_users():
    return db


@app.get("/api/v1/users/{id}", status_code=status.HTTP_200_OK)
async def get_user(id: UUID = uuid4):
    for user in db:
        if user.id == id:
            return user
    
    raise HTTPException(status_code=404, detail=f'Could not find user with id: {id}')


@app.post('/api/v1/users', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete('/api/v1/users/{id}', status_code=status.HTTP_200_OK)
async def delete_user(id: UUID = uuid4):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"user deleted"}
    raise HTTPException(status_code=404, detail=f'Delete user failed, id {id} not found.')


@app.put("/api/v1/users/{id}")
async def update_user(user_update: UpdateUser, id: UUID = uuid4):
    for user in db:
        if user.id == id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user.id
    raise HTTPException(status_code=404, detail=f'Could not find user with id: {id}')
