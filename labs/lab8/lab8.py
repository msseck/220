"""
Name:Marietou Seck
lab8.py
"""


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, "r")
    out_file = open(out_file_name, "w")
    acc = 0
    for line in in_file:
        words = line.split()
        for word in words:
            acc = acc + 1
            print(acc, word, file=out_file)
    in_file.close()
    out_file.close()


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        lines = line.split()
        first_name = lines[0]
        last_name = lines[1]
        wage = float(lines[2])
        hours_worked = int(lines[3])
        print(first_name, last_name, (float(wage) + 1.65) * hours_worked, file=out_file)
    in_file.close()
    out_file.close()


def calc_check_sum(isbn):
    check_sum = 0
    for i in range(10):
        isb_num = int(isbn[i]) * (10-i)
        check_sum += isb_num
    print(check_sum)


def send_message(file, friend):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    message = in_file.read()
    print(message, file=out_file)
    in_file.close()
    out_file.close()


def encode(message, key_value):
    empty = ""
    for ch in message:
        letter = ord(ch) + key_value
        empty += chr(letter)
    return empty


def encode_better(message, cipher_key):
    empty = ""
    for i in range(len(message)):
        letter = ord(message[i]) + ord(cipher_key[i % len(cipher_key)]) - 97
        empty += chr(letter)
    return empty


def send_safe_message(file, friend, key):
    in_file = open(file, 'r')
    out_file = open(friend + '.txt', 'w')
    message = in_file.read()
    secret = encode_better(message, key)
    print(secret, file=out_file)
    in_file.close()
    out_file.close()


def main():
    number_words('walrus.txt', 'wal_output.txt')
    hourly_wages('hourly_wages.txt', 'hourly_wages_output.txt')
    calc_check_sum('0072946520')
    send_message('message.txt', 'bob')
    send_safe_message('secret_message.txt', 'katy', 'pad.txt')

    pass


main()
