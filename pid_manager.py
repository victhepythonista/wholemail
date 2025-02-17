# product id manage here 




import uuid,os
from string import ascii_uppercase, digits 
from random import choice 
from io import StringIO
import datetime as dt

# generate a new serial number
codes_file = "pids/test/CODES.txt"


def  Makeid(length = 10 ,  numbers = True , letters = True):
    contents = ""
    if numbers:
        contents += digits
    if letters:
        contents += ascii_uppercase
    cache = ""
    while True:
        for i in range(0, length):
            cache += choice(contents)
        return cache

    
def  NewSerialNo( length = 10 , data_file = codes_file ):
    print(f'Creating a serial number -- file {data_file}')
    if not os.path.isfile(data_file):
        try:
            missing_folder , missing_file  = os.path.split(data_file)
            os.makedirs(missing_folder)
            with open( data_file , "w") as f:
                f.write("")
                print("File  created sucessfully")
        except:
            print(f"Error creating serial number for {data_file}")
    with open(data_file, "r") as f :
        lines = f.readlines()
    lines = [s.strip() for s in lines]
    contents = digits + ascii_uppercase
    while True:
        cache = ""
        for i in range(0, length):
            cache += choice(contents)
        if not cache  in lines:
            lines.append(cache)
            with open(data_file, 'w') as f:
                for char in lines:
                    f.write(char + "\n")
                
            return cache

 
 
def IsValidCode(code , email , file  ):
	if not os.path.isfile(file):
		with open(file, "w") as f:
			f.write("EMAIL  , CODE")
	with open(file, "r") as f:
		data = f.readlines()

	info = []
	lines = [s.strip() for s in data]
	for l in lines:
		if email in l and code in l.split():
			lines.pop(lines.index(l))
			with open(file, "w") as f:
				for l in lines:
					f.write(l+"\n")
			return True

	

	return False

 
 
 

if __name__ == '__main__':
    print(NewSerialNo(10))