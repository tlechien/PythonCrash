"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""
if __name__ == '__main__':
    list_msg = ["This", "is", "pointless", "..."]
    new_msg = list_msg.copy()

    def show_messages(msgs):
        print(*msgs, sep="\n")

    def send_messages(msgs):
        sent = []
        while msgs:
            print(msgs[0])
            sent.append(msgs[0])
            msgs.pop(0)
        return sent

    print("initial list:")
    show_messages(list_msg)
    print("transfer process:")
    sent_msg = send_messages(new_msg)
    print("sent_msg list:")
    print(sent_msg)
    print("rest:")
    print(new_msg)
    print("archive")
    print(list_msg)

