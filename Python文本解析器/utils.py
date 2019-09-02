# encoding: utf-8

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'

def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        # 非空行,加到当前的block中
        if line.strip():
            block.append(line)
        # 遇到空行，将当前保存的block连接起来，然后block清空
        elif block:
            yield ''.join(block).strip()
            block = []