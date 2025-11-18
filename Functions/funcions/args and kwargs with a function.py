#  Concept:
# - *args → multiple positional arguments (tuple ban jaata hai)
# - **kwargs → multiple keyword arguments (dictionary ban jaata hai)


def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Raj", age=21)
