import markdown

with open("Git.md", "r") as file:
    text = file.read()
    html = markdown.markdown(text)
    
    title = html.split()[0].replace("<h1>","").replace("</h1>","")
    
print(title)