import hashlib
from utils import get_input_path

# PART ONE
file_path = get_input_path(__file__, '2015_4_input.txt')
file = open(file_path)
secret_key = file.read()
file.close()
potential_answer = 1
while True:
    key = f'{secret_key}{potential_answer}'
    hash_of_key = hashlib.md5(key.encode()).hexdigest()
    if "00000" in hash_of_key[0:5]:
        print(potential_answer)
        break
    else:
        potential_answer += 1

# PART TWO
while True:
    key = f'{secret_key}{potential_answer}'
    hash_of_key = hashlib.md5(key.encode()).hexdigest()
    if "000000" in hash_of_key[0:6]:
        print(potential_answer)
        break
    else:
        potential_answer += 1
