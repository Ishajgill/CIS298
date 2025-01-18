import math
'''
college_credits_needed = int(input("How many college credits you need?"))
credits_completed = int(input("How many credits you have completed?"))
credits_taking_per_semester = int(input("Credits taken per semester"))
credits_remaining = int(college_credits_needed - credits_completed)
semesters_needed = (math.ceil(credits_remaining/credits_taking_per_semester))
RATE = 600
def tuition_to_be_paid(college_credits_needed, credits_completed):
    if credits_taking_per_semester < 12:
        print("Tuition is ",RATE * credits_remaining  )
    else:
        print("Tuition is ",math.floor(credits_remaining/credits_taking_per_semester)*7200 + (credits_remaining % credits_taking_per_semester*RATE))

print(tuition_to_be_paid(120,60))

def print_numbers():
    for num in range(1,100):
        if num % 3 == 0:
            print("Fuzz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

print_numbers()
'''
def is_palindrome(word):



