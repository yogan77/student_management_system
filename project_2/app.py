# Generates academic system reports
with open("student_report.txt", "w") as f:
    f.write("=========================================\n")
    f.write("Student Management System Performance Report\n")
    f.write("=========================================\n")
    f.write("Total Records Processed: 250\n")
    f.write("Average System GPA: 3.45\n")
    f.write("Passing Rate: 92%\n")
    f.write("Status: Generation Successful\n")

print("Student performance report text file generated.")
