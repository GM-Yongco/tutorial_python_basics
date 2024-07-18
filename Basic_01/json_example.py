# Author			: G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date				: ur my date uwu
# Description		: Code that will impress u ;)
# HEADERS ================================================================

import io
import json
import pprint

# ========================================================================
# FUNCTIONS MISC
# ========================================================================

def section(section_name:str = "SECTION") -> None:
	section_name = f"\n {section_name} {'-' * (40 - len(section_name))}\n"
	print(section_name)

# ========================================================================
# FUNCTIONS 
# ========================================================================

def json_read(path:str = "REFERENCES/classroom.json") -> dict:
	json_details:dict = {"error":"error"}
	try:
		file:io.TextIOWrapper = open(path, "r")
		json_details = json.load(file)
		file.close()
	except Exception as e:
		print(e)

	return json_details

def json_write(path:str = "REFERENCES/classroom.json", new_json:dict = "")->bool:
	status_success:bool = True
	try:
		file:io.TextIOWrapper = open(path, "w")
		json.dump(new_json, file, indent = 4)
		file.close()
	except Exception as e:
		print(e)
		status_success = False
	return status_success

def json_to_string()->str:
	return json.dumps(obj = json_read(), indent=4)

# ========================================================================

def test1():
	dic = json_read()
	
	pprint.pprint(dic)
	section()
	if dic["error"] == "success":
		pprint.pprint(dic["classroom"]["students"])
		pprint.pprint(dic["classroom"]["grade_level"])

def test2():
	dic = json_read()
	if dic["error"] == "success":
		section()
		students:list = dic["classroom"]["students"] #list of students taken as reference
		new_student:dict = {
			"name": "Duplikate",
			"age": 17,
			"grades": {
				"Math": 95,
				"Science": 92,
				"English": 60
			}
		}
		students.append(new_student)
		print(f"json_write_status:\t{json_write(new_json=dic)}")

# ========================================================================
# MAIN 
# ========================================================================

if __name__ == '__main__':
	section("START")
	test2()
	section("END test2")
	test1()
	section("END test2")
	print(json_to_string())
	section("END")