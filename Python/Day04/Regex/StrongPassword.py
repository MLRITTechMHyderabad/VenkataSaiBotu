import re
passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]
for password in passwords:
    l = len(password)
    has_upper = re.search('[A-Z]',password)
    has_lower = re.search('[a-z]',password)
    has_num = re.search('[0-9]',password)
    has_special = re.search('[#@!$%*?&]',password)
    if l >= 8 and has_upper and has_lower and has_special and has_num :
        print(password,'->','Valid')
    else:
        print(password,'->','Invalid')