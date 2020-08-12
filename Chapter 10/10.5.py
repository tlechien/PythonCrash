"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""
if __name__ == '__main__':
    with open("reasons.txt", "a") as file:
        reason = True
        while reason:
            reason = input("Why do you like programming? ")
            if reason: file.write(reason + "\n")
