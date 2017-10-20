import pandas as pd
import numpy as np


B=pd.read_csv('Behrens.csv', sep='\t', lineterminator='\r')
cols=list(B)
#print(cols)

B = B.rename(columns={'Left seed\rTotal track no.': 'Mask_L_tot', 'Right seed\rTotal track no.': 'Mask_R_tot'})

L_col = [col for col in B if col.startswith('L')]
R_col = [col for col in B if col.startswith('R')]
#print(cols)
#print(L_col)

B['Num_L_tot'] = B[L_col].sum(axis=1)
B['Num_R_tot'] = B[R_col].sum(axis=1)

for lcol in L_col:
    B['perc_'+lcol] = B[lcol]/B['Mask_L_tot']

L_perc = [col for col in B if col.startswith('perc_L')]
Left_B = B.loc[:, B.columns.isin(list(L_perc))]
subject = B[['Subject']]
Left_B = subject.join(Left_B)

Order_LeftB = Left_B.set_index('Subject')
np.argsort(-Order_LeftB.values, axis=1)
Order_LeftB.columns[np.argsort(-Order_LeftB.values, axis=1)]
Results_Order_LeftB=pd.DataFrame(Order_LeftB.columns[np.argsort(-Order_LeftB.values, axis=1)], index=Order_LeftB.index)
Results_Order_LeftB.to_csv('Results_Order_LeftB.csv')










#B=pd.read_csv('Behrens.csv', sep='\t', lineterminator='\r')
#cols=list(B)
#print(cols)
#B = B.rename(columns={'Left seed\rTotal track no.': 'L_tot', 'Right seed\rTotal track no.': 'R_tot'})
#B = B.rename(columns={'L_tot': 'JHS_L_tot', 'R_tot': 'JHS_R_tot'})
#L_col = [col for col in B if col.startswith('L')]
#R_col = [col for col in B if col.startswith('R')]
#print(cols)
#print(L_col)
#print(R_col)
#B = B.rename(columns={'YBK_L_tot': 'Num_L_tot', 'YBK_R_tot': 'Num_R_tot'})
#
#
#for lcol in L_col:
#    B['perc_'+lcol] = B[lcol]/B['Mask_L_tot']
#
#L_perc = [col for col in B if col.startswith('perc_L')]
#Left_B = B.loc[:, B.columns.isin(list(L_perc))]
#subject = B[['Subject']]
#Left_B = subject.join(Left_B)
#
#Ordering_LeftB = Left_B.set_index('Subject')
#np.argsort(-Ordering_LeftB.values, axis=1)
#Ordering_LeftB.columns[np.argsort(-Ordering_LeftB.values, axis=1)]
#results_Ordering_LeftB=pd.DataFrame(Ordering_LeftB.columns[np.argsort(-Ordering_LeftB.values, axis=1)], index=Ordering_LeftB.index)

