from .process import *
import math
import random 
def search_dict(key,dict):
    possible = [key]
    possible.append(q_t1_proc(key))

    segments = q_t1_proc(key).split(" ")
    keys = list(dict.keys())
    segments = [x for x in segments if x != "my"]
    segments = [x for x in segments if x != "of"]
    possible += segments
    #print(str(possible))
    for k in keys:
        for p in possible:
            if p==k:
                return k
            if p+" " in k:
                return k
            if " "+p in k:
                return k


