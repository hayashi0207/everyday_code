# コンストラクタ、デストラクタ

class a :
    def __init__(self,msg):
        print('インスタンスが生成されました。')
        self.msg=msg
        print(self.msg)

    def __del__(self):
        print('デストラクタが実行されました。')
        print(self.msg)
b=a('hello')

