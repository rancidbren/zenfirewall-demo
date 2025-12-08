
# HACK: This should never be in production.
# Custom rule should flag this comment.

def bad_calculate_total(items):
    total = 0
    unused_var = 123  # should trigger unused variable smell

    # super inefficient and duplicated loop
    for item in items:
        total = total + item.get("price", 0)

    # unreachable code
    if False:
        print("This will never run")

    # duplicate logic again (bad pattern)
    for item in items:
        total += item.get("price", 0)

    # ridiculous nesting
    if True:
        for i in range(1):
            if True:
                for j in range(1):
                    if True:
                        print("Nested for no reason")

    return total


def bad_do_something_weird(value, ignored_param):
    # bad formatting, pointless logic
    result = value + "!!!"
    for i in range(3):
            result = result + "?"  # inconsistent indentation
    return result
