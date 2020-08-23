# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1: Visualizing Company's records wrt loan approvals
#Creating a new variable to store the value counts
loan_status = data['Loan_Status'].value_counts()

#Plotting bar plot
loan_status.plot(kind ='barh')

# Step 2: Loan approval distribution across the regions
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
property_and_loan.plot(kind = 'bar', stacked =False, figsize =(20,10))
#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation =45)

# Step 3: To find out whether higher education results in a better guarantee in issuing loans
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()
education_and_loan.plot(kind = 'bar', stacked = True, figsize = (20,10))

#Changing the x-axis label
plt.xlabel('Education')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation = 45)

# Step 4: To check whether being graduate or not leads to different loan amount distribution
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education'] == 'Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education'] == 'Not Graduate']

#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind = 'density', label = 'Graduate')

#Plotting density plot for 'Graduate'
not_graduate['LoanAmount'].plot(kind = 'density', label = 'Not Graduate')

#For automatic legend display
plt.legend()

# Step 5: To find a correlation between the borrower's income and loan amount he is lent
#Setting up the subplots
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize = (20,20))

#Plotting scatter plot
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

#Setting the subplot axis title
ax_1.set(title='Applicant Income')

#Plotting scatter plot
ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])

#Setting the subplot axis title
ax_2.set(title = 'Coapplicant Income')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot
ax_3.scatter(data['TotalIncome'], data['LoanAmount'])

#Setting the subplot axis title
ax_3.set(title = 'Total Income')


