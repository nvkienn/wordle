def generate_all_outcomes():
    core = ["G", "Y", "B"]
    res = {}
    for a in core:
        for b in core:
            for c in core:
                for d in core:
                    for e in core:
                        res[a + b + c + d + e] = 0
    return res
