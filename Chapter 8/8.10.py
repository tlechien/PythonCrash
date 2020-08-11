"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""
if __name__ == '__main__':
    list_msg = ["This", "is", "pointless", "..."]

    def show_messages(msgs):
        print(*msgs, sep="\n")

    def send_messages(msgs):
        sent = []
        while msgs:
            print(msgs[0])
            sent.append(msgs.pop(0))
        return sent

    print("initial list:")
    show_messages(list_msg)
    print("transfer process:")
    sent_msg = send_messages(list_msg)
    print("sent_msg list:")
    print(sent_msg)
    print("rest:")
    print(list_msg)
