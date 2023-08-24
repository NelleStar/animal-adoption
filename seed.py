from app import app
from models import db, Pet

db.drop_all()
db.create_all()

pet1 = Pet(name='Timon', species='Meerkat', photo_url='https://images.unsplash.com/photo-1609695001873-bf16717ba9db?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8ZGlzbmV5JTIwYW5pbWFsc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60', age=3, notes='Sarcastic', available=True)
pet2 = Pet(name='Zazu', species='Hornbill', photo_url='https://images.unsplash.com/photo-1565416593273-7d06a92154b0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGhvcm5iaWxsfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60', age=7, notes='Right Hand Man')
pet3 = Pet(name='Nala', species='Lioness', photo_url='https://images.unsplash.com/photo-1509556948-32ff846e7968?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bGlvbmVzc3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=800&q=60', age='1', available=False)
pet4 = Pet(name='Rafiki', species='Mandrill', photo_url='https://images.unsplash.com/photo-1605583956585-c749b5d92c9d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bWFuZHJpbGx8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=800&q=60', notes='Likes drugs', available=True)
pet5 = Pet(name='Ed', species='Hyena', age='5', notes='Funnier in the animated movie', available=False)

db.session.add_all([pet1, pet2, pet3, pet4, pet5])
db.session.commit()