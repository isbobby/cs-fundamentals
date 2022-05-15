from disjoint_sets import DisjointSet

test_case_1 = [
    ("init", 8),
    ("union", 4, 5),
    ("union", 6, 7),
    ("union", 4, 6),
    ("find", 1),
    ("find", 5)
]
result_1 = [1, 4, [-1, -1, -1, -1, -1, 4, 4, 6]]

def test(commands, result):
    disjset = None
    res = []
    for cmd in commands:
        if cmd[0] == "init":
            disjset = DisjointSet(cmd[1])
        elif cmd[0] == "union":
            disjset.simpleUnionSets(cmd[1], cmd[2])
        elif cmd[0] == "find":
            res.append(disjset.find(cmd[1]))
    
    res.append(disjset.s)
    return res == result

print(f"TEST1 CORRECT : {test(test_case_1, result_1)}")