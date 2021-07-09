def test_var_args(farg, *args):
    print("formal arg:", farg)
    for arg in args:
        print("another arg:", arg)

test_var_args(1, "two", 3)


def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another kw arg: {}:{}".format(key,kwargs[key]))
test_var_kwargs(1,myarg2="two", myarg3=3)


