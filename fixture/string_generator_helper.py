import random
import string

class StringGeneratoHelper:

    def get_random_email(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2,3)))
        email = 'testliveedu_' + first_part+"@"+secondpart+"."+domain_part
        #email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type1(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part + secondpart + "." + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type2(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part +'@'+ secondpart
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type3(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part+'іваіва'+'@'+ secondpart + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type4(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = 'testliveedu_' + first_part + ' ' + '@' + secondpart + "." + domain_part
        # email = first_part + '@' + 'carbtc.net'

        return email

    def get_random_incorrect_email_type5(self):
        first_part = ''.join(random.choice(string.ascii_lowercase) for i in range(20))
        secondpart = ''.join(random.choice(string.ascii_lowercase) for i in range(5))
        domain_part = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(2, 3)))
        email = ""
        # email = first_part + '@' + 'carbtc.net'user = app.user_parse.parse_user_properties(resp_dict={'email': email})
        return email

    def get_random_two_passwords(self):
        password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(8, 20)))
        password2 = password1

        return [password1, password2]

    def get_random_two_passwords_not_the_same(self):
        password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(8, 20)))
        password2 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(8, 20)))

        return [password1, password2]

    def get_random_two_passwords_numeric(self):
        password1 = random.randint(10000000, 100000000000)
        password2 = password1

        return [password1, password2]

    def get_random_two_passwords_short(self):
        password1 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 7)))
        password2 = password1

        return [password1, password2]

    def get_random_two_passwords_uppercase_lowercase_the_same(self):
        password1 = ''.join(random.choice(string.ascii_uppercase) for i in range(random.randint(8, 30)))
        password2 = password1.lower()

        return [password1, password2]

    def get_random_username(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(10, 20)))

        return username
    def get_random_username_short(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1, 2)))

        return username

    def get_random_username_long(self):
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(30, 60)))

        return username