"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

ans = 0

def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, inputted by the user
	:return: int, the largest digit
	"""
	global ans
	ans = 0
	if n < 0:
		n = -n
	helper(n)
	return ans

def helper(n):
	"""
	:param n: int, inputted by the user, which is always bigger than zero
	:return: int, the largest digit
	"""
	global ans
	if n == 0:
		return
	else:
		helper(n//10)
		n1 = n//10
		n2 = n - n1 * 10
		if n2 > ans:
			ans = n2












if __name__ == '__main__':
	main()
