import os

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    catalog = os.path.join(path, "cn//1-目录.md")

    outfilename = os.path.join(path, "cn\\release.md")

    # clear contents
    open(outfilename, 'w', encoding="utf-8").close()

    # write catalog
    with open(catalog, encoding="utf-8") as file:
        while (line := file.readline()):
            with open(outfilename, "a+", encoding="utf-8") as outfile:
                outfile.write(line)

    with open(catalog, encoding="utf-8") as file:
        while (line := file.readline()):
        # while (line := file.readline().rstrip()):
            if(line.rstrip()):
                # print(line)
                if(line.find("(")) == -1:
                    continue

                subfilename = line[line.find("(")+1:line.find(")")]
                # print(subfilename)
                title = subfilename[subfilename.rfind("-")+1:subfilename.rfind('.')]
                print(title)
                headerlevel = subfilename.count("-")
                pageheader = "\r\n#" + "#"*headerlevel + " " + title + "\r\n"
                print(pageheader)

                infilename = os.path.join(path, "cn\\"+subfilename)
                with open(outfilename, "a+", encoding="utf-8") as outfile:
                    try:
                        with open(infilename, encoding="utf-8") as infile:
                            outfile.write(pageheader)
                            for line in infile:
                                outfile.write(line)
                    except Exception  as e:
                        print(e)

    # import subprocess
    # subprocess.run(["python",  "-m markdown2", ".\cn\release.md > .\cn\release.html"])         