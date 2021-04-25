import os

banks_path = ["bank1.csv", "bank2.csv", "bank3.csv"]
integrated = 'integrated.csv'

# To avoid unwanted append - remove file, if already exists
if os.path.isfile(integrated):
    os.remove(integrated)

for banks in banks_path:
    with open(banks, 'r') as f:
        data = f.read()

    with open(integrated, 'a') as f:
        f.write(data)
