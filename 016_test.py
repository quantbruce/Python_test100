16.输出指定格式的日期。

import datetime


if __name__ == '__main__':
    # 普通格式输出
    print(datetime.date.today().strftime('%Y-%m-%d %H:%M:%S'))
    # 建立专门的时间对象
    date_object = datetime.date(1949, 10, 1)
    print(date_object.strftime('%Y-%m-%d'))
    # 时间加减运算
    date_another = date_object + datetime.timedelta(days=2)
    print(date_another.strftime('%Y-%m-%d'))
    # 时间替换运算
    date_replace = date_object.replace(year=date_another.year + 1)
    print(date_replace)
