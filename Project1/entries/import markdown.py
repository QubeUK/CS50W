import markdown

with open("Git.md", "r") as file:
    text = file.read()
    html = markdown.markdown(text)
    
print(html)