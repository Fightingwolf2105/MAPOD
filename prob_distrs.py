# Filename: prob_distrs.py

'''used for generating random variables
   assume all probabilistic variables be independent
   will keep updating the code later 
   '''

# Created: October/02/2017
# Last modified: October/05/2017
# Author: Xiaosong

import os
os.chdir('pyDOE-0.3.8')
print 'Installing pyDOE'
os.system('python setup.py install')
from pyDOE import lhs
print 'pyDOE installed successfully \n\n'
os.chdir('..')

import sys
from scipy import stats

def gen_exp(x_sample, x_prob):
    '''inputs:
       x_sample: contain samping method and # of samples, dictionary
       x_prob: contain random-variable information, dictionary
       outputs:
       x_design: required number of sample points, with specified sampling scheme
    '''
    
    # sample inputs with MCS or LHS
    if 'MCS' in x_sample:
        print 'Under construction!'
        print 'Now exiting, you will not get sample points'
        sys.exit()
    elif 'LHS' in x_sample:
        print 'Generating initial sample points, with LHS method'
        x_design = lhs(len(x_prob), samples = x_sample['LHS'])
    else:
        print 'Sampling method is not found, use LHS as default!'
        print 'Generating initail sample points'
        x_design = lhs(len(x_prob), samples = x_sample.values()[0])
        
    print 'Initial sample points generated successfully \n\n'
    
    i = 0
    for key, value in x_prob.iteritems():
        if key.startswith('Uniform'):
            x_design[:,i] = (value[1] - value[0]) * x_design[:,i] + value[0]
            i = i+1
            continue
            
        elif key.startswith('Gaussian'):
            loc = value[0]
            scale = value[1]
            x_design[:,i] = stats.norm(loc, scale).ppf(x_design[:,i])
            i = i+1
            continue
        else:
            print '{} distribution is still under construction' .format(key)
            print 'Now exiting, you will not get sample points'
            sys.exit()
    
    return x_design
    
def run_exp(full_model, x_experiment):
    print 'run_exp is under construction!'
    pass