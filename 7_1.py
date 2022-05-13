from sys import argv
import os


def make_dir(name):
    try:
        os.makedirs(name)
        file = os.path.join(os.path.dirname(os.path.abspath(name)), name)
        os.mkdir(os.path.join(file, "settings"))
        os.mkdir(os.path.join(file, "mainapp"))
        os.mkdir(os.path.join(file, "adminapp"))
        os.mkdir(os.path.join(file, "mainapp"))
    except FileExistsError:
        print('{} - уже существует, дайте другое имя'.format(name))



#make_dir("dz")

if __name__ == '__main__':
    print('---------------------Задача №1 (easy)----------------------')
    make_dir(argv[-1])

