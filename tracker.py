import csv
from matcher import compare_keywords

def add_job_entry():
    company = input("Company Name: ")
    role = input("Role Title: ")
    job_desc = input("Path to Job Description file: ")
    resume = input("Path to your Resume: ")

    match_percent = compare_keywords(job_desc, resume)

    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([company, role, job_desc, resume, f"{match_percent}%"])

    print(f"Job added! Resume matched {match_percent}% of the job description.\n")

def view_jobs():
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

if __name__ == "__main__":
    while True:
        print("\n1. Add Job\n2. View All Jobs\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_job_entry()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            break
        else:
            print("Invalid option.")
