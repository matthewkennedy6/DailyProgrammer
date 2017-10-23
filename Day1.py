#Day 1 Hard

min_guess = -1
max_guess = 101
guess = 50

while True:
    ri = input("I guess your number is " + str(guess) + ".  Is it (h)igher, (l)ower, or (c)orrect?")
    if(ri == "h"):
        min_guess = guess
        guess = guess + int(0.5*(max_guess-guess))
    if(ri == "l"):
        max_guess = guess
        guess = int(min_guess + int(0.5*(guess-min_guess)))
    if(ri == "c"):
        break

exit()

#Day 1 Intermediate


def print_schedule(sched):
    print(sched)
    return


def delete_event(sched):
    print(sched)

    time = int(input("Enter the time of the event you'd like to delete"))
    del sched[time]

    return sched


def edit_event(sched):

    print(sched)

    time = int(input("Enter the time of the event you'd like to edit"))
    description = input("Enter the new description for the event")
    sched[time] = description

    return sched


def add_event(sched):
    time = int(input("Enter a time"))
    description = input("Enter a description for the event")
    sched[time] = description

    return sched

schedule = {}
while True:
    key = input("Choose an option (a)dd, e(dit), d(elete), p(rint), q(uit)")
    if key == "a":
        schedule = add_event(schedule)
    if key == "e":
        schedule = edit_event(schedule)
    if key == "d":
        schedule = delete_event(schedule)
    if key == "p":
        print_schedule(schedule)
    if key == "q":
        break

exit()

#Day 1 Easy

#print("What is your name?")
name = input("What is your name?")
age = input("What is your age?")
uname = input("What is your username?")

print("your name is " + name + ", you are " + age + " years old, and your username is " + uname)