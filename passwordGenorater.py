import random
import pyperclip
import argparse


def setupArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('--minAlpha', help='Minimum alphabetical characters to generate', type=int, default=8)
    parser.add_argument('--maxAlpha', help='Maximum alphabetical characters to generate', type=int, default=8)
    parser.add_argument('--minNum', help='Minimum numerical characters to generate', type=int, default=3)
    parser.add_argument('--maxNum', help='Maximum numerical characters to generate', type=int, default=3)
    parser.add_argument('--minSym', help='Minimum symbolic characters to generate', type=int, default=2)
    parser.add_argument('--maxSym', help='Maximum symbolic characters to generate', type=int, default=2)

    parser.add_argument('-p', '--private', help='Hide password in the console window', action='store_true')

    args = parser.parse_args()

    '''Handling error prone input'''
    if args.minAlpha > args.maxAlpha:
        args.maxAlpha = args.minAlpha + (args.minAlpha*0.5)
    if args.minNum > args.maxNum:
        args.maxNum = args.minNum + (args.minNum*0.5)
    if args.minSym > args.maxSym:
        args.maxSym = args.minSym + (args.minSym*0.5)

    return args


def generatePass(args):
    password = ""

    symbols = []
    nums = []
    alphabet = []

    for letter in range(97, 123):
        alphabet.append(chr(letter))

    for symbol in range(33, 47):
        symbols.append(chr(symbol))

    for symbol in range(58, 64):
        symbols.append(chr(symbol))

    for num in range(48, 57):
        nums.append(chr(num))

    for x in range(random.randint(args.minAlpha, args.maxAlpha)):
        password = password + random.choice(alphabet)
    for x in range(random.randint(args.minNum, args.maxNum)):
        password = password + random.choice(nums)
    for x in range(random.randint(args.minSym, args.maxSym)):
        password = password + random.choice(symbols)
    return password


if __name__ == '__main__':

    args = setupArgs()

    password = generatePass(args)

    if not args.private:
        print(password)
    else:
        print('**************')

    pyperclip.copy(password)
    print("the password was copied to your clipboard")
    print("Quick Tip: Use a password manager")
    print("These passwords are hard to memorize")
