35. 文本颜色设置

#### 只需要用时候会能找到，会调用即可
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC
