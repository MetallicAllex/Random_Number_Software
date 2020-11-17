dim array(66)
dim last, idx, rand_num, str

last = ubound(array) - 1

for idx = 0 to last
    array(idx) = idx + 1
next

randomize()

for idx = last to 0 step -1
  rand_num = int( idx * rnd )
  str = str & array( rand_num ) & " "
  array(rand_num) = array( idx )
next

msgbox str