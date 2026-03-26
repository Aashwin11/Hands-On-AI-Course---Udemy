# Docuemnting Built-in Functions

def chai_flavour(flavour="Masala"):
    """Return flavour""" # tRIPLE QUOTES FUNCTION
    return flavour

print(chai_flavour.__doc__) # Function documentation string - Whatever written in """" -> The 1st line of the function should be in """"
print(chai_flavour.__name__)# Return function name


help(len)


def generate_bill(chai=0,samomsa=0):
    """ Calculate total bill : Chai and samosa
    :param chai: Number of chai cups
    :param samosa: Number of samosa
    :return: (total amount, thankyou message)
    """
    total=chai*10+samomsa*2
    return total, "Thankyou"

print(generate_bill.__doc__)
print(generate_bill(1,2))


