import os
def dirUser(userId):
    uId = str(userId)

    if __name__ != '__main__':
        mainPath = os.path.abspath(os.getcwd())
        print(mainPath)
        myBotUsersPath = f'{mainPath}/cache/multiUse/Users'
    elif __name__ == '__main__':
        myBotUsersPath = 'D:/Ruslan/2. Work/ТГУ/multiBot/cache/multiUse/Users'

    userDir = myBotUsersPath + f'/{uId}'
    print(userDir)
    if os.path.isdir(userDir):
        print('Директория пользователя существует')
    else:
        print('Директория пользователя не существует')
        os.makedirs(userDir+'/cache', 0o754)
        with open(f'{userDir}/cache/flag_RSP.txt', 'w') as flagRSP_file:
            flagRSP_file.write('False')
        with open(f'{userDir}/cache/flag_echo.txt', 'w') as flagEcho_file:
            flagEcho_file.write('False')

        print('Директория пользователя создана')
    return uId

if __name__ == '__main__':
    dirUser()