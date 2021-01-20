import os
import shutil
import glob

while True:

    print("*** Last essays ***")
    os.chdir("..\\")
    root_elements = []
    for file in glob.glob("*.*"):
        root_elements.append(file)

    root_elements.sort(reverse=True)
    for file in root_elements[0:10]:
        print(file)

    print("******")

    os.chdir("folder")
    for file in glob.glob("*.docx"):
        doc_result = file

    for file in glob.glob("*.png"):
        pic_result = file

    try:
        print("PNG found: " + pic_result)
    except NameError:
        print("No .png provided")
        break

    name_input = input("Provide a number ")

    pic_name = name_input + ".png"

    doc_name = name_input + ".docx"

    def copy_rename(old_file_name, new_file_name):

        src_dir = os.curdir

        # COPY
        dst_dir = os.path.join(os.curdir, "..\\")

        src_file = os.path.join(src_dir, old_file_name)

        shutil.copy(src_file, dst_dir)

        # RENAME
        dst_file = os.path.join(dst_dir, old_file_name)

        new_dst_file_name = os.path.join(dst_dir, new_file_name)

        os.rename(dst_file, new_dst_file_name)

        # if src_file is png then delete it

        for i in glob.glob("*.png"):
            os.remove(i)

    copy_rename(pic_result, pic_name)

    copy_rename(doc_result, doc_name)

    break

print("The end")

input('press Enter to exit: ')
