def str_to_binrep(c_arr: str) -> str:
    out_arr = []

    for c in c_arr:
        if c == ' ':
            o_str = '/'
        else:
            o_bin = bin(ord(c))
            o_str = o_bin[2::]

        out_arr.append(o_str)

    return ' '.join(out_arr)


def str_to_hexrep(c_arr: str) -> str:
    out_arr = []

    for c in c_arr:
        if c == ' ':
            o_str = '/'
        else:
            o_hex = hex(ord(c))
            o_str = o_hex[2::]

        out_arr.append(o_str)

    return ' '.join(out_arr)


while True:
    text = input("Enter some text: ")
    print(str_to_binrep(text) + '\n' + str_to_hexrep(text) + '\n')
