def rollback():
    words=input('请输入英语单词:')
    new_words=''.join(reversed(words))
    print(f'反转后的单词是{new_words}')
rollback()