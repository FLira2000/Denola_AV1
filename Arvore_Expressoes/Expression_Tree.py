from typings import List

class Expression_Tree:
    root = None
    level = 0
    _list_chunk_reducer = lambda lst, chunk_size: [lst[i * chunk_size:(i + 1) * chunk_size] for i in range((len(lst) + chunk_size - 1) // chunk_size)]
    _parser = lambda exp: list(filter(lambda e: e != '', exp.split('|')))

    def __init__(self, exp: str):
        self._parser(exp)
