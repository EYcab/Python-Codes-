
__author__ = 'Chenxi'
# It is interesting to note that for integers greater than 0 and less than 10.
# (101/ 9) X 1=1
# (102/ 9) X 2=22
# (103/ 9) X 3=333
# (104/ 9) X 4=4444
# (105/ 9) X 5=55555
# (106/ 9) X 6=666666
# (107/ 9) X 7=7777777
# (108/ 9) X 8=88888888
# (109/ 9) X 9=999999999
#thus below is the code


for i in range(1,input()):
    print  i * 10**i / 9