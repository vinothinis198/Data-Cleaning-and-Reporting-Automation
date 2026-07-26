import pandas as pd
import matplotlib.pyplot as plt
# Read the Excel file
data = pd.read_excel("employee_data.xlsx")
# Display original data
print("Original Data")
print(data)
# Fill missing values
data["Age"] = data["Age"].fillna(0)
data["Salary"] = data["Salary"].fillna(0)
# Remove duplicate rows
data = data.drop_duplicates()
# Convert department names to uppercase
data["Department"] = data["Department"].str.upper()
# Display cleaned data
print("\nCleaned Data")
print(data)
# Generate summary report
print("\nSummary Report")
print("Total Employees =", len(data))
print("Average Salary =", data["Salary"].mean())
print("Maximum Salary =", data["Salary"].max())
print("Minimum Salary =", data["Salary"].min())
# Plot salary graph
plt.bar(data["Name"], data["Salary"])
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.title("Employee Salary Report")
plt.savefig("salary_report.png")
plt.show()