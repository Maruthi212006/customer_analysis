
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Convert Purchase_Date into date format
df["Purchase_Date"] = pd.to_datetime(df["Purchase_Date"])

# Customer purchase analysis
analysis = df.groupby(
    ["Customer_ID", "Customer_Name"]
).agg(
    Purchase_Frequency=("Purchase_ID", "count"),
    Total_Amount=("Amount", "sum"),
    Average_Amount=("Amount", "mean"),
    Last_Purchase=("Purchase_Date", "max")
).reset_index()

# Sort by purchase frequency
analysis = analysis.sort_values(
    by="Purchase_Frequency",
    ascending=False
)

# Customer classification
def classify_customer(frequency):
    if frequency >= 4:
        return "Frequent Customer"
    elif frequency >= 2:
        return "Occasional Customer"
    else:
        return "Low Frequency Customer"

analysis["Customer_Category"] = (
    analysis["Purchase_Frequency"].apply(classify_customer)
)

# Display results
print("\nCUSTOMER PURCHASE FREQUENCY ANALYSIS")
print("------------------------------------")
print(analysis.to_string(index=False))

# Save analysis result
analysis.to_csv("customer_analysis_output.csv", index=False)

# Graph 1: Purchase Frequency
plt.figure(figsize=(8, 5))
plt.bar(analysis["Customer_Name"],
        analysis["Purchase_Frequency"])
plt.title("Customer Purchase Frequency")
plt.xlabel("Customer Name")
plt.ylabel("Number of Purchases")
plt.tight_layout()
plt.savefig("purchase_frequency.png")
plt.show()

# Graph 2: Total Spending
plt.figure(figsize=(8, 5))
plt.bar(analysis["Customer_Name"],
        analysis["Total_Amount"])
plt.title("Customer Total Spending")
plt.xlabel("Customer Name")
plt.ylabel("Total Amount")
plt.tight_layout()
plt.savefig("customer_spending.png")
plt.show()

print("\nAnalysis completed successfully!")
print("Results saved in customer_analysis_output.csv")
print("Graphs saved successfully!")
