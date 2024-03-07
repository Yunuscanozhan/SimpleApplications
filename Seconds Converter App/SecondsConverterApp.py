# SecondsConverter App:

print("Welcome to the SecondsConverter App!")
print()
print("Please enter the number of seconds you wish to convert (or type 'exit' to quit).")
print()
while True:
    str_seconds = input("Enter seconds: ")

    if str_seconds.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break

    total_secs = int(str_seconds)

    hours = total_secs // 3600
    secs_still_remaining = total_secs % 3600
    minutes = secs_still_remaining // 60
    secs_finally_remaining = secs_still_remaining % 60
    print()
    print("Hrs = ", hours, "Mins = ", minutes, "Secs = ", secs_finally_remaining)
    print()
    print("Would you like to convert another time? (Type 'exit' to quit)")
