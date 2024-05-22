from bs4 import BeautifulSoup
EXTENSION = "sql"
FILE_PATH = "/Users/koomin/Coding/CodingTest/programmers/SQL/level2/"

with open("problems.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
a_tags = soup.find_all("a")
for a_tag in a_tags:
    title  = a_tag.get_text()
    title = title.replace(' ', '_').replace('/', '_') + '.' + EXTENSION
    print(title)
    with open(FILE_PATH + title, "w") as f:
        pass
# print(soup.prettify())
    

git commit --amend --no-edit --date "Mon 4 Mar 2024 17:39:40 KST"