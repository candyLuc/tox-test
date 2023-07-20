from math import fabs, ceil


# 返回绝对值
def math_fabs(x):
    return fabs(x)


# 返回上入整数
def math_ceil(x):
    return ceil(x)


if __name__ == '__main__':
    print(math_fabs(-1.2))
    print(math_ceil(-2.3))
