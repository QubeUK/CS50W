

entries = ["CSS","Git","HTML","Python","HTTP"]
query = "ht"
search = query.casefold()

result=[]



if search in map(str.casefold, entries):
    print("Found it")


#result = list(filter(lambda entry: query in entry, map(str.casefold, entries)))

for entry in entries:   
    if search in entry.casefold():        
        result.append(entry)


print(result)
print(entries)


