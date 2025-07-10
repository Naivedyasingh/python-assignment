s="mjsibfjs"
check=""
for ch1 in s:
    if ch1 not in check:
       count=0
       for ch2 in s:
           if ch1==ch2:
              count+=1
       print(ch1+"=" +str(count)  )     
       check+=ch1