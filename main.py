import os
from simple_term_menu import TerminalMenu
import math
from datamanager import *

#Commands
add_new_dir = 'Add Directory'
remove_dir = 'Remove Directory'
change_dir = 'Change Current Directory'
get_dir_info = 'Get Directory Info'
get_file_location = 'Get File Location'
create_file = 'Create File'
rename_file = 'Rename File'
delete_file = 'Delete A File'
delete_all_files = 'Delete All Files'
delete_type_of_files = 'Delete A Type Of Files'
delete_files_with_specific_size = 'Delete Files With Specific Size'
create_dir = 'Create Directory'
delete_dir = 'Delete Directory'
sort_filenames_numerically = 'Sort File Names With Numbers'
close_program = '[x] Close'
exit_menu = '[x] Exit'

current_dir = ''
invalid_input = '(Invalid Input!)'

options = [add_new_dir, remove_dir, change_dir, get_dir_info, get_file_location, create_file, rename_file, delete_file, delete_all_files, delete_type_of_files, delete_files_with_specific_size, create_dir, delete_dir, sort_filenames_numerically, close_program]
menu = TerminalMenu(options)

print()

create_database()
if len(get_dirs_names()) > 0:
    current_dir = get_current_dir_path()

    if len(current_dir) > 0:
        os.chdir(current_dir)
        print('Current Directory Path: ' + current_dir + '\n')

