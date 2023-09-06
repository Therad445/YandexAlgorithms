memory = input()
x = input()
y = input()
z = input()


def clear_num(str_in):
    str_in = str_in.replace("+7", "8")
    new_str = ''
    for sym in str_in:
        if sym == "-" or sym == "(" or sym == ")":
            continue
        new_str = new_str + sym
    if len(new_str) == 7:
        new_str = "8495" + new_str
    return new_str


def check_base(mem, in_date):
    if in_date == mem:
        print("YES")
    else:
        print("NO")


check_base(clear_num(memory), clear_num(x))
check_base(clear_num(memory), clear_num(y))
check_base(clear_num(memory), clear_num(z))
