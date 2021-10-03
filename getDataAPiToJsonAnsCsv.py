import requests
import base64
import json

base_url = "http://dummy.restapiexample.com/api/v1/employees";
#base_url = "https://v6.exchangerate-api.com/v6/1fca918a82cf5772aab3ea46/latest/USD";

def get_report(base_url):
    print("Getting report results...")
    header_gs = {'Accept': 'application/json'}
    r = requests.get(base_url)
    if r.ok:
        print("Report results received...")
        print("HTTP %i - %s" % (r.status_code, r.reason))
        return r.text
    else:
        print("HTTP %i - %s" % (r.status_code, r.reason))

def export_to_json(base_url):
    print("Exporting report results to JSON file...")
    r = get_report(base_url)
    text_file = open("report_results.json", "w", encoding="utf8")
    text_file.write(r)
    text_file.close()

def export_to_csv(base_url):
    print("Exporting report results to JSON file...")

    csv_file = open('report_results.csv', "w", encoding="utf8")
    csv_file.write("Id, Employee_Name"+"\n") #manually modify this CSV file header
    csv_file.close()

    #there are 3 attributes in my example; add/remove levels according to the number of attributes in your case
    r = get_report(base_url)
    report_parsed = json.loads(r)
    print(report_parsed)
    a1_list = report_parsed['data']
    print(a1_list)
    for a1 in a1_list:
        a1_id = a1['id']
        a2_employee_name=a1['employee_name']
        csv_file = open('report_results.csv', "a", encoding="utf8")
        csv_file.write("'"+a1_id + "','" + a2_employee_name +"\n")
        csv_file.close()


    print("Export finished")

def main():
    choice = None
    while choice != "0":
        print \
            ("""
        ---MENU---
        
        0 - Exit
        1 - Export report results to JSON file
        2 - Export report results to CSV file
        """)

        choice = input("Your choice: ") # What To Do ???
        print()

        if choice == "0":
            print("Good bye!")
        elif choice == "1":
            export_to_json(base_url)
        elif choice == "2":
            export_to_csv(base_url)
        else:
            print(" ### Wrong option ### ")

### Main program
main()

