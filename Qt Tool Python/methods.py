"""
Module contains all the methods used in the Main.py file
for ease of use and readability.
"""
import os

from colorama import init, Fore

init(autoreset=True)


def open_file(path):
    os.startfile(os.path.abspath(path))


def search_widget(file, widget):
    with open(os.path.abspath(file)) as file:
        widget_vars = []
        lines_array = file.readlines()
        for line in lines_array:
            if widget in line:
                widget_vars.append((line.split("=")[0]).strip())
            else:
                continue
        print(f"\n{len(widget_vars)} Variables with Type {widget}:\n")
        x = 1
        for widget in widget_vars:
            print(f"{x}) {widget}")
            x += 1


def search_line(file, string):
    with open(os.path.abspath(file)) as file:
        lines_array = file.readlines()
        finds = []
        for line in lines_array:
            if string in line:
                finds.append(line.strip())
            else:
                continue
        print(f"\n{len(finds)} Instances:\n")
        x = 1
        for find in finds:
            print(f"{x}) {find}")
            x += 1


def search_line_nums(file, string):
    with open(os.path.abspath(file)) as file:
        lines_array = file.readlines()
        finds = []
        for line in lines_array:
            if string in line:
                finds.append(lines_array.index(line) + 1)
            else:
                continue
        print(f"\n{len(finds)} Instances:\n")
        x = 1
        for find in finds:
            print(f"{x}) {find}")
            x += 1


def view(file):
    with open(os.path.abspath(file)) as file:
        print("\nFile Read Begin:")
        print(file.read())
        print("\nFile Read End")


def gen_copy(input_file, output_file):
    with open(os.path.abspath(input_file)) as file:
        lines_array = file.readlines()
    with open(os.path.abspath(output_file), "w+") as outfile:
        outfile.writelines(lines_array)


def gen(output_file, widget, con_key):
    variables = []
    insert_pt_1 = 0
    insert_pt_2 = 0
    with open(os.path.abspath(output_file), "r+") as outfile:
        original_lines = outfile.readlines()
    for line in original_lines:
        if widget in line and "self." in line:
            variables.append((line.split("=")[0]).strip())
        elif "def retranslate" in line:
            insert_pt_1 = original_lines.index(line)
        elif "if __name__" in line:
            insert_pt_2 = original_lines.index(line)
        else:
            continue
    # Start
    new_lines = original_lines[0:insert_pt_1]
    new_lines.append("\n        # Start of Generated Code\n")
    for var in variables:
        new_lines.append(f"\n        {var}.{con_key}.connect(lambda: {var}_function())")
    new_lines.append("\n\n       # End of Generated Code\n\n")
    new_lines += original_lines[insert_pt_1: insert_pt_2]
    new_lines.append("\n    # Start of Generated Code\n")
    for var in variables:
        new_lines.append(f"    def {var[5:]}_function(self):\n        pass\n\n")
    new_lines.append("\n    # Start of Generated Code\n")
    new_lines += original_lines[insert_pt_2:]
    # End
    with open(os.path.abspath(output_file), "w+") as outfile:
        outfile.writelines(new_lines)


def gen_imports(output_file, imports):
    with open(os.path.abspath(output_file), "r+") as outfile:
        original_lines = outfile.readlines()
    with open(output_file, "w+") as file:
        colorama = ""
        for i in imports:
            if "colorama" in i:
                colorama = input(f"{Fore.BLUE}Do you want to add init statement?(y/n){Fore.GREEN}")
                if len(i) == 1:
                    file.write(f"\nimport {i[0]}")
                elif i[0] == "namespace":
                    file.write(f"\nimport {i[1]} as {i[2]}")
                elif i[0] == "package":
                    file.write(f"\nfrom {i[1]} import {i[2]}")
                else:
                    continue
        if colorama == "y":
            file.write("\n\ninit(autoreset=True)\n")
        file.write("\n\n")
        file.writelines(original_lines)
