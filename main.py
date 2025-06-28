import csv
from matcher import compare_keywords
import pandas as pd

def add_job_entry():
    company = input("Company Name: ")
    role = input("Job Title: ")
    job_file = input("Job Description file name (e.g. job_description.txt): ")
    resume_file = input("Resume file name (e.g. resume.txt): ")

    match_percent = compare_keywords(job_file, resume_file)

    with open("data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([company, role, job_file, resume_file, f"{match_percent}%"])

    print(f"\n✔️  Job added! Resume matched {match_percent}% of the job description.\n")

def view_jobs():
    print("\n📄 Saved Applications:\n")
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)



def show_analytics():
    try:
        df = pd.read_csv("data.csv", names=["Company", "Role", "JobFile", "ResumeFile", "Match"])
        df["Match"] = df["Match"].str.replace('%', '').astype(float)

        print(f"\n📈 Total Applications: {len(df)}")
        print(f"✅ Average Match: {df['Match'].mean():.2f}%")
        print("🏆 Top Companies Applied To:\n")
        print(df['Company'].value_counts().head(3))
    except Exception as e:
        print(f"❌ Error reading data: {e}")


if __name__ == "__main__":
    while True:
        print("\n=== Job Tracker ===")
        print("1. Add a Job Application")
        print("2. View All Applications")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_job_entry()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            break
        else:
            print("❌ Invalid option. Try again.")
        print("Please enter a valid option.\n")
        print("Please enter a valid option.\n")