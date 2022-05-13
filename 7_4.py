import os


def size_folder(name):
    some_dict = {}
    i = 0
    b = 0
    for address, dirs, files in os.walk(name):
        for file in files:
            file_size = os.stat(os.path.join(address, file)).st_size
            if file_size <= 100:
                i += 1

            elif file_size <= 1000:
                b += 1
    file1 = some_dict.update({100: i, 1000: b})
    return some_dict


print(size_folder("test"))
