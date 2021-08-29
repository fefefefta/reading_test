import sqlite3


class User:

	def __init__(self):
		self.auth()


	def auth(self):
		reg_answer = input("Вы зарегистрированы? да/нет/выйти: ")
		if reg_answer.lower() == "нет":
			self.reg()
			self.auth()
		elif reg_answer.lower() == "выйти":
			self.__name = None
			self.__secret = None
			self.__is_accessed = False
		elif reg_answer.lower() == "да":
			conn = sqlite3.connect("readers_db.db")
			# create_query = "CREATE TABLE readers (user_name TEXT, user_password TEXT, last_score INTEGER)"
			cursor = conn.cursor()
			# cursor.execute(create_query)
			login = input("Введите ваш логин: ")
			password = input("Введите ваш пароль: ")
			cursor.execute("SELECT * FROM readers WHERE user_name=? AND user_password=?", (login, password))
			data = cursor.fetchone()
			conn.close()
			if data:
				print("Вы вошли.")
				self.__name = login
				self.__secret = password
				self.__is_accessed = True
			else:
				print("Неверный логин или пароль. Попробуйте еще раз.")
				self.auth()
		else:
			print("Я вас не понимаю. Попробуйте еще раз.")
			self.auth()


	def get_name(self):
		return self.__name


	def reg(self):
		login = input("Придумайте логин: ")
		password = input("Придумайте пароль: ")
		conn = sqlite3.connect("readers_db.db")
		create_query = "CREATE TABLE readers (user_name TEXT, user_password TEXT, last_score INTEGER)"
		cursor = conn.cursor()
		cursor.execute(create_query)

		cursor.execute("INSERT INTO readers VALUES (?, ?, ?)", (login, password, 0))
		conn.commit()
		conn.close()
		print("Вы зарегистрировались. Теперь авторизуйтесь.")


	
	def push_score(self, score):
		self.__score = score
		conn = sqlite3.connect("readers_db.db")
		cursor = conn.cursor()

		cursor.execute("UPDATE readers SET last_score=? WHERE user_name=? AND user_password=?", (self.__score, self.__name, self.__secret))
		conn.commit()
		conn.close()



	def get_score(self):
		return self.score
