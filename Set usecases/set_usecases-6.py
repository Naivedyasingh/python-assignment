# 6.you're buildinga program to analyze customer purchase patterns. write a pyhton program to find the set of unique products frequently purchased together in given set of transation

def find_ferquent_sets():
    transations=[{'milk','bread','butter'},{'bread','butter'},{'milk','bread'},{'milk','bread','butter'},{'bread'}]
    
    freq={}
    for i in range(len(transations)):
        for j in range(i+1,len(transations)):
            common=transations[i] & transations[j]
            if len(common)>=2:
                key=frozenset(common)
                freq[key]=freq.get(key,0)+1
    for itemset,count in freq.items():
        if count>=2:
            print(set(itemset))            


find_ferquent_sets()