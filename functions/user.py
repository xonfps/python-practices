from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = 'Isaque Souza'

external_data = {
    'id': '157'
}

user = User(**external_data)

##print(user.id)
print(user.dict())
