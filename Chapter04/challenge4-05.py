def ten(shin):
    try:
        return float(shin)
    except ValueError:
        print("フルカウンター")
        return None  #エラー時にNoneと返す

c = ten("55.0")
print(c)
