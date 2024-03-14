import math

ruleset=str(input("""Please input your ruleset starting with x, it should be the same length as the password and in the following format.
             \n\nx means any digit is acceptable in its place\nu means it must be higher than the last one\nd means it must be lower than the last one
             \nIf the password was 5 digits long, the rule input could be xxddu\n\n>>> """))
input_password=str(input("\nNumerical Password (0-9 only)\n>>> "))

split_pass=[]
split_rules=[]
qmarklist=[]
positionbeforelist=[]
filtered_ruleset=[]
elements_removed=0

for i in input_password:
    split_pass.append(i)

for i in ruleset:
    split_rules.append(i)
    filtered_ruleset.append(i)

for i in range (len(split_rules)):
    if split_rules[i]=='?':
        qmarklist.append(i)

for i in qmarklist:
    positionbeforelist.append(i-1)
final_position_list = positionbeforelist+qmarklist

final_position_list.sort(reverse=True)
for i in final_position_list:
    elements_removed=elements_removed+1
    filtered_ruleset.pop(i)

print(filtered_ruleset)
print(split_rules)

#for i in range (elements_removed):
#    filtered_ruleset.append('x')
#print(filtered_ruleset)
#An alternative solution to the new checklist length not matching the password length.

def compare(list_position, list):
    error2='error2'
    error='error'
    ruletype=list[list_position]

    if ruletype=='x':
        pass

    elif ruletype=='u':

        if split_pass[list_position] > split_pass[list_position-1]:
            pass

        else:
            return error2

    elif ruletype=='d':

        if split_pass[list_position] < split_pass[list_position-1]:
            pass

        else:
            return error
        

# Adding some modifiers and general boundaries

if split_rules[0]=='u' or split_rules[0]=='d' or split_rules[0]=='?':
    print("Your ruleset cannot start with u, d, or ? ")
    exit()

for i in range (len(ruleset)):
    x=compare(i, split_rules)
    if x=='error' or x=='error2':
        break

if x=='error' or x=='error2':
    print("Error with first list")
    for i in range (len(filtered_ruleset)):
        y=compare(i,filtered_ruleset)
    if y=='error' or y=='error2':
        print("Error with second list")
        print("Password Invalid")
    else:
        print("Passed on second list")
else:
    print("Passed on first list")
    

    

