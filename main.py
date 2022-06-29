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
delete_files_start_end_with = 'Delete Files That Starts/Ends With Character(s)'
create_dir = 'Create Directory'
delete_dir = 'Delete Directory'
sort_filenames_numerically = 'Sort File Names With Numbers'
sort_filenames_of_file_type_numerically = 'Sort File Names Of A File Type Numerically'
capitalize_filenames = 'Un/Capitalize File and Directory Names'
close_program = '[x] Close'
exit_menu = '[x] Exit'
cancel = '[x] Cancel'
confirm_option = 'Confirm?'

current_dir = ''
invalid_input = '(Invalid Input!)'

options = [add_new_dir, remove_dir, change_dir, get_dir_info, get_file_location, create_file, rename_file, delete_file, delete_all_files, delete_type_of_files, delete_files_with_specific_size, create_dir, delete_dir, sort_filenames_numerically, sort_filenames_of_file_type_numerically, delete_files_start_end_with, capitalize_filenames]
options.sort()
options.append(close_program)

menu = TerminalMenu(options)

print()

create_database()
if len(get_dirs_names()) > 0:
    current_dir = get_current_dir_path()

    if len(current_dir) > 0:
        os.chdir(current_dir)
        print('Current Directory Path: \n')
        print('\t' + current_dir + '\n')

while True:
    menu_index = menu.show()

    if options[menu_index] == add_new_dir:
        dir_nickname = input('Enter Directory Nickname: ')

        dir_path = input('Enter Directory Path: ')
        print()

        confirm = [confirm_option, cancel]
        confirm_menu = TerminalMenu(confirm)
        confirm_menu_index = confirm_menu.show()

        if confirm[confirm_menu_index] == confirm_option:
            add_dir_info(dir_nickname, dir_path)
            print('\t(New directory info added)\n')

    elif options[menu_index] == remove_dir:
        saved_dirs = get_dirs_names()
        saved_dirs.append(exit_menu)

        if len(saved_dirs) > 0:
            saved_dirs_menu = TerminalMenu(saved_dirs)
            saved_dirs_menu_index = saved_dirs_menu.show()

            if saved_dirs[saved_dirs_menu_index] != exit_menu:
                remove_dir_directory_list(saved_dirs[saved_dirs_menu_index])
                print("(Directory '{}' removed from directory list)\n".format(saved_dirs[saved_dirs_menu_index]))

        else:
            print('(No saved directories found in the directory list!)\n')

    elif options[menu_index] == change_dir:

        if len(get_dirs_names()) > 0:
            saved_dirs = get_dirs_names()
            saved_dirs.append(exit_menu)
            saved_dirs_menu = TerminalMenu(saved_dirs)
            saved_dirs_menu_index = saved_dirs_menu.show()

            if saved_dirs[saved_dirs_menu_index] != exit_menu:
                if os.path.isdir(get_dir_path(saved_dirs[saved_dirs_menu_index])):
                    os.chdir(get_dir_path(saved_dirs[saved_dirs_menu_index]))
                    current_dir = os.getcwd()

                    print('Current Directory Path: ' + current_dir + '\n')

                else:
                    print("(Directory doesn't exist anymore!)\n")

        else:
            print('(No saved directories found in the directory list!)\n')

    elif options[menu_index] == get_dir_info:
        print('Absolute Path: \n')
        print('\t' + current_dir + '\n')

        print(os.listdir())
        print()

    elif options[menu_index] == get_file_location:
        file_name = input('File Name (example.txt): ')
        print()

        if len(file_name) > 0:
            if os.path.isfile(file_name):
                print('\tAbsolute Path: ' + os.path.join(os.getcwd(), file_name) + '\n')

            else:
                print("\t(File doesn't exist in the directory!)\n")

        else:
            print('\t(Must enter a file name!)\n')

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

        if len(old_file_name) > 0:
            if os.path.isfile(old_file_name):
                new_file_name = input('New File Name (example.txt): ')
                print()

                try:
                    os.rename(old_file_name, new_file_name)
                    print('\tFile Renamed\n')
                except:
                    print('\t' + invalid_input + '\n')

            else:
                print("\n\t(File doesn't exist in the directory!)\n")

        else:
            print('\n\t(Must enter a file name!)\n')

    elif options[menu_index] == delete_file:
        file_name = input('Enter File Name (example.txt): ')
        print()

        if len(file_name) > 0:
            if os.path.isfile(file_name):
                os.remove(file_name)

            else:
                print('\t' + invalid_input + '\n')

        else:
            print('\t(Must enter a file name!)\n')

    elif options[menu_index] == delete_all_files:
        confirm = [confirm_option, cancel]
        confirm_menu = TerminalMenu(confirm)
        confirm_menu_index = confirm_menu.show()
        print()

        if confirm[confirm_menu_index] == confirm_option:
            total_files_deleted = 0

            for file in os.listdir():
                if os.path.isfile(file):
                    os.remove(file)
                    total_files_deleted += 1

            print('\t(' + str(total_files_deleted) + ' files deleted)\n')

    elif options[menu_index] == delete_type_of_files:
        file_type = input("Enter File Type (Example: txt): ")
        print()

        if len(file_type) > 0:
            total_files_deleted = 0

            for file in os.listdir():
                if os.path.isfile(file) and file.endswith(file_type):
                    os.remove(file)
                    total_files_deleted += 1

            print('\t(' + str(total_files_deleted) + ' files deleted)\n')

        else:
            print('\t(Must enter a file name!)\n')

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

        if len(dir_name) > 0:
            if os.path.isdir(dir_name):
                os.rmdir(dir_name)
                print('\t(Directory deleted)\n')

            else:
                print("\t(Directory doesn't exist!)\n")

        else:
            print('\t(Directory must have a name!)\n')

    elif options[menu_index] == sort_filenames_numerically:

        order_name = input("Order File Name (Don't write file extension): ")
        print()

        if len(order_name) > 0:
            name_exists = False

            for file_name in os.listdir():
                if os.path.isfile(file_name):
                    if os.path.splitext(file_name)[0] == order_name:
                        name_exists = True
                        break

            if name_exists:
                print('\t(File name already exists, the name must be different from the names in the directory!)\n')

            else:
                file_num = 1

                for file_name in os.listdir():

                    if os.path.isfile(file_name):
                        extension = os.path.splitext(file_name)[1]
                        os.rename(file_name, order_name + str(file_num) + extension)

                        file_num += 1

    elif options[menu_index] == sort_filenames_of_file_type_numerically:

        file_type = input('File Type (example: txt): ')
        print()

        if len(file_type) > 0:
            order_name = input('\tOrder Name: ')
            print()

            if len(order_name) > 0:
                file_num = 1;

                for file_name in os.listdir():
                    if os.path.isfile(file_name):
                        if file_name.endswith(file_type):
                            extension = os.path.splitext(file_name)[1]
                            os.rename(file_name, order_name + str(file_num) + extension)

                            file_num += 1

            else:
                print('\t\t(Must enter a order name!)\n')

        else:
            print('\t(Must enter a file type!)\n')

    elif options[menu_index] == delete_files_start_end_with:

        side = ['Starts With', 'Ends With', exit_menu]
        side_menu = TerminalMenu(side)
        side_menu_index = side_menu.show()

        if side[side_menu_index] != exit_menu:

            characters = input('Enter Character(s): ')
            print()

            if len(characters) > 0:

                total_files_deleted = 0

                for file_name in os.listdir():
                    if os.path.isfile(file_name):

                        if side[side_menu_index] == 'Starts With':
                            if os.path.splitext(file_name)[0].startswith(characters):
                                os.remove(file_name)
                                total_files_deleted += 1

                        elif side[side_menu_index] == 'Ends With':
                            if os.path.splitext(file_name)[0].endswith(characters):
                                os.remove(file_name)
                                total_files_deleted += 1

                print('\t(' + str(total_files_deleted) + ' files deleted)\n')

            else:
                print('\t(Must enter character(s))\n')

    elif options[menu_index] == capitalize_filenames:
        only_files = 'Only Files'
        only_folders = 'Only Folders'
        both_type = 'Both'

        type_to_capitalize = [only_files, only_folders, both_type, cancel]
        type_to_capitalize_menu = TerminalMenu(type_to_capitalize)
        type_to_capitalize_menu_index = type_to_capitalize_menu.show()

        if type_to_capitalize[type_to_capitalize_menu_index] != cancel:

            cap_all_chars = 'Capitalize All The Characters'
            cap_first_char = 'Capitalize The First Character Only'
            uncap_all_chars = 'Uncapitalize All The Characters'

            capitalize = [cap_all_chars, cap_first_char, uncap_all_chars, cancel]
            capitalize_menu = TerminalMenu(capitalize)
            capitalize_menu_index = capitalize_menu.show()

            if capitalize[capitalize_menu_index] != cancel:

                for type in os.listdir():
                    if capitalize[capitalize_menu_index] == cap_all_chars:
                        if type_to_capitalize[type_to_capitalize_menu_index] == only_files or type_to_capitalize[type_to_capitalize_menu_index] == both_type:
                            if os.path.isfile(type):
                                os.rename(type, os.path.splitext(type)[0].upper() + os.path.splitext(type)[1])

                        if type_to_capitalize[type_to_capitalize_menu_index] == only_folders or type_to_capitalize[type_to_capitalize_menu_index] == both_type:
                            if os.path.isdir(type):
                                os.rename(os.path.splitext(type)[0], os.path.splitext(type)[0].upper())

                    elif capitalize[capitalize_menu_index] == cap_first_char:
                        if type_to_capitalize[type_to_capitalize_menu_index] == only_files or type_to_capitalize[type_to_capitalize_menu_index] == both_type:
                            if os.path.isfile(type):
                                os.rename(type, os.path.splitext(type)[0].capitalize() + os.path.splitext(type)[1])

                        if type_to_capitalize[type_to_capitalize_menu_index] == only_folders or type_to_capitalize[type_to_capitalize_menu_index] == both_type:
                            if os.path.isdir(type):
                                os.rename(os.path.splitext(type)[0], os.path.splitext(type)[0].capitalize())

                    else:
                        if type_to_capitalize[type_to_capitalize_menu_index] == only_files or type_to_capitalize[type_to_capitalize_menu_index] == both_type:
                            if os.path.isfile(type):
                                os.rename(type, os.path.splitext(type)[0].lower() + os.path.splitext(type)[1])

                        if type_to_capitalize[type_to_capitalize_menu_index] == only_folders or type_to_capitalize[type_to_capitalize_menu_index] == both_type:
                            if os.path.isdir(type):
                                os.rename(os.path.splitext(type)[0], os.path.splitext(type)[0].lower())

    else:
        break
