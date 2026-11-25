import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")



df = df.drop_duplicates()

df["salary"] = (
    df["salary"]
    .astype("string")
    .str.replace(",", "", regex=False)
)

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["salary"] = df["salary"].fillna(df["salary"].median())

df["salary"] =  pd.to_numeric(df["salary"],errors="coerce")

df["salary"] = df["salary"].fillna(df["salary"].median())


df["experience_years"] = pd.to_numeric(
    df["experience_years"], errors="coerce"
)

mask = (df["id"] == 1019) & (df["experience_years"].isna())
df.loc[mask,"experience_years"] = 1.7

print(df)

print(df.isna().sum())
print("Duplicate rows remaining:", df.duplicated().sum())
df.info()

fig,ax = plt.subplots(figsize=(10,6))

department_count= df["department"].value_counts()

ax.bar(department_count.index,department_count.values)

ax.set_title("Number of Employees in Each Department")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")

fig.tight_layout()
plt.show()
plt.savefig("department Employees count.png",dpi=300)
# histogram

fig,ax = plt.subplots(figsize=(10,8))
ax.hist(df["salary"],bins=20,edgecolor="red")

ax.set_title("salary Distribution")

ax.set_xlabel("salary")
ax.set_ylabel("Number of Employees")

fig.tight_layout()
plt.show()
plt.savefig("salary distribution.png",dpi=300)

#scatter plot

fig,ax = plt.subplots(figsize=(10,8))
ax.scatter(df["experience_years"],df["salary"],color="blue",alpha=0.5)

ax.set_title("experience vs salary")

ax.set_xlabel("experience years")
ax.set_ylabel("salary")

fig.tight_layout()
plt.show()
plt.savefig("experience vs salary.png",dpi=300)

#line chart

average_salary = df.groupby("department")["salary"].mean()

fig,ax =plt.subplots(figsize=(10,8))

ax.plot(average_salary.index, average_salary.values, marker="o")

ax.set_title("salary by department")
ax.set_xlabel("department")
ax.set_ylabel("salary")

fig.tight_layout()

plt.show()
plt.savefig("salary by department.png",dpi=300)