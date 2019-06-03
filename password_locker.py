import pyperclip

PASSWORDS = {
    'gmail': 'sdflkjsdflkjsdf',
    'naver': 'sdflkjsdfljfoiwerjiofwejoiwef',
    'facebook': '12345'
}

def main():
    site = input('input your site: ')

    password = PASSWORDS[site]

    if not password:
        print('not valid site.')
    else:
        pyperclip.copy(password)
        print('your password is copied')


main()