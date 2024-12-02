# Write a program that saves user inputs in a list. The program stop asking the
# user to enter a word when the user doesn't enter anything (presses Enter).
user_inputs = []
while user_input := input("Enter something: "):
    user_inputs.append(user_input)

print(user_inputs)

# Rewrite the following code using walrus operator:
budget = 100
total = 0

while (expense := float(input("Enter an expense (or -1 to quit): "))) != -1:
    if (total := total + expense) > budget:
        print(f"Budget exceeded! Total: ${total:.2f}")
        break

    print(f"Current total: ${total:.2f}, "
          f"Remaining budget: ${budget - total:.2f}")


# Imagine you have users coming from three different sources, in different
# formats:
# {"name": "Jane Addams"}
# {"full_name": "Jane Addams"}
# {"first_name": "Jane", "last_name": "Addams"}
# Write a function that can extract a user's first name.

def extract_first_name(user):
    if name := (user.get("name") or user.get("full_name")):
        return name.split()[0]
    elif first_name := user.get("first_name"):
        return first_name


print(extract_first_name({"name": "Jane Addams"}))
print(extract_first_name({"full_name": "Jane Addams"}))
print(extract_first_name({"first_name": "Jane", "last_name": "Addams"}))
