import sqlite3


f = open('text.txt', 'r')
text = ''
line = f.readline()
while "###" not in line:
	text += line
	line = f.readline()

questions = []

for i in range(5):
	question_str = ''
	line = f.readline()
	while "###" not in line:
		question_str += line
		line = f.readline()
	questions.append(question_str)

answers = f.readline().split()

f.close()

conn = sqlite3.connect("texts_db.db")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE texts (id INTEGER, text_ TEXT, q1 TEXT, q2 TEXT, q3 TEXT, q4 TEXT, q5 TEXT, a1 TEXT, a2 TEXT, a3 TEXT, a4 TEXT, a5 TEXT)")
cursor.execute("SELECT * FROM texts")

text_id = len(cursor.fetchall()) + 1
values = (text_id, text, *questions, *answers)

cursor.execute("INSERT INTO texts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values)

conn.commit()
conn.close()








