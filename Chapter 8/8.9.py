"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""
if __name__ == '__main__':
    list_msg = ["This", "is", "pointless", "..."]

    def show_messages(msgs):
        print(*msgs, sep="\n")
    show_messages(list_msg)
