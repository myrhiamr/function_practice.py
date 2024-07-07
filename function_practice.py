def hello():
    print("Hello, user!")


def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {lunch_list[0]}")
        for item in lunch_list[1:]:
            print(f"Next I eat {item}")


hello()
packed_list = pack("apple", "sandwich", "cookie")
print(packed_list)

eat_lunch(["apple", "sandwich", "cookie"])
eat_lunch([])