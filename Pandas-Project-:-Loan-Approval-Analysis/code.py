# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank = pd.read_csv(path)
#print(bank.head())

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here
banks = bank.drop(['Loan_ID'],axis=1)
#print(banks)

#print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
#print(bank_mode)
banks = banks.fillna(value=bank_mode)
#print(banks)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here





avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here




check = banks[(banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')]
loan_approved_se = len(check)
check1 = banks[(banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')]
loan_approved_nse = len(check1)
Loan_Status = 614
percentage_se = (loan_approved_se / Loan_Status) * 100
print(percentage_se)
percentage_nse = (loan_approved_nse / Loan_Status) * 100
print(percentage_nse)

# code ends here


# --------------
# code starts here

def month_to_year(x):
    return (x/12)

loan_term=banks["Loan_Amount_Term"].apply(month_to_year)

#print(loan_term)


big_loan_term = len(loan_term[loan_term >= 25])
print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()

# code ends here


