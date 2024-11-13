from findTemperatureLive import findTemperatureLive
from sentence import sentence

def getTemp():
    return findTemperatureLive()

def split_emailuser(emailuser):
    firstname, lastname = emailuser.split(".")
    return firstname.capitalize(), lastname.capitalize()

def generate_html_head(firstname, lastname):
    return f"""<head>
    <title>{firstname} {lastname}'s Home Page</title>
</head>"""

def generate_html_body(firstname, lastname):
    temperature = findTemperatureLive()
    randomSentence = sentence()
    return f"""<body style="background-color:cyan;">
    <h1>Welcome to {firstname} {lastname}'s Home Page</h1>
    <img src="{firstname}.{lastname}.jpg" alt="Picture of {firstname}"
    width = "400"
    height = "500">
    <p>This is {firstname} {lastname}'s personal home page.</p>
    <p>The current temperature in Boston is {temperature} Degrees Farenheit</p>
    <p>Here's a random sentence: {randomSentence}</p>
    </body>
    """

def generate_html_content(firstname, lastname):
    head = generate_html_head(firstname, lastname)
    body = generate_html_body(firstname, lastname)
    return f"""<!DOCTYPE html>
<html>
{head}
{body}
</html>"""

def write_html_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def createHomePage(emailuser):
    firstname, lastname = split_emailuser(emailuser)
    html_content = generate_html_content(firstname, lastname)
    write_html_file(f"{emailuser}.html", html_content)

if __name__ == "__main__":
    createHomePage("matt.brittain")