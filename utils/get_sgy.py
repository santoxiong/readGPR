import os
import fnmatch
import shutil  # 支持跨磁盘移动文件


# find all sgy files in a directory and its subdirectories and move them to a new directory
def getSGYFiles(rootDir, newDir):
    for dirName, subdirList, fileList in os.walk(rootDir):
        for file in fileList:
            if fnmatch.fnmatch(file, '*.sgy'):
                print('Found sgy file %s' % os.path.join(dirName, file))
                shutil.move(os.path.join(dirName, file), os.path.join(newDir, file))
                print('Moved to %s' % os.path.join(newDir, file))
                continue
            else:
                continue
    return


if __name__ == '__main__':
    sgy_files_path = 'D:/88'
    sgy_save_path = '/data/sgy'
    if not os.path.exists(sgy_save_path):
        os.makedirs(sgy_save_path)
    getSGYFiles(sgy_files_path, sgy_save_path)
