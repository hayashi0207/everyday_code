# 論理型

from werkzeug.formparser import is_valid_multipart_boundary
# 論理型

is_man=True
is_adult=False

if is_man and is_adult:
    print('成人男性')

if is_man or is_adult:
    print('男性か大人')
