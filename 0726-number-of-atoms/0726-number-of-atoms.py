class Solution:
    def countOfAtoms(self, formula: str) -> str:
        count = defaultdict(int)

        def helper(i, j, M):
            c = i
            while c < j:
                if formula[c].isupper():  # case of a aton name
                    name = formula[c]
                    c += 1
                    while c < j and formula[c].islower():  # go to find all of the name
                        name += formula[c]
                        c += 1
                    # test if this atom has a multiplicity
                    num = 1
                    if c < j and formula[c].isdigit():
                        num = formula[c]
                        c += 1
                        while (
                            c < j and formula[c].isdigit()
                        ):  # go to find all of the miltiplicity
                            num += formula[c]
                            c += 1
                    # now we have evry thing so its good let add it into our count
                    count[name] += M * int(num)
                elif formula[c] == "(":  # we have the case of the inside-formula
                    a = 1
                    c += 1
                    start = c
                    # go until the end of the inside-formula
                    while a:
                        if formula[c] == "(":
                            a += 1
                        elif formula[c] == ")":
                            a -= 1
                        c += 1
                    end = c - 1
                    # get the miltiplicity
                    num = 1
                    if c < j and formula[c].isdigit():
                        num = formula[c]
                        c += 1
                        while (
                            c < j and formula[c].isdigit()
                        ):  # go to find all of the miltiplicity
                            num += formula[c]
                            c += 1
                    helper(start, end, M * int(num))

        helper(0, len(formula), 1)
        count = {k: count[k] for k in sorted(count)}
        res = ""
        for k, v in count.items():
            res += k + (str(v) if v > 1 else "")
        return res
