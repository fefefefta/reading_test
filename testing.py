import random
import sqlite3
import time
import os

class Testing:

	def __init__(self):
		self.text_info = self.get_text_info()


	def get_text_info(self):
		conn = sqlite3.connect("texts_db.db")
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM texts")
		rand_text_info = cursor.fetchall()
		conn.close()
		return random.choice((rand_text_info))
		

	def test_process(self):
		text_id, text, q1, q2, q3, q4, q5, a1, a2, a3, a4, a5 = self.text_info
		questions = [q1, q2, q3, q4, q5]
		answers = [a1, a2, a3, a4, a5]

		counter = 0
		for word in text.split(' '):
			counter += 1

		input("Нажмите Enter, если готовы начать. Сразу после прочтения также нажмите Enter.")
		start_time = time.time()
		print(text)
		input()
		result_time = time.time() - start_time
		os.system('cls' if os.name == 'nt' else 'clear')

		print("Теперь пройдите небольшой тест на содержание текста.")

		correct_ans = 0
		for i in range(5):
			ans = input("Вопрос: " + questions[i])
			if ans == answers[i]:
				print("Верно!")
				correct_ans += 1
			else:
				print("Неверно:(")

		self.speed_score = counter // (result_time/60)
		self.comprehension_score = (correct_ans / 5) * 100
		return (self.speed_score, self.comprehension_score)

	


