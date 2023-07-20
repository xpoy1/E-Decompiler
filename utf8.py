import os
import codecs


for file_name in os.listdir(r'E:\xpoy\tools\debugger\IDA_Pro_7.6\plugins\esig'):
    if file_name.endswith(('.cpp', '.h', '.esig')):
        path= os.path.join(r'E:\xpoy\tools\debugger\IDA_Pro_7.6\plugins\esig', file_name)
        try:
            with codecs.open(path, 'r', 'gb2312') as file:
                content = file.read()
        except UnicodeDecodeError:
            with codecs.open(path, 'r', 'utf-8-sig') as file:
                content = file.read()
        with codecs.open(path, 'w', 'UTF-8') as file:
            file.write(content)