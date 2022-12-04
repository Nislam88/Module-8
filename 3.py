def heading_two(text):
    html = f"<h2>{text}</h2>"
    return html
data = heading_two("This is heading two")
# print(data)

def html_tag(text, html_tag):
    html = f"<{html_tag}>{text}</{html_tag}>"
    return html
print(html_tag("This is paragraph", "p"))
