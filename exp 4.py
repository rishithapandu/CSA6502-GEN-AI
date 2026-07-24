import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [25000, 30000, 28000, 35000, 40000]

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.subplot(1,2,2)
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Line Graph")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()
