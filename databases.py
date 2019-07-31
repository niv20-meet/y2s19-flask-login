from model import Base, User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word, food="pies"):

	user = User(username=name, fav_food=food, add_pic=pic)
	user.hash_password(secret_word)
	session.add(user)
	session.commit()


def update_food(fave_food,user):
	user.fav_food=fave_food
	session.commit()

def update_photo(pic,user):
	user.add_pic=pic
	session.commit()


def get_user(username):
	"""Find the first user in the DB, by their username."""
	return session.query(User).filter_by(username=username).first()

def delet_all_users():
	session.query(User).delete()
	session.commit()
