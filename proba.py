data={"Россия":{"capital":"Моcква"},"Корея":{"capital":"Сеул"}}
for n in data:
    print(n,data[n]['capital'])

n=data.get("Корея")

print(n)