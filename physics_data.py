import matplotlib.pyplot as plt
import numpy as np
'''
Do you have prior programming experience? - 17 students indicated yes, 4 no
Have you learned Python before? 7 yes, 14 no
Were you able to follow along with the Python demonstration? - 20 yes, 1 no
Do you believe the demonstration expanded your understanding of the material presented? - 21 yes, 0 no

Would you benefit from greater integration of Python into this course? 18 yes, 3 no

'''
data = {'Yes':17,'No':4}
x = list(data.keys())

y = list(data.values())
fig = plt.figure(figsize = (10,10))
plt.bar(x, y, width=.2)
plt.xlabel('Do students have prior programming experience?')
plt.ylabel('Number of Students')
plt.title('Number of students with or without prior programming experience')
plt.savefig('physicspriorxp')

#plt.show()


