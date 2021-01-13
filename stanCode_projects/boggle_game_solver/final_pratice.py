
def main():
    lst = [2, 2, 3, 3, 5]
    target = 9
    print(can_make_sum(lst, target))

def can_make_sum(lst, target):
    ans = []
    helper(lst, [], target, ans)
    if len(ans) == 0:
        return False
    else:
        return True

def helper(lst, ans_lst, target, ans):
    if sum(ans_lst) == target:
        ans.append(ans_lst)
        return
    else:
        for ele in lst:
            if count(ele, ans_lst) < count(ele, lst):
                if sum(ans_lst)+ele <= target:
                    ans_lst.append(ele)
                    helper(lst, ans_lst, target, ans)
                    ans_lst.pop()
            else:
                pass

def count(ele, lst):
    n = 0
    for e in lst:
        if e == ele:
            n += 1
        else:
            pass
    return n
















if __name__ == '__main__':
    main()