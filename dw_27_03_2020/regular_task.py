import re


class InvalidLeftSideException(Exception):
    pass


class InvalidRightSideException(Exception):
    pass


class InvalidBothSidesException(Exception):
    pass


class EmailChecker:
    EMAIL_REGEX = r'^(?P<left_side>[a-zA-Z0-9_\-\.]+|(?P<left_error>.*))@' \
                  r'(?P<right_side>[a-zA-Z0-9_\-\.]+\.[a-zA-Z]{2,5}|(?P<right_error>.*))$'

    def check_email(self, string):
        temp = re.compile(self.EMAIL_REGEX)
        res = temp.match(string).groupdict()
        if res['left_error'] is not None and res['right_error'] is not None:
            raise InvalidBothSidesException(f"Email is invalid ({res['left_error']} @ {res['right_error']})")
        elif res['left_error'] is not None:
            raise InvalidLeftSideException(f"Left side of entered email ({res['left_error']}) is invalid")
        elif res['right_error'] is not None:
            raise InvalidRightSideException(f"Right side of entered email ({res['right_error']}) is invalid")
        else:
            return f'Valid email ({string})'


if __name__ == '__main__':
    checker = EmailChecker()
    with open('emails.txt') as file:
        for line in file:
            try:
                print(checker.check_email(line))
            except Exception as e:
                print(e)
