def get_total(ls):
    try:
        val = sum(ls)
    except Exception as e:
        print(e)
        return "There is something wrong with the input."

    return val

