# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
print("STEP 1: To check which variable is categorical and which one is numerical to get a basic idea about the features of the dataset")
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.shape)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.shape)
print("="*50)

print("STEP 2: To check which columns have missing values and also check the coount of missing values each column has")
banks = bank.drop('Loan_ID', axis = 1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
print(bank_mode)

banks.fillna(bank_mode, inplace =True)
print("="*50)
print("STEP 3: Check loan amount of an avg person based on Gender, marriage status and employment status")
avg_loan_amount = pd.pivot_table(banks, index = ['Gender', 'Married', 'Self_Employed'],values = ['LoanAmount'],aggfunc = 'mean')
print(avg_loan_amount)

print("="*50)
print("STEP 4: Check percentage of loan approved based on a person's employment type")
loan_approved_se = banks[ (banks['Self_Employed'] == "Yes") & (banks['Loan_Status'] == "Y") ]
loan_approved_nse = banks[ (banks['Self_Employed'] == "No") & (banks['Loan_Status'] == "Y") ]

#Calculating percentage: Loan_status count is 614
percentage_se = (len(loan_approved_se) /614) *100
percentage_nse = (len(loan_approved_nse) /614) *100
print("{} percentage of people are self employed and their loans have been approved".format(percentage_se))
print("{} percentage of people are not self employed and their loans have been approved".format(percentage_nse))

print("="*50)
print("STEP 5: To find applicants with long loan amount term")
loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)

print("="*50)
print("STEP 6: To check avg income of an applicant and the average loan given to a person based on their income")
loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)
print(mean_values.iloc[1,0])