while True:
    menu_index = menu.show()

    if options[menu_index] == add_new_dir:
        dir_nickname = input('Enter Directory Nickname: ')

        dir_path = input('Enter Directory Path: ')
        print()

        confirm = ['Yes', 'No']
        confirm_menu = TerminalMenu(confirm)
        confirm_menu_index = confirm_menu.show()

        if confirm[confirm_menu_index] == 'Yes':
            add_dir_info(dir_nickname, dir_path)
            print('\t(New directory info added)\n')

    elif options[menu_index] == remove_dir:
        saved_dirs = get_dirs_names()
        saved_dirs.append(exit_menu)

        if len(saved_dirs) > 0:
            saved_dirs_menu = TerminalMenu(saved_dirs)
            saved_dirs_menu_index = saved_dirs_menu.show()

            if saved_dirs[saved_dirs_menu_index] != exit_menu:
                remove_dir(saved_dirs[saved_dirs_menu_index])
                print('(Directory removed)\n')

        else:
            print('(No saved directories found in the directory list!)\n')

    elif options[menu_index] == change_dir:

        if len(get_dirs_names()) > 0:
            saved_dirs = get_dirs_names()
            saved_dirs.append(exit_menu)
            saved_dirs_menu = TerminalMenu(saved_dirs)
            saved_dirs_menu_index = saved_dirs_menu.show()

            if saved_dirs[saved_dirs_menu_index] != exit_menu:
                os.chdir(get_dir_path(saved_dirs[saved_dirs_menu_index]))
                current_dir = os.getcwd()

                print('Current Directory Path: ' + current_dir + '\n')

        else:
            print('(No saved directories found in the directory list!)\n')

    elif options[menu_index] == get_dir_info:
        print('Absolute Path: ' + current_dir + '\n')

        print(os.listdir())
        print()

    elif options[menu_index] == get_file_location:
        file_name = input('File Name (example.txt): ')
        print()

        if os.path.isfile(file_name):
            print('\tAbsolute Path: ' + os.path.join(os.getcwd(), file_name) + '\n')

        else:
            print('\t' + invalid_input + '\n')

    elif options[menu_index] == create_file:
        file_name = input('File Name (example.txt): ')
        print()

        if os.path.exists(file_name):
            print('\t(File already exists!)\n')

        else:
            new_file = open(os.path.join(os.getcwd(), file_name), 'w')
            new_file.close()

            print('\t(File successfully created)\n')

    elif options[menu_index] == rename_file:
        old_file_name = input('Old File Name (example.txt): ')

        if os.path.isfile(old_file_name):
            new_file_name = input('New File Name (example.txt): ')
            print()

            try:
                os.rename(old_file_name, new_file_name)
                print('\tFile Renamed\n')
            except:
                print('\t' + invalid_input + '\n')

        else:
            print('\t' + invalid_input + '\n')

    elif options[menu_index] == delete_file:
        file_name = input('Enter File Name (example.txt): ')
        print()

        if os.path.isfile(file_name):
            os.remove(file_name)

        else:
            print('\t' + invalid_input + '\n')

    elif options[menu_index] == delete_all_files:
        confirm = input('Confirm? (Yes or No): ')
        print()

        if confirm == 'Yes':
            total_files_deleted = 0

            for file in os.listdir():
                if os.path.isfile(file):
                    os.remove(file)
                    total_files_deleted += 1

            print('\t(' + str(total_files_deleted) + ' files deleted)\n')

    elif options[menu_index] == delete_type_of_files:
        file_type = input("Enter File Type (Example: txt): ")
        print()

        total_files_deleted = 0

        for file in os.listdir():
            if os.path.isfile(file) and file.endswith(file_type):
                os.remove(file)
                total_files_deleted += 1

        print('\t(' + str(total_files_deleted) + ' files deleted)\n')

    elif options[menu_index] == delete_files_with_specific_size:
        file_sizes = ['bytes', 'KB', 'MB', 'GB', 'TB', close_program]
        file_sizes_menu = TerminalMenu(file_sizes)
        file_size_index = file_sizes_menu.show()

        if file_sizes[file_size_index] != close_program:

            estimate_file_size = ['<', '>', '=', '>=', '<=', close_program]
            estimate_file_size_menu = TerminalMenu(estimate_file_size)
            estimate_file_size_index = estimate_file_size_menu.show()

            if estimate_file_size[estimate_file_size_index] != close_program:

                try:
                    input_file_size = float(input('File Size (Example: 10): '))
                    print()

                    converted_to_bytes = input_file_size

                    if file_sizes[file_size_index] == 'KB':
                        converted_to_bytes *= 1024

                    elif file_sizes[file_size_index] == 'MB':
                        converted_to_bytes *= math.pow(1024, 2)

                    elif file_sizes[file_size_index] == 'GB':
                        converted_to_bytes *= math.pow(1024, 3)

                    elif file_sizes[file_size_index] == 'TB':
                        converted_to_bytes *= math.pow(1024, 4)

                    total_files_deleted = 0

                    for file in os.listdir():
                        if os.path.isfile(file):
                            file_size = os.path.getsize(file)

                            if estimate_file_size[estimate_file_size_index] == '=':
                                if file_size == converted_to_bytes:
                                    os.remove(file)
                                    total_files_deleted += 1

                            elif estimate_file_size[estimate_file_size_index] == '<':
                                if file_size < converted_to_bytes:
                                    os.remove(file)
                                    total_files_deleted += 1

                            elif estimate_file_size[estimate_file_size_index] == '>':
                                if file_size > converted_to_bytes:
                                    os.remove(file)
                                    total_files_deleted += 1

                            elif estimate_file_size[estimate_file_size_index] == '<=':
                                if file_size <= converted_to_bytes:
                                    os.remove(file)
                                    total_files_deleted += 1

                            elif estimate_file_size[estimate_file_size_index] == '>=':
                                if file_size >= converted_to_bytes:
                                    os.remove(file)
                                    total_files_deleted += 1

                            print('\t(' + total_files_deleted + ' files deleted)\n')

                except:
                    print('\t' + invalid_input + '\n')

    elif options[menu_index] == create_dir:
        dir_name = input('Enter Directory Name: ')
        print()

        if len(dir_name) > 0:
            os.mkdir(dir_name)
            print('\t(Directory successfully created)\n')

        else:
            print('\t(Directory must have a name!)\n')

    elif options[menu_index] == delete_dir:
        dir_name = input('Enter Directory Name: ')
        print()

        if os.path.isdir(dir_name):
            os.rmdir(dir_name)
            print('\t(Directory deleted)\n')

        else:
            print("\t(Directory doesn't exist!)\n")

    elif options[menu_index] == sort_filenames_numerically:
        num_order = ['Yes', 'No']
        num_order_menu = TerminalMenu(num_order)
        num_order_menu_index = num_order_menu.show()

        if num_order[num_order_menu_index] == 'Yes':

            order_name = input("Order File Name (Don't write file extension): ")
            print()

            file_num = 1

            for file_name in os.listdir():

                if os.path.isfile(file_name):
                    extension = os.path.splitext(file_name)[1]
                    os.rename(file_name, order_name + str(file_num) + extension)

                    file_num += 1

    else:
        break
