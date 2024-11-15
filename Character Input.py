USER_NAME = str(input("What is your name:\n "))
USER_AGE = int(input("What is your age: \n"))
CURRENT_YEAR = 2024
YEARS_TO_HUNDRED = 100 - USER_AGE
YEAR_USER_IS_HUNDRED = CURRENT_YEAR + YEARS_TO_HUNDRED

print(f"Hello {USER_NAME} you will be 100 years old at year {YEAR_USER_IS_HUNDRED} ")
