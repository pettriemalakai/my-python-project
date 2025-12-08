def count_lines_with_word(filename, word):
    try:
        count = 0
        word_lower = word.lower()

        with open(filename, "r") as file:
            for line in file:
                if word_lower in line.lower():
                    count += 1

        return count

    except FileNotFoundError:
        return 0


#Question 2 
class BankAccount:
    """
    A simple bank account class.
    """

    def __init__(self, owner_name, initial_balance=0):
        """
        Initialize a bank account.
        Parameters:
            owner_name (str): Name of account owner
            initial_balance (float): Starting balance (default 0)
        """
        # Store owner_name and balance as instance variables
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Add money to the account.
        Parameters:
            amount (float): Amount to deposit
        Returns:
            float: New balance after deposit
        """
        # Add amount to balance if amount is positive
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Remove money from the account if sufficient funds exist.
        Parameters:
            amount (float): Amount to withdraw
        Returns:
            float: New balance after withdrawal
            Returns current balance unchanged if insufficient funds
        """
        # Check if balance >= amount
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self.balance

    def get_balance(self):
        """
        Get current balance.
        Returns:
            float: Current balance
        """
        return self.balance


# Test code (don't modify):
# account = BankAccount("John", 100)
# print(account.deposit(50))     # Should print: 150
# print(account.withdraw(30))    # Should print: 120
# print(account.withdraw(200))   # Should print: "Insufficient funds" then 120



#Question 3
def safe_calculate(num1, num2, operation):
    """
    Perform arithmetic operation with exception handling.
    """

    try:
        n1 = float(num1)
        n2 = float(num2)

        if operation == '+':
            return n1 + n2
        elif operation == '-':
            return n1 - n2
        elif operation == '*':
            return n1 * n2
        elif operation == '/':
            return n1 / n2   

    except ValueError:
        return "Error: Invalid number"
    except ZeroDivisionError:
        return "Error: Division by zero"

#Question 4 

def is_palindrome_recursive(s):
    """
    Check if a string is a palindrome using recursion.
    Ignore spaces and case.
    """
    s = s.replace(" ", "").lower()

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome_recursive(s[1:-1])


# Test your function:
print(is_palindrome_recursive("racecar"))                      # True
print(is_palindrome_recursive("hello"))                        # False
print(is_palindrome_recursive("A man a plan a canal Panama"))  # True
print(is_palindrome_recursive(""))                             # True
print(is_palindrome_recursive("a"))                            # True

#Question 5
def analyze_grades(students):
    """
    Analyze student grades using map, filter, and lambda functions.
    """
    
    # Step 1: Calculate average for each student
    student_averages = list(map(lambda s: (s[0], sum(s[1]) / len(s[1])), students))

    # Step 2: Filter passing students (average >= 70)
    passing = list(filter(lambda s: s[1] >= 70, student_averages))

    # Step 3: Filter failing students (average < 70)
    failing = list(filter(lambda s: s[1] < 70, student_averages))

    # Step 4: Find student with highest average
    highest = max(student_averages, key=lambda s: s[1])[0]

    # Step 5: Calculate class average
    class_avg = sum(map(lambda s: s[1], student_averages)) / len(student_averages)

    return {
        'passing': [s[0] for s in passing],
        'failing': [s[0] for s in failing],
        'highest': highest,
        'class_average': round(class_avg, 1)
    }


# Test your function:
test_data = [
    ('Alice', [85, 90, 88]),
    ('Bob', [60, 65, 62]),
    ('Charlie', [75, 80, 77]),
    ('Diana', [95, 92, 94])
]

# result = analyze_grades(test_data)
# print(result)
