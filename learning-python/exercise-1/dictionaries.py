#used alot in python to store different types of data
monthConversions = {
    "Jan": "January",
    "Jan": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
    0: "Zero",
    1: "One",
    }

print(monthConversions["Nov"])
print(monthConversions.get("Mar"))
print(monthConversions.get("Mqtt", "Not a valid key"))

#exercises for practise

