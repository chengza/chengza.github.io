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
    with open("post.template.html", "r") as f:
        post_template = f.read()
    for f in files:
        html_file = f.replace(".md", ".html")
        html_file = html_file.replace("posts", "html")
        if not os.path.exists(html_file) or os.path.getmtime(f) > os.path.getmtime(html_file):
            #convert markdown to html string
            html = markdown.markdown(open(f).read())
            post_html=post_template.replace("{{post}}", html)
            #write html string to html file
            with open(html_file, "w") as f:
                f.write(post_html)
            print("Converted %s to %s" % (f, html_file))

    #create index.html file by ./index.tamplate.html
    with open("index.template.html", "r",encoding='utf-8') as f:
        template = f.read()
        list_str = "<ul>"
        for f in files:
            html_file = f.replace(".md", ".html")
            html_file = html_file.replace("posts", "html")
            list_str += "<li><a href='%s'>%s</a></li>" % (html_file, f.split('/')[-1].split('\\')[-1][:-3])
        list_str += "</ul>"
        template = template.replace("{{list}}", list_str)
        with open("index.html", "w",encoding='utf-8') as f:
            f.write(template)
    # exit(0)

    #git add all files
    code=os.system("git add .")
    #git commit
    code=os.system('git commit -m "pages auto commit"')
    #git push
    code=os.system("git push")
    if code != 0:
        print("git push failed")
        exit(1)