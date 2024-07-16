def decimal_to_binary(dec_val:int):
    if dec_val<2:
        return str(dec_val)
    else:
        return decimal_to_binary(dec_val//2)+decimal_to_binary(dec_val%2)


if __name__ == '__main__':
    print(decimal_to_binary(11546541213))