import csv
import json
import statistics


def read_records():
    global emps
    with open("emp.csv") as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]


def correct_types():
    for e in emps:
        e['age'] = int(e['age'])

def correct_types_json(profs):
    for e in profs:
        e['age'] = int(e['age'])


# average employee age
def find_average_age():
    avg_age = sum([x['age'] for x in emps]) / len(emps)
    return avg_age


# TODO:: implement this
def find_average_age_for_dept(dept):
    '''try:
        avg_age=sum([x['age'] for x in emp_data if x['dept'] == dept]) / len([x['age'] for x in emp_data if x['dept'] == dept]) #working code
    except ZeroDivisionError:
        return 0.0'''


    avg_age= statistics.mean([x['age'] for x in emps if x['dept'] == dept] or [0.0])
    return avg_age

def read_json_records():
    print("\nReading from json file\n")
    global profs
    profs = json.load(open("emp_json.json"))


def correct_types_json():
    for e in profs:
        e['age'] = int(e['age'])



def find_average_age_json():
    avg_age = sum([x['age'] for x in profs]) / len(profs)
    return avg_age


def find_average_age_for_dept_json(dept):
    '''try:
        avg_age=sum([x['age'] for x in emp_data if x['dept'] == dept]) / len([x['age'] for x in emp_data if x['dept'] == dept]) #working code
    except ZeroDivisionError:
        return 0.0'''


    avg_age= statistics.mean([x['age'] for x in profs if x['dept'] == dept] or [0.0])
    return avg_age








def main():
    read_records()
    correct_types()
    print("Average emp age is:", find_average_age())
    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))


    # TODO: Do same thing with json file instead of csv file
    read_json_records()
    correct_types_json()
    print("Average emp age is:", find_average_age_json())
    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))



if __name__ == "__main__":
    main()
