# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 10:19:49 2021

@author: vcheplyg
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import helpers



'''
grow sapling to initiate tree growth ------------------------------------
'''
def grow_sapling():
    
    data = {'old_x': [0],  # sapling grows from the origin
            'old_y': [0],   # sapling grows from the origin
            'new_x': [0], # sapling doesn't grow horizontally
            'new_y': [1],  # sapling does grow vertically
            'angle': [90], # angle from horizontal is 90 degrees
            'scale': [1]  # length of the sapling is 1
            }
    sapling = pd.DataFrame(data)
    return sapling




'''
grow a single tip -------------------------------------------------------

tips is a dataframe 
param is a dict

does not append, only finds parameters

'''
def grow_from(tips, param):
    
  all_scales = param['scales'] 
  all_angles = param['angles']  

  # mutate the tips tibble
  new_growth = tips.copy()
  
  #for i, new_growth in new_tips.iterrows():
      
  new_growth['old_x'] = new_growth['new_x']  # begin where last seg ended
  new_growth['old_y'] = new_growth['new_y']     # begin where last seg ended
     
  new_growth['scale'] = helpers.adjust_scale(new_growth['scale'], all_scales)    # change segment scale
  new_growth['angle'] = helpers.adjust_angle(new_growth['angle'], all_angles)   # change segment angle
      
  new_growth['new_x'] = helpers.adjust_x(new_growth['old_x'], new_growth['scale'], new_growth['angle'])
  new_growth['new_y'] = helpers.adjust_y(new_growth['old_y'], new_growth['scale'], new_growth['angle'])
      

  return new_growth
 
    
'''
grow one tip into multiple new tips (or branches) -----------------------

appends branches to existing DF
'''
def grow_multi(tips, param):
    
    branches = pd.DataFrame()
    
    for i in np.arange(1, param['splits']):
        branch = grow_from(tips, param)
        branches = branches.append(branch)
    
    return branches

'''
accumulate (multi-tip) growth over several cycles -----------------------

appends branches 

'''
def grow_tree(param):
    
    tree = grow_sapling()
    
    for i in np.arange(1,param['cycles']):
        multi = grow_multi(tree, param)
        tree = tree.append(multi)
        
    print(tree.head())
    return tree


'''
draw a picture of a tree ------------------------------------------------

'''

def draw_tree(tree):
    
    # Put the coordinates on the plot
    for i, row in tree.iterrows():
        x = [row['old_x'], row['new_x']]
        y = [row['old_y'], row['new_y']]
        plt.plot(x,y)


    # Make things pretty 
    plt.show()
    