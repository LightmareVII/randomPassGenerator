import random
import string

def generatePass(numberOfPasswords=1,
                 passwordLength=0):

    passwordList = []

    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    nums = [x for x in range(15, 31)]

    for x in range(numberOfPasswords):
        if passwordLength == 0:
            num = random.choice(nums)
        else:
            num = passwordLength
        passwordList.append(''.join(random.choice(chars) for i in range(num)))

    return passwordList