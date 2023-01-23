def push(stack, x):
    stack.append(x)


def pop(stack):
    size = len(stack)
    if size > 0:
        return stack.pop(size - 1)
    else:
        print('Underflow')


def peek(stack):
    size = len(stack)
    if size > 0:
        return stack[size - 1]
    else:
        print('Underflow')


def main():
    stack = []

    push(stack, 10)
    push(stack, 20)
    push(stack, 30)
    push(stack, 40)
    # 栈就像是是一个洞口向上的羽毛球筒，先进来的羽毛球就在最底部，后进来的元素就是顶部
    print('Top Element: ', peek(stack))
    pop(stack)      # 移除顶部元素
    print('Top Element: ', peek(stack))


if __name__ == '__main__':
    main()
