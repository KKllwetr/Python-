def SearchQuestions(_list=[]):
    _new_list = []
    for i in range(len(_list)):
        if str(_list[i]).isdigit():
            _new_list.append(_list[i])
        elif str(_list[i]).replace(".", "").isdigit():
            _new_list.append(_list[i])
        elif str(_list[i]).replace(",", "").isdigit():
            _new_list.append(_list[i])
    return _new_list
