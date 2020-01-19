#coding:utf-8
'''
This program replaces the characters in all the names of files and directories
at your will
'''
import logging
#logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(level = logging.INFO,format = '[%(levelname)s] - %(message)s')
logger = logging.getLogger(__name__)

import os  

def rename_all_scanner(file_dir='.',original=' ',replaced='_',tasks=[]):
    '''renames everything in file_dir
    including sub-directoires and items in sub-directories
    substituting the oringinal string for replaced
    '''
    if file_dir.endswith('/'):
        file_dir=file_dir[:-1]  #去除目录最后的'/'
    
    for filename in os.listdir(file_dir):  #当前路径下所有子文件和子目录
        #print(filename) 

        full_filename=file_dir+'/'+filename
        if os.path.isdir(full_filename):#如果是目录，先进入这个目录，重命名内部文件
            tasks=rename_all_scanner(full_filename,original,replaced)

        #不论filename是不是目录，重命名当前目录或文件的filename
        new_filename=filename.replace(original,replaced)
        if new_filename!=filename:
            print(filename,'->',new_filename)
            #print(full_filename,'->',new_filename)
            tasks.append((full_filename,file_dir+'/'+new_filename))

    return tasks

def rename_all(file_dir='.',original=' ',replaced='_'):
    try:
        tasks=rename_all_scanner(file_dir,original,replaced)
        count=len(tasks)
        print('\n',count,'files or directories to rename')
        #tasks.reverse() #do not rename the directories first!
        print('\nWARNING: YOU ARE RENAMING YOUR FILES,\nSUBSTITUTING "'+original+'" for "'+replaced+'"','\nTHIS OPERATION IS NOT REVOKAVLE!\n')
        input("Press Ctrl+C to cancel, or press Enter to continue renaming\n")
        for task in tasks:
            os.rename(task[0],task[1])
            logger.info(task[0]+' -> '+task[1])
        return count
    except KeyboardInterrupt:
        print("renaming cancelled")

def prefix_numbers(file_dir='.',add_zero_prefix=True, digits=5):
    '''
    for all the files and directories with its name prefixed by a number,
    add 000... as prefix, or remove the prefixes
    
    Example of adding zero_prefix (with digits=5):
    1-LuoguPaintBoard.py -> 00001-LuoguPaintBoard.py
    Note that the program should scan the whole directory
    and adaptively add the digits when needed
    (e.g. digits=6 when finding a filename with a prefix number 186246).
    Example of removing zero_prefix:
    051-LuoguPaintBoard.py -> 51-LuoguPaintBoard.py
    '''
    if file_dir.endswith('/'):
        file_dir=file_dir[:-1]  #去除目录最后的'/'
    raise NotImplementedError

if __name__=='__main__':
    original,replaced=' ','_'
    print('\n',rename_all('.',original,replaced),'files and directories renamed\n')
    #prefix_numbers()
    input("Press ENTER to exit")
