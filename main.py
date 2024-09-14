import pandas as pd 
import numpy as np 

from module.hello import hello

def gen_df(n):
    df = pd.DataFrame(np.random.rand(n, 3), columns=['A', 'B', 'C'])
    return df 

def hello():
    print('hello world')

if __name__ == '__main__':
    hello()
    df = gen_df(10)
    print(df)
    input('press any key to exit')


#注释
# pyarmor-7 obfuscate main.py
# conda activate py39



# 打包
# https://pyarmor.readthedocs.io/zh/v5.7.0/examples.html

# 简单打包
# 打包前先删除文件夹
# Remove-Item -Recurse -Force "build"
# Remove-Item -Recurse -Force "dist"
# pyarmor-7 pack -e "-F --paths 'D:\project\工具开发\代码混淆' " main.py


# 分步打包

# 1.生成spec文件
# pyinstaller -F main.py
# pyinstaller main.spec

# pyinstaller --paths "D:\project\工具开发\代码混淆" main.py

# pyi-makespec -F --name 代码混淆 main.py 

# 2.删除文件夹
# Remove-Item -Recurse -Force "build"
# Remove-Item -Recurse -Force "dist"



#3.利用pack命令打包
# pyarmor-7 pack -s "main.spec" main.py






# pyarmor-7 pack -e " --name easy-han --hidden-import comtypes --add-data 'config.json;.'" \
#              -x " --exclude vnev --exclude tests" -s "easy-han.spec" main.py

