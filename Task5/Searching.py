def SearchQuestions(_list=[]):
    _new_list = {}
    _endOfText = ".!?"
    _intermediate_list = []

    for i in range(len(_list)):
        _intermediate_list.append(_list[i])
        if "?" in _intermediate_list[len(_intermediate_list) - 1]:
            _new_list.update({len(_new_list) + 1: ' '.join(_intermediate_list)})
            _intermediate_list.clear()
        elif "." in _intermediate_list[len(_intermediate_list) - 1] or "!" in _intermediate_list[
            len(_intermediate_list) - 1]:
            _intermediate_list.clear()
        else:
            continue
    lis = [v for v in _new_list.values()]
    return lis
