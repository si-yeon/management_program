import os

if __name__ == '__main__':
    name1 = 'view_login'
    name2 = 'view_membership'
    name3 = 'view_check'
    name4 = 'view_connect'

    os.system(f'python -m PyQt5.uic.pyuic -x {name1}.ui -o {name1}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name2}.ui -o {name2}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name3}.ui -o {name3}.py')
    os.system(f'python -m PyQt5.uic.pyuic -x {name4}.ui -o {name4}.py')

