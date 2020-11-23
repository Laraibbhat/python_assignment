import csv
import json
import statistics


def read_records():
    global emps
    with open("emp.csv") as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]


def correct_types(data):
    for e in data:
        e['age'] = int(e['age'])


# average employee age
def find_average_age(emp_data):
    avg_age = sum([x['age'] for x in emp_data]) / len(emp_data)
    return avg_age


# TODO:: implement this
def find_average_age_for_dept(dept, emp_data):
    '''try:
        avg_age=sum([x['age'] for x in emp_data if x['dept'] == dept]) / len([x['age'] for x in emp_data if x['dept'] == dept]) #working code
    except ZeroDivisionError:
        return 0.0'''

    
    avg_age= statistics.mean([x['age'] for x in emp_data if x['dept'] == dept] or [0.0])
    return avg_age

def read_json_records():
    print("\nReading from json file\n")
    global profs
    profs = json.load(open("emp_json.json"))








def main():
    read_records()
    correct_types(emps)
    print("Average emp age is:", find_average_age(emps))
    print("Average emp age for dept d1:", find_average_age_for_dept("d1",emps))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2",emps))


    # TODO: Do same thing with json file instead of csv file
    read_json_records()
    correct_types(profs)
    print("Average emp age is:", find_average_age(profs))
    print("Average emp age for dept d1:", find_average_age_for_dept("d1",profs))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2",profs))



if __name__ == "__main__":
    main()
