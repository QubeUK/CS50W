

entries = ["CSS","Git","HTML","Python"]
query = "css"
search = query.casefold()



print(entries)
print(search)


if query.casefold() in map(str.casefold, entries):
    print("found it")