import os
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='change-name-file-dir'
    )
    parser.add_argument('path', help='Enter the path of directory or file')
    args = parser.parse_args()
    print(args.path)
    # Get list of subdirectories and files of root_path (not recursive)
    list_dir = os.listdir(args.path)
    for name in list_dir:
        #first create full path name
        full_name = os.path.join(args.path,name)
        print(full_name)
        #check if entry is dir
        if os.path.isdir(full_name):
            #replace whitespace with underscore
            new_name = full_name.replace(' ','_')
            #os.rename(full_name,new_name)
        #print(name + ' | ' + os.path.isdir(os.path.realpath(name)).__str__())
        #name_new = name.replace(' ', '_')
        #src = os.path.join(root_path)
        #os.rename()

if __name__ == '__main__':
    main()
