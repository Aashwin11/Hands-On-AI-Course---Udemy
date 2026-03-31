#74-raise-your-own-errors : Custom esceptions

def brew_chai(flavor):
    if flavor not in ["masala","ginger","elaichi"]:
        raise ValueError("The falvour does not exist")
    print(f"Brewing the flavor {flavor}")

brew_chai("mint")