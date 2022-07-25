# Functions file containing the workhorses for it all
import time

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def userInput(option: str):
    print('Instructions:')
    print('plain/cipher/unknown texts can only contain alphabetical and spaces')
    print('key can only contain numbers')
    text = input(f"Input the {option}\n")
    key = input("Provide the key:\n(Enter 0 if unknown)\n")
    text = text.upper()
    try:
        key = int(key)
    except ValueError:
        print('INCORRECT VALUE ENTERED FOR KEY')
        return -1

    return [text, key, option]


def cipherMachine(data):
    if data == -1:
        return
    text = list(data[0])
    letterKey = []
    newText = []
    blankStr = ""
    for i in range(0, len(text), 1):
        if text[i] == ' ':
            letterKey.append(-1)
        else:
            for j in range(0, len(alphabet), 1):
                if text[i] == alphabet[j]:
                    letterKey.append(j)

    if data[2] == 'plaintext' or 'ciphertext':
        for j in letterKey:
            tempInt = 0
            tempSum = j + data[1]
            tempNeg = j - data[1]
            if data[2] == 'plaintext':
                if j == -1:
                    newText.append(' ')
                elif tempSum > 25:
                    tempInt = tempSum - 26
                else:
                    tempInt = tempSum
                if j != -1:
                    newText.append(alphabet[tempInt])
            if data[2] == 'ciphertext':
                if j == -1:
                    newText.append(' ')
                else:
                    newText.append(alphabet[tempNeg])
        print(blankStr.join(newText))
    if data[2] == 'unknown':
        for i in range(0, len(alphabet), 1):
            tempList = []
            for k in range(0, i, 1):
                tempList.append(' ')
            for j in letterKey:
                tempInt = 0
                tempSum = j + i
                if j == -1:
                    tempList.append(' ')
                elif tempSum > 25:
                    tempInt = tempSum - 26
                else:
                    tempInt = tempSum
                if j != -1:
                    tempList.append(alphabet[tempInt])
            print(blankStr.join(tempList))


def stateMachine():
    stateRunnerBool = True
    while stateRunnerBool:
        try:
            data = input(
                'Select a integer from following options:\n(0): plaintext encryption\n(1): ciphertext decryption\n(2): unknown text decryption\n(3): Exit\n')
            if int(data) == 0:
                userData = userInput('plaintext')
                print('Plaintext Encoded')
                cipherMachine(userData)
                print('')
            if int(data) == 1:
                userData = userInput('ciphertext')
                print('Cipher Text Decoded')
                cipherMachine(userData)
                print('')
            if int(data) == 2:
                userData = userInput('unknown')
                print('Unknown Possibilities')
                cipherMachine(userData)
                print('')
            if int(data) == 3:
                stateRunnerBool = False
                print(f"Exiting Program.")
                print("................")
                time.sleep(.2)
                print("......Happy.....")
                time.sleep(.2)
                print("...Encrypting...")
                time.sleep(.2)
                print("................")
                time.sleep(.2)
        except ValueError:
            print('INCORRECT VALUE ENTERED')


# Program Runner!

stateMachine()
