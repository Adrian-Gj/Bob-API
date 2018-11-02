import os
import libs.send2trash

def mkdir(name):
    try:
        os.makedirs(name)
    except OSError:
        return 
def copy(src, dst, symlinks=False, ignore=None):
    x = os.path.basename(src)
    y = dst + ""
    if os.path.isdir(src):
        shutil.copytree(src, os.path.join(dst,x), symlinks, ignore)
    else:
        shutil.copy2(src, dst)

