import os

if __name__ == '__main__':
    name1 = 'view_login'
    name2 = 'view_membership'
    name3 = 'view_check'
    name4 = 'view_connect'
    name5 = 'view_main'
    name6 = 'view_register'
    name7 = 'view_take'

    os.system(f'python -m PyQt5.uic.pyuic -x {name1}.ui -o {name1}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name2}.ui -o {name2}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name4}.ui -o {name4}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name5}.ui -o {name5}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name6}.ui -o {name6}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name7}.ui -o {name7}.py')

