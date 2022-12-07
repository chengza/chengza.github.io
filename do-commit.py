import glob
import os
import markdown

if __name__ == "__main__":
    #ensure ./posts and ./html exist
    if not os.path.exists("./posts"):
        os.makedirs("./posts")
    if not os.path.exists("./html"):
        os.makedirs("./html")

    #collect all .md files in posts directory
    files = glob.glob("posts/*.md")
    #sort by modification time
    files.sort(key=os.path.getmtime)
    #check if matching html file is in the output directory ./html
    for f in files:
        html_file = f.replace(".md", ".html")
        html_file = html_file.replace("posts", "html")
        if not os.path.exists(html_file) or os.path.getmtime(f) > os.path.getmtime(html_file):
            #convert markdown to html file
            html = markdown.markdownFromFile(input=f, output=html_file, encoding="utf-8")

    #create index.html file
    index = open("./index.html", "w")
    index.write("<html><head><title>My Blog</title></head><body>")
    index.write("<h1>My Blog</h1>")
    index.write("<ul>")
    for f in files:
        html_file = f.replace(".md", ".html")
        html_file = html_file.replace("posts", "html")
        index.write("<li><a href='" + html_file + "'>" + f + "</a></li>")
    index.write("</ul>")
    index.write("</body></html>")
    index.close()

    #git add all files
    code=os.system("git add .")
    if code != 0:
        print("git add failed")
        exit(1)
    #git commit
    code=os.system('git commit -m "pages auto commit"')
    if code != 0:
        print("git commit failed")
        exit(1)
    #git push
    code=os.system("git push")
    if code != 0:
        print("git push failed")
        exit(1)