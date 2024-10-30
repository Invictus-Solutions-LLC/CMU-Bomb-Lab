'''
File: solutions.py

Copyright: 2024, Blaise Aranador

Description:
    This file contains the code to generate the solutions file for
the publicly accessible Carnegie Mellon University's Bomb Lab

Lab Assignments: https://csapp.cs.cmu.edu/3e/labs.html
CMU Bomb Lab: https://csapp.cs.cmu.edu/3e/bomb.tar
'''


answers = []


# phase 1
# reads in string
# answer is a string
# match hardcoded string
answers.insert(0, 'Border relations with Canada have never been better.')


# phase 2
# reads in 6 digits
# answer is 6 numbers - space separated
# 1st number - match hardcoded value, 1; next number in sequence is twice the previous
answers.insert(1, '1 2 4 8 16 32')


# phase 3
# reads in 2 digits
# switch - 8 cases [0-7]
# answer is 2 numbers - space separated
# 1st number - switch case 0-7 inclusive, 1; 2nd number - match case's hardcoded value respectively, 311
answers.insert(2, '1 311')


# phase 4
# reads in 2 digits
# answer is 2 numbers - space separated
# 1st number - less than or equal to hardcoded value, 14, less than or equal to AND greater than or equal to hardcoded value, 7; 2nd number - match hardcoded value, 0
answers.insert(3, '7 0')


# phase 5
# reads in string
# answer is 6 characters
# each character will be masked with 0x0F which is used as an index for an array
# characters from array will be copied to another array and compared with the hardcoded string, flyers
# 0x6D is the only character in the array - index: 0
# 'aduiersnfotvbylSo you think you can stop the bomb with ctrl-c, do' string follows the array data
# access to first character in string will be index of 1
# indices to retrieve the characters in flyers, respectively: 9 (1001), 15 (1111), 14 (1110), 5 (0101), 6 (0110), 7 (0111)
# use ascii characters where last 4 bits match above: i (01101001), o (01101111), n (01101110), e (01100101), f (01100110), g (01100111)
# 9  (1001) == i (01101001) & 0x0F (00001111)
# 15 (1111) == o (01101111) & 0x0F (00001111)
# 14 (1110) == n (01101110) & 0x0F (00001111)
# 5  (0101) == e (01100101) & 0x0F (00001111)
# 6  (0110) == f (01100110) & 0x0F (00001111)
# 7  (0111) == g (01100111) & 0x0F (00001111)
answers.insert(4, 'ionefg')


# phase 6
# reads in 6 digits
# answer is 6 numbers - space separated
# all numbers are <= 6
# all numbers are unique
# new num = 7 - num
# numbers indicate node id
# order of node ids is the value of the nodes in decreasing order:
# 0x6032f0 <node3>:       924     3       6304512 0
# 0x603300 <node4>:       691     4       6304528 0
# 0x603310 <node5>:       477     5       6304544 0
# 0x603320 <node6>:       443     6       0       0
# 0x6032d0 <node1>:       332     1       6304480 0
# 0x6032e0 <node2>:       168     2       6304496 0
# need to substract the node id from the number 7 to get the input answer
# 1st number = 4, 2nd number = 3, 3rd number = 2, 4th number = 1, 5th = 6, 6th number = 5 
answers.insert(5, '4 3 2 1 6 5')


# phase secret
# within the phase_defused function
# 2 conditions to reach the secret phase
# 1) must have passed 6 phases
# 2) 3rd line in the answer file has the string ' DrEvil' appended to it
# 2 conditions to pass the secret phase
# 1) 7th line in the answer file is a number, <= 1001, used in recursive function, fun7
# 2) fun7 must return value == 2
# 3 conditions during recursion to have fun7 return 2
# 1) <= 36 , return value is added to itself
# 2) != 8 , return value adds 1 to itself
# 3) == 22, return value 0
# 0x6030f0 <n1>:  36      0       6304016 0
# 0x603100 <n1+16>:       6304048 0       0       0
# 0x603110 <n21>: 8       0       6304144 0
# 0x603120 <n21+16>:      6304080 0       0       0
# 0x603130 <n22>: 50      0       6304112 0
# 0x603140 <n22+16>:      6304176 0       0       0
# 0x603150 <n32>: 22      0       6304368 0
# 0x603160 <n32+16>:      6304304 0       0       0
# 0x603170 <n33>: 45      0       6304208 0
# 0x603180 <n33+16>:      6304400 0       0       0
# 0x603190 <n31>: 6       0       6304240 0
# 0x6031a0 <n31+16>:      6304336 0       0       0
# 0x6031b0 <n34>: 107     0       6304272 0
# 0x6031c0 <n34+16>:      6304432 0       0       0
# 0x6031d0 <n45>: 40      0       0       0
# 0x6031e0 <n45+16>:      0       0       0       0
# 0x6031f0 <n41>: 1       0       0       0
# 0x603200 <n41+16>:      0       0       0       0
# 0x603210 <n47>: 99      0       0       0
# 0x603220 <n47+16>:      0       0       0       0
# 0x603230 <n44>: 35      0       0       0
# 0x603240 <n44+16>:      0       0       0       0
# 0x603250 <n42>: 7       0       0       0
# 0x603260 <n42+16>:      0       0       0       0
# 0x603270 <n43>: 20      0       0       0
# 0x603280 <n43+16>:      0       0       0       0
# 0x603290 <n46>: 47      0       0       0
# 0x6032a0 <n46+16>:      0       0       0       0
# 0x6032b0 <n48>: 1001    0       0       0
# 0x6032c0 <n48+16>:      0       0       0       0
answers[3] += ' DrEvil'
answers.insert(6, '22')


# generate answer file
with open('./answers.txt', 'w') as f:
    for answer in answers:
        f.write(answer + '\n')
