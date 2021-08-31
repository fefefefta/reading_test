from user import User
from testing import Testing
reader = User()
test = Testing()

if reader.get_is_accessed() == True:
	reader.push_score(test.test_process())
else: 
	print("До свидания!")