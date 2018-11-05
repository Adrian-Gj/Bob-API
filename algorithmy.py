from process import *
import math
import random 
def search_dict(key,dict):
    possible = [key]
    possible.append(q_t1_proc(key))

    segments = q_t1_proc(key).split(" ")
    keys = list(dict.keys())

    possible += segments
    for k in keys:
        for p in possible:
            if p in k:
                return k

