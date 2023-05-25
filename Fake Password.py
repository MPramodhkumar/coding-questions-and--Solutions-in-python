t = int(input())
places = 2
while t > 0:
    password = input()
    fake_password = input()
    # for left rotation
    lf = fake_password[:places]
    lr = fake_password[places:]
    duplicate = lr + lf

    # for right
    rf = fake_password[: len(fake_password) - places]
    rr = fake_password[len(fake_password) - places :]
    duplicate1 = rr + rf

    if password == duplicate or password == duplicate1:
        print("Yes")
    else:
        print("No")
    t = t - 1
