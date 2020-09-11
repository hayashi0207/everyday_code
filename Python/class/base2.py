# インスタンス変数、クラス変数

class SampleA():
    class_val = 'class val'

    def set_val(self):
        self.instance_val = 'instance val'
        
instance_a = SampleA()
instance_a.set_val()
print(instance_a.__class__.class_val)
instance_b=SampleA()
instance_b.set_val()
instance_b.print_val()
