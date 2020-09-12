CRED = '\033[91m'
CEND = '\033[0m'

# Reference: https://www.cs.cmu.edu/~02710/Lectures/ScoringMatrices2015.pdf

import utils
import numpy as np
import save

def generate(X, seqType, args):
    '''
    # Reference: repRNA
    :param X:
    :param seqType:
    :param args:
    :return:
    '''

    if seqType == 'DNA':
        d = {
            'GGG': [5.7000, 5.8500, 3.0000, 13.0000, 5.8270, 5.8270, 3.3110, 3.8680, 622.4000, 103.3887, 6.0000,3.5360, ],
            'GGA': [6.2000, 5.0000, 2.0000, -5.0000, 4.9907, 4.9907, 3.8190, 3.5810, 622.4000, 103.3887, 3.8000,4.7990, ],
            'GGC': [8.2000, 9.1000, 3.0000, 45.0000, 9.0823, 9.0823, 1.3870, 2.4480, 622.4000, 103.3887, 10.0000,1.3090, ],
            'GGT': [5.2000, 5.3000, 2.0000, 8.0000, 5.3160, 5.3160, 3.6190, 4.1560, 622.4000, 103.3887, 5.4000,3.8780, ],
            'GAG': [6.6000, 6.0000, 2.0000, 8.0000, 5.9806, 5.9806, 3.2210, 3.3530, 621.4000, 103.2226, 5.4000,3.8780, ],
            'GAA': [5.1000, 4.0500, 1.0000, -12.0000, 4.0633, 4.0633, 4.3850, 4.2140, 621.4000, 103.2226, 3.0000,5.2640, ],
            'GAC': [5.6000, 5.5000, 2.0000, 8.0000, 5.5164, 5.5164, 3.4980, 3.9250, 621.4000, 103.2226, 5.4000,3.8780, ],
            'GAT': [3.6000, 4.4500, 1.0000, 7.0000, 4.4432, 4.4432, 4.1530, 5.0870, 621.4000, 103.2226, 5.3000,3.9350, ],
            'GCG': [4.3000, 5.9000, 3.0000, 25.0000, 5.8914, 5.8914, 3.2750, 4.6780, 622.4000, 103.3887, 7.5000,2.6910, ],
            'GCA': [7.5000, 6.7500, 2.0000, 13.0000, 6.7553, 6.7553, 2.7540, 2.8420, 622.4000, 103.3887, 6.0000,3.5360, ],
            'GCC': [8.2000, 9.1000, 3.0000, 45.0000, 9.0823, 9.0823, 1.3870, 2.4480, 622.4000, 103.3887, 10.0000, 1.3090, ],
            'GCT': [6.3000, 6.9000, 2.0000, 25.0000, 6.8829, 6.8829, 2.6830, 3.5240, 622.4000, 103.3887, 7.5000,2.6910, ],
            'GTG': [6.8000, 6.6500, 2.0000, 17.0000, 6.6255, 6.6255, 2.8320, 3.2390, 621.4000, 103.2226, 6.5000,3.2530, ],
            'GTA': [6.4000, 5.0500, 1.0000, -6.0000, 5.0673, 5.0673, 3.7700, 3.4670, 621.4000, 103.2226, 3.7000,4.8570, ],
            'GTC': [5.6000, 5.5000, 2.0000, 8.0000, 5.5164, 5.5164, 3.4980, 3.9250, 621.4000, 103.2226, 5.4000,3.8780, ],
            'GTT': [1.6000, 2.6500, 1.0000, -6.0000, 2.6412, 2.6412, 5.2600, 6.2720, 621.4000, 103.2226, 3.7000,4.8570, ],
            'AGG': [4.7000, 5.0500, 2.0000, 8.0000, 5.0523, 5.0523, 3.7820, 4.4450, 622.4000, 103.3887, 5.4000,3.8780, ],
            'AGA': [6.5000, 4.9000, 1.0000, -9.0000, 4.8884, 4.8884, 3.8790, 3.4100, 622.4000, 103.3887, 3.3000,5.0890, ],
            'AGC': [6.3000, 6.9000, 2.0000, 25.0000, 6.8829, 6.8829, 2.6830, 3.5240, 622.4000, 103.3887, 7.5000,2.6910, ],
            'AGT': [2.0000, 3.9000, 1.0000, 11.0000, 3.9232, 3.9232, 4.4710, 6.0330, 622.4000, 103.3887, 5.8000,3.6500, ],
            'AAG': [4.2000, 4.7000, 1.0000, 6.0000, 4.6992, 4.6992, 3.9950, 4.7360, 621.4000, 103.2226, 5.2000,3.9920, ],
            'AAA': [0.1000, 0.0500, 0.0000, -36.0000, 0.0633, 0.0633, 6.8820, 7.1760, 621.4000, 103.2226, 0.0000,7.0450, ],
            'AAC': [1.6000, 2.6500, 1.0000, -6.0000, 2.6412, 2.6412, 5.2600, 6.2720, 621.4000, 103.2226, 3.7000,4.8570, ],
            'AAT': [0.0000, 0.3500, 0.0000, -30.0000, 0.3500, 0.3500, 6.6980, 7.2370, 621.4000, 103.2226, 0.7000,6.6240, ],
            'ACG': [5.2000, 5.3000, 2.0000, 8.0000, 5.3055, 5.3055, 3.6250, 4.1560, 622.4000, 103.3887, 5.4000,3.8780, ],
            'ACA': [5.8000, 5.5000, 1.0000, 6.0000, 5.4903, 5.4903, 3.5160, 3.8100, 622.4000, 103.3887, 5.2000,3.9920, ],
            'ACC': [5.2000, 5.3000, 2.0000, 8.0000, 5.3160, 5.3160, 3.6190, 4.1560, 622.4000, 103.3887, 5.4000,3.8780, ],
            'ACT': [2.0000, 3.9000, 1.0000, 11.0000, 3.9232, 3.9232, 4.4710, 6.0330, 622.4000, 103.3887, 5.8000,3.6500, ],
            'ATG': [8.7000, 7.7000, 1.0000, 18.0000, 7.7171, 7.7171, 2.1850, 2.1690, 621.4000, 103.2226, 6.7000,3.1400, ],
            'ATA': [9.7000, 6.2500, 0.0000, -13.0000, 6.2734, 6.2734, 3.0470, 1.6130, 621.4000, 103.2226, 2.8000,5.3810, ],
            'ATC': [3.6000, 4.4500, 1.0000, 7.0000, 4.4432, 4.4432, 4.1530, 5.0870, 621.4000, 103.2226, 5.3000,3.9350, ],
            'ATT': [0.0000, 0.3500, 0.0000, -30.0000, 0.3500, 0.3500, 6.6980, 7.2370, 621.4000, 103.2226, 0.7000,6.6240, ],
            'CGG': [3.0000, 3.8500, 3.0000, 2.0000, 3.8690, 3.8690, 4.5020, 5.4400, 622.4000, 103.3887, 4.7000,4.2790, ],
            'CGA': [5.8000, 7.0500, 2.0000, 31.0000, 7.0720, 7.0720, 2.5700, 3.8100, 622.4000, 103.3887, 8.3000,2.2450, ],
            'CGC': [4.3000, 5.9000, 3.0000, 25.0000, 5.8914, 5.8914, 3.2750, 4.6780, 622.4000, 103.3887, 7.5000,2.6910, ],
            'CGT': [5.2000, 5.3000, 2.0000, 8.0000, 5.3055, 5.3055, 3.6250, 4.1560, 622.4000, 103.3887, 5.4000,3.8780, ],
            'CAG': [9.6000, 6.9000, 2.0000, -2.0000, 6.8996, 6.8996, 2.6710, 1.6680, 621.4000, 103.2226, 4.2000,4.5670, ],
            'CAA': [6.2000, 4.7500, 1.0000, -9.0000, 4.7618, 4.7618, 3.9580, 3.5810, 621.4000, 103.2226, 3.3000,5.0890, ],
            'CAC': [6.8000, 6.6500, 2.0000, 17.0000, 6.6255, 6.6255, 2.8320, 3.2390, 621.4000, 103.2226, 6.5000,3.2530, ],
            'CAT': [8.7000, 7.7000, 1.0000, 18.0000, 7.7171, 7.7171, 2.1850, 2.1690, 621.4000, 103.2226, 6.7000,3.1400, ],
            'CCG': [3.0000, 3.8500, 3.0000, 2.0000, 3.8690, 3.8690, 4.5020, 5.4400, 622.4000, 103.3887, 4.7000,4.2790, ],
            'CCA': [0.7000, 3.0500, 2.0000, 8.0000, 3.0587, 3.0587, 5.0000, 6.8130, 622.4000, 103.3887, 5.4000,3.8780, ],
            'CCC': [5.7000, 5.8500, 3.0000, 13.0000, 5.8270, 5.8270, 3.3110, 3.8680, 622.4000, 103.3887, 6.0000,3.5360, ],
            'CCT': [4.7000, 5.0500, 2.0000, 8.0000, 5.0523, 5.0523, 3.7820, 4.4450, 622.4000, 103.3887, 5.4000,3.8780, ],
            'CTG': [9.6000, 6.9000, 2.0000, -2.0000, 6.8996, 6.8996, 2.6710, 1.6680, 621.4000, 103.2226, 4.2000,4.5670, ],
            'CTA': [7.8000, 5.0000, 1.0000, -18.0000, 5.0030, 5.0030, 3.8130, 2.6730, 621.4000, 103.2226, 2.2000,5.7340, ],
            'CTC': [6.6000, 6.0000, 2.0000, 8.0000, 5.9806, 5.9806, 3.2210, 3.3530, 621.4000, 103.2226, 5.4000,3.8780, ],
            'CTT': [4.2000, 4.7000, 1.0000, 6.0000, 4.6992, 4.6992, 3.9950, 4.7360, 621.4000, 103.2226, 5.2000,3.9920, ],
            'TGG': [0.7000, 3.0500, 2.0000, 8.0000, 3.0587, 3.0587, 5.0000, 6.8130, 622.4000, 103.3887, 5.4000,3.8780, ],
            'TGA': [10.0000, 7.7000, 1.0000, 8.0000, 7.7000, 7.7000, 10.0000, 1.4470, 622.4000, 103.3887, 5.4000,3.8780, ],
            'TGC': [7.5000, 6.7500, 2.0000, 13.0000, 6.7553, 6.7553, 2.7540, 2.8420, 622.4000, 103.3887, 6.0000,3.5360, ],
            'TGT': [5.8000, 5.5000, 1.0000, 6.0000, 5.4903, 5.4903, 3.5160, 3.8100, 622.4000, 103.3887, 5.2000,3.9920, ],
            'TAG': [7.8000, 5.0000, 1.0000, -18.0000, 5.0030, 5.0030, 3.8130, 2.6730, 621.4000, 103.2226, 2.2000,5.7340, ],
            'TAA': [7.3000, 4.6500, 0.0000, -20.0000, 4.6709, 4.6709, 4.0130, 2.9550, 621.4000, 103.2226, 2.0000,5.8520, ],
            'TAC': [6.4000, 5.0500, 1.0000, -6.0000, 5.0673, 5.0673, 3.7700, 3.4670, 621.4000, 103.2226, 3.7000,4.8570, ],
            'TAT': [9.7000, 6.2500, 0.0000, -13.0000, 6.2734, 6.2734, 3.0470, 1.6130, 621.4000, 103.2226, 2.8000,5.3810, ],
            'TCG': [5.8000, 7.0500, 2.0000, 31.0000, 7.0720, 7.0720, 2.5700, 3.8100, 622.4000, 103.3887, 8.3000,2.2450, ],
            'TCA': [10.0000, 7.7000, 1.0000, 8.0000, 7.7000, 7.7000, 2.1970, 1.4470, 622.4000, 103.3887, 5.4000,3.8780, ],
            'TCC': [6.2000, 5.0000, 2.0000, -5.0000, 4.9907, 4.9907, 3.8190, 3.5810, 622.4000, 103.3887, 3.8000,4.7990, ],
            'TCT': [6.5000, 4.9000, 1.0000, -9.0000, 4.8884, 4.8884, 3.8790, 3.4100, 622.4000, 103.3887, 3.3000,5.0890, ],
            'TTG': [6.2000, 4.7500, 1.0000, -9.0000, 4.7618, 4.7618, 3.9580, 3.5810, 621.4000, 103.2226, 3.3000,5.0890, ],
            'TTA': [7.3000, 4.6500, 0.0000, -20.0000, 4.6709, 4.6709, 4.0130, 2.9550, 621.4000, 103.2226, 2.0000,5.8520, ],
            'TTC': [5.1000, 4.0500, 1.0000, -12.0000, 4.0633, 4.0633, 4.3850, 4.2140, 621.4000, 103.2226, 3.0000,5.2640, ],
            'TTT': [0.1000, 0.0500, 0.0000, -36.0000, 0.0633, 0.0633, 0.1000, 7.1760, 621.4000, 103.2226, 0.0000,7.0450, ],
            'p'  : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # padding
        }
    else:
        if seqType == 'PROT' or seqType == 'RNA':
            print(CRED + 'Error: The \'Physicochemical Properties-D2\' feature is NOT applicable for PROT and RNA.' + CEND)
            return None
        else: None
    #end-if

    # print(X)

    X = utils.processTri(X, d, args)
    # print(X.shape)

    totalFeature = 0
    if seqType == 'DNA':
        totalFeature = 12
    else:
        if seqType == 'PROT' or seqType == 'RNA': None
        else:
            None
    # end-if

    save.datasetSave(X, totalFeature, 'pcpD2')
#end-def