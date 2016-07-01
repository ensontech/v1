###########################################################
### This is the matrix of python functions that run V1 on the client! ###
###########################################################

### The following modules need to be imported first ###

import sys

### From here, we have the actual functions ###

### This function returns the name of the platform the script is running on ###

def detectplatform():
    if sys.platform == 'linux2':
        return "linux"
    elif sys.platform == 'win32':
        return "windows"
    elif sys.platform == 'linux4':
        return "android"
    elif sys.platform == 'darwin':
        return "mac"
    else:
        return "unrecognised"


### END OF FILE ###
