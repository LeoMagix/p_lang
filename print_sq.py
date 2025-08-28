"""Simple program that prints a square of length n to the command line.
   the user is asked to enter length."""

sq_len = int(input("Enter a number: "))

print("*"*sq_len)

for i in range(sq_len - 2):
    for j in range(1, sq_len + 1):
        if j == 1:
            print("*", end="")
        elif j == sq_len:
            print("*")
            #print()
        else:
            print(" ", end=" ")
    #print()
print("*"*sq_len)
