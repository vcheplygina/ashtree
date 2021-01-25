# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:44:28 2021

@author: vcheplyg
"""

import workers


#test_grow_sapling()

    
param = {'seed': 3,
        'cycles': 3,
        'splits': 2,
        'scales': [0.5, 0.8, 0.9, 0.95],
        'angles': [-10, -5, 0, 5, 15, 20, 25]
        }


t = workers.grow_tree(param)
workers.draw_tree(t)


    

def test_grow_sapling():
    s = workers.grow_sapling()
    workers.draw_tree(s)
    
    
def test_grow_from():
    s = workers.grow_sapling()
    t = workers.grow_from(s,param)
    
    tree = s.append(t)    
    
    print(tree.head())
    workers.draw_tree(tree)
    
    
def test_grow_multi():
    s = workers.grow_sapling()
    b = workers.grow_multi(s,param)
    
    t = workers.grow_from(b,param)
       
    #print(tree.head())
    workers.draw_tree(t)
    
    
