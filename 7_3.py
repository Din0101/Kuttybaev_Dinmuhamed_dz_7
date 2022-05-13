import os
import shutil


def templates_join():
    file = os.path.dirname(os.path.abspath("my_project"))
    file2 = os.path.join(file, "my_project")
    file_dst = os.path.join(file, "templates")
    for i in os.listdir("my_project"):
        file3 = os.path.join(file2, i)
        for e in os.listdir(file3):
            if e == "templates":
                file4 = os.path.join(file3, e)
                for el in os.listdir(file4):
                    file5 = os.path.join(file4, el)
                    file_dst2 = os.path.join(file_dst, el)
                    shutil.copytree(file4, file_dst2)

    print(file)
    return


templates_join()
