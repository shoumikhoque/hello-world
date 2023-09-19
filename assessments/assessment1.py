def isOneBitCharacter( bits):
    if len(bits) == 1:
        return True
    if len (bits)==2 :
        if bits==[0,0]:
            return True
        else:
            return False
    for i in range(len(bits)-1):
        print(bits[i])
        i+=6


if __name__ == '__main__':
    print("Hello World!")
    isOneBitCharacter( [1, 1, 0, 1, 1, 1,0,0])