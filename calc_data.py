import matplotlib.pyplot as plt
import numpy as np
'''
Do you have prior programming experience? 14 yes, 10 no
Have you learned Python before? 5 yes, 19 no
Were you able to follow along with the Python demonstration? 19 yes, 5 no
Do you believe the demonstration expanded your understanding of the material presented? 17 yes, 7 no

Would you benefit from greater integration of Python into this course? 16 yes, 8 no


'''
data = {'Yes':19,'No':5}
x = list(data.keys())

y = list(data.values())
fig = plt.figure(figsize = (10,10))
plt.bar(x, y, width=.2)
plt.xlabel('Do students believe the demonstration expanded their understanding of the material presented?')
plt.ylabel('Number of Students')
plt.title('Number of Students In/Not In Agreement with Survey Question')
plt.savefig('calc_expanded_knowledge.png')

#plt.show()


