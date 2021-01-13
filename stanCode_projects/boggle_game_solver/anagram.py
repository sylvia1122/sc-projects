"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dic = []

def main():
    """
    this program could find all of the anagrams of the word the user key in
    """
    global dic
    print('Welcome to stanCode \"Anagram Generator\" (or ' + EXIT + ' to quit)')
    while True:
        dic = read_dictionary()  # lst
        word = input('Find anagrams for: ')
        print('Searching...')
        if word == EXIT:
            break
        else:
            dic = shrink_dic(word)
            maybe_ana = find_anagrams(word)  # lst
            ana = []
            for ele in maybe_ana:
                if ele in dic:
                    if ele in ana:
                        pass
                    else:
                        print('Found: ' + ele)
                        print('Searching...')
                        ana.append(ele)
            print(str(len(ana)) + ' anagrams: ' + str(ana))

def shrink_dic(word):
    """
    this program narrow down the list of the dictionary by choosing the word
    that has same digits of the word keyed in by the user
    :param word: str, keyed in by the user
    :return: lst, which only contains the words begin with the digit of the keyed-in word
    """
    new_dic = []
    shrink_helper(word, new_dic)
    return new_dic


def shrink_helper(word, new_dic):
    global dic
    for w in dic:
        for ch in word:
            if w[0] == ch:
                new_dic.append(w)
            else:
                pass



def read_dictionary():
    """
    this program could change the txt file into a python list
    """
    with open(FILE, 'r') as f:
        for line in f:
            line = line.split('\n')
            dic.append(line[0])
    return dic


def find_anagrams(s):
    """
    :param s: str, the word keyed in by the user
    :return: lst, which contains all of the anagrams of the word
    """
    ans_lst = []
    helper(s, '', len(s), ans_lst)
    return ans_lst

def helper(s, cur_s, ans_len, ans_lst):
    """
    :param s: str, the word keyed in by the user
    :param cur_s: str
    :param ans_len: int, the number of the digits of the word
    :param ans_lst: lst, which contains all of the anagrams of the word
    """
    # if len(cur_s) == ans_len:
    #     ans_lst.append(cur_s)
    # else:
    #     for ch in s:
    #         if count(ch, cur_s) < count(ch, s):
    #             cur_s += ch
    #             if has_prefix(cur_s):
    #                 helper(s, cur_s, ans_len, ans_lst)
    #                 cur_s = cur_s[0:len(cur_s) - 1]
    #             else:
    #                 cur_s = cur_s[0:len(cur_s) - 1]
    #         pass

    if len(cur_s) == ans_len:
        ans_lst.append(cur_s)
    else:
        for ch in s:
            if count(ch, cur_s) < count(ch, s):
                cur_s += ch
                helper(s, cur_s, ans_len, ans_lst)
                cur_s = cur_s[0:len(cur_s) - 1]
            else:
                pass

def count(ch, str):
    """
    this program could count the number of the chosen digit in a string
    :param ch: str, the chosen digit
    :param str: str, the string that being counted
    :return: int, times of the chosen digit appear
    """
    num = 0
    for i in range(len(str)):
        if str[i] == ch:
            num += 1
        else:
            pass
    return num


def has_prefix(sub_s):
    """
    this program could check if there is a word begins with the given string
    :param sub_s: str, the string given to be checked if there is a word begin with it
    :return: bool, true if there is a word begins with the given string
    """
    global dic
    n = 0
    for i in range(len(dic)):
        if dic[i].startswith(sub_s) is True:
            n += 1
        if n > 0:
            return True
    return False




if __name__ == '__main__':
    main()
