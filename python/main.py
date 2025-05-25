import os

root_path = r'C:\Users\stsch\Documents\Feuerwehr'
if __name__ == '__main__':
    #tuple_subdir = os.walk(root_path)
    #print(type(tuple_subdir))
    #for subdir in tuple_subdir:
        #print(type(subdir))
        #print(subdir)
    # Get list of subdirectories and files of root_path (not recursive)
    list_dir = os.listdir(root_path)
    print(os.path.isdir(root_path))
    for name in list_dir:
        #first create full path name, e.g. C:\\Users\\stsch\\Documents\\Feuerwehr\10 Sichern gegen Absturz
        full_name = os.path.join(root_path,name)
        #check if entry is dir
        if os.path.isdir(full_name):
            #replace whitespace with underscore
            new_name = full_name.replace(' ','_')
            os.rename(full_name,new_name)
        #print(name + ' | ' + os.path.isdir(os.path.realpath(name)).__str__())
        #name_new = name.replace(' ', '_')
        #src = os.path.join(root_path)
        #os.rename()


    #path = input('Enter the path of your files:')
    #print(path)
    #files = os.listdir(path)
    #for file in files:
    #    file.
    #    print(file)
