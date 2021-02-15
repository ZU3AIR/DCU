def get_counts_dict(data):
    Dict = {}
    for term in data:
        if len(term) not in Dict:
            Dict[len(term)] = 1
        else:
            Dict[len(term)] += 1
    return Dict