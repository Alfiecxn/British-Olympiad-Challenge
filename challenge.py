import math
ruleset=str(input("""Please input your ruleset, it should be the same length as the password and in the following format.
             \n\nx means any digit is acceptable in its place\nu means it must be higher than the last one\nd means it must be lower than the last one
             \nIf the password was 5 digits long, the rule input could be xxddu\n\n>>> """))
input_password=str(input("\nNumerical Password (0-9 only)\n>>> "))
split_pass=[]
split_rules=[]
for i in input_password:
    split_pass.append(i)
for i in ruleset:
    split_rules.append(i)
print(split_pass)
print(split_rules)
def compare(list_position):
    passnum=split_pass[list_position]
    ruletype=split_rules[list_position]
    if ruletype=='x':
        pass
    elif ruletype=='u':
        if split_pass[list_position] > split_pass[list_position-1]:
            pass
        else:
            print("Password Invalid")
    elif ruletype=='d':
        if split_pass[list_position] < split_pass[list_position-1]:
            pass
        else:
            print("Password Invalid")
if len(ruleset) != len(input_password):
    print("your password and ruleset need to be the same length")
for i in range (len(ruleset)):
    compare(i)
