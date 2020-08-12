# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
print("STEP 1: LOAD DATA TO NUMPY ARRAY AND ADDING A NEW RECORD TO IT")
census = np.concatenate((data,new_record), axis = 0)
print(" The shape of concatenated data is {}".format(np.shape(census)))
print("STEP 2: ANALYSIS OF AGE DISTRIBUTION")
age = census[:,0]
print(" The array of ages: {}".format(age))
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)
print(" Maximum age is {} \n Minimum Age is {} \n The mean of ages is {} \n The standard deviation of ages is{}".format(max_age, min_age, age_mean, age_std))

print("STEP 3:CHECKING COUNTRY'S RACE DISTRIBUTION")
#RACE COLUMN ARRAYS
race = census[:,2]
race_0 = race[race==0]
race_1 = race[race==1]
race_2 = race[race==2]
race_3 = race[race==3]
race_4 = race[race==4]

#LENGTH OF RACE ARRAYS
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
#MINORITY RACE
mini = (len_0, len_1, len_2, len_3, len_4)
minority_race = mini.index(min(mini))
print(" The minority race is {}".format(minority_race))

print("STEP 4: CHECKING THE GOVT. POLICY - CITIZENS ABOVE 60 SHOULD NOT WORK MORE THAN 25 HRS PER WEEK")
senior_citizens = census[census[:,0] > 60]
working_hours_sum = senior_citizens.sum(axis=0)[6]
print(" The sum of working hours is {}".format(working_hours_sum))
senior_citizens_len = len(senior_citizens)
print(" The number of senior citizens are {}".format(senior_citizens_len))
avg_working_hours = working_hours_sum / senior_citizens_len
print(" The average working hours of citizens above age of 60 is {}".format(avg_working_hours))
if avg_working_hours <= 25:
    print(" THE GOVT. POLICY IS BEING FOLLOWED")
else:
    print(" THE GOVT. POLICY IS NOT BEING FOLLOWED")

print("STEP 5: CHECKING WHETHER HIGHLY EDUCATED PEOPLE HAVE BETTER PAY IN GENERAL")
high = census[census[:,1] > 10]
low = census[census[:,1] <= 10]
sum_high = high.sum(axis=0)[7]
len_high = len(high)
avg_pay_high = sum_high / len_high
sum_low = low.sum(axis=0)[7]
len_low = len(low)
avg_pay_low = sum_low / len_low
print(" The average pay of highly educated citizens is {} \n The pay of less educated people is {}".format(avg_pay_high, avg_pay_low ))
if avg_pay_high > avg_pay_low:
    print(" HIGHER EDUCATED HAVE BETTER PAY IN GENERAL")
else:
    print(" THE LESS EDUCATED HAVE BETTER PAY TOO")


