"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
"""
if __name__ == '__main__':
    dic = {
        'Amazon': 'Bresil',
        'Nile': 'Egypt',
        'Danube': 'Germany'
    }

    for river in dic:
        print("The {} runs through {}.".format(river, dic[river]))

    for river in dic:
        print(river)

    for river in dic:
        print(dic[river])