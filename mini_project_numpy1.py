import numpy as n


months = n.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
sales=[]

print("Enter sales (in $) for each month: ")

for month in months:
    value=float(input(f"{month} : "))
    sales.append(value)

sales=n.array(sales)


print("\n---Company Sales Analysis---")
print("Total Sales Is:",n.sum(sales))
print("Avareg of total sales is: ",n.mean(sales))
print("Highest sale is: ",max(sales))
print("Lowest sale is: ",min(sales))


best_month = months[n.argmax(sales)]
worst_month = months[n.argmin(sales)]

print("Best Month:", best_month)
print("Worst Month:", worst_month)


above_avg = months[sales > n.mean(sales)]
below_avg = months[sales < n.mean(sales)]

print("Above Average Months:", above_avg)
print("Below Average Months:", below_avg)