# Introduction
# In a parallel universe not too distant from our own, Julius Caesar finds himself locked in a fierce conflict with Genghis Khan.

# Legend has it that Khan's armies were renowned for their mastery of horseback archery, a formidable advantage in battle. To level the playing field, divine intervention granted Caesar a helping hand.

# With divine assistance, Big Jul gained the ability to impart his knowledge to his troops, a boon bestowed upon all of his men. He could impart any skill he possessed to those who lacked it.

# Skills, in this universe, are represented by the binary representation of an integer. Each bit corresponds to a specific skill, with 1 denoting proficiency and 0 representing ignorance.

# Using his wisdom, Caesar could transform any 0 to a 1 if he himself possessed the corresponding skill.

# Armed with the value n, representing his own skills, Caesar sets out to enhance the abilities of his troops, numbering from 1 to n. Time is of the essence as the threat of the approaching Asian cavalry looms ever closer.

# Task
# Given a positive integer n, return the sum of the Bitwise OR operation between n and all integers from 1 to n (both inclusive). In fancy math terms: 
# ∑
# �
# =
# 1
# �
# �
# ∣
# �
# ∑ 
# i=1
# n
# ​
#  n∣i, where | is the Bitwise OR operation.

# Performance
# Brute force solutions, yielding a time complexity of O(n), won't work.

# The expected time complexity is O(logn). Most solutions with a time complexity equal or close to that should pass with ease.

# Random Tests: 100
# Integer Size: 1 to 10 ** 100
# Examples
# 1 -> 1
# 2 -> 5
# 3 -> 9
# 4 -> 22
# 10 -> 121
# 100 -> 11302

#GAVE UP LOL
def or_sum(n: int) -> int:
  result = 0
  bit_position = 0

  while n > 0:
      # Count the number of set bits at the current position
      count_set_bits = (n + 1) // 2

      # Add the contribution of the current position to the result
      result += count_set_bits * (1 << bit_position)

      # Move to the next bit position
      bit_position += 1
      n //= 2

  return result