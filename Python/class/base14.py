# ファイル出力、追記

file_path = 'resources/output.csv'

f = open(file_path,mode='w',encoding='utf-8',newline='\n')
f.write('あああ\nいいい')

with open(file_path,mode='w',encoding='utf-8',newline='\n') as f:
    list_a = [
        ['A','B','c'],
        ['あ','い','う']
    ]
    f.writelines(list_a[0])