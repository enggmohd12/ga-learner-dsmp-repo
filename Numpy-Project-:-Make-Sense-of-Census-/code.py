# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record= np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Code starts here
data_file = path
data = np.genfromtxt(data_file, delimiter=",", skip_header=1)
print(data)
print("="*20)
census = np.concatenate((data,new_record))
print(census)


# --------------
#Code starts here
age = census[:,:1]
print(age)

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print(age_mean)

age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
#race = census[:,2]
#zero = race[race == 0]
#race_0 = np.array(zero,dtype=int)


race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]


len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

list_min = [len_0, len_1, len_2, len_3, len_4]
minimum_race = min(list_min)
if len_0 == minimum_race:
    minority_race = 0
elif len_1 == minimum_race:
    minority_race = 1
elif len_2 == minimum_race:
    minority_race = 2
elif len_3 == minimum_race:
    minority_race = 3
else:
    minority_race = 4

print("The minority class is ",minority_race)


# --------------
#Code starts here
age_check = census[:,0] > 60
senior_citizens = census[age_check]
working_hours = senior_citizens[:,6]
working_hours_sum = np.sum(working_hours)
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum / senior_citizens_len
print("The average working hours of senior citizen is ",avg_working_hours)


# --------------
#Code starts here
education_high = census[:,1] > 10
education_low = census[:,1] <= 10
high = census[education_high]
low = census[education_low]
pay_high = high[:,7]
low_high = low[:,7] 
avg_pay_low = np.mean(low_high)
print(avg_pay_low)
avg_pay_high = np.mean(pay_high)
print(avg_pay_high)


