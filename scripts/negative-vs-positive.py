import random
import numpy
import matplotlib
import matplotlib.pyplot as plt
import pylab

#------------------------------------------------------------------------------
# Simulation settings
# ===================

# probability for a student to be present
attendance_probability = 0.99

# number of samples for the simulation
num_samples = 1000
#------------------------------------------------------------------------------

# embedding fonts in the generated pdf graphs
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True

# marks for the seminar presentation
def getSeminarPresMark():
    mark = random.randint(0,25)
    return mark

# marks for the book chapter presentation
def getBookChapterPresMark():
    mark = random.randint(0,25)
    return mark

# marks for the single page review
def getSinglePageReviewMark():
    mark = random.randint(0,30)
    return mark

# marks for the active participation
def getActiveParticipationMark():
    mark = random.randint(0,10)
    return mark

# marks for the highlighting and questioning
def getHighlightQuestionMark():
    mark = random.randint(0,10)
    return mark

# panelty marks for being absent
def getAbsentPaneltyMark():
    total_panalty = 0
    x = 0
    while x < 60:
        panelty = numpy.random.choice([0,1], p=[attendance_probability, 1-attendance_probability])
        total_panalty = total_panalty + panelty
        x+=1

    #print("Total panalty: %d", total_panalty)
    return total_panalty



#-------------------------------------------------------------------------------------------
# Now, just to test our possibilities for marks, let's roll the dice for "num_samples" times.
mark_list = list()
result = 0
x = 0
while x < num_samples:
    result = getSeminarPresMark() + getBookChapterPresMark() + getSinglePageReviewMark() + getActiveParticipationMark() + getHighlightQuestionMark() - getAbsentPaneltyMark()

    # we don't give negative final marks
    if result < 0:
        result = 0
        #print(0)

    mark_list.append(result)
    #print(result)
    x+=1


# Now, just to test our possibilities for marks, let's roll the dice for "num_samples" times.
mark_list2 = list()
result = 0
x = 0
while x < num_samples:
    result = getSeminarPresMark() + getBookChapterPresMark() + getSinglePageReviewMark() + getActiveParticipationMark() + getHighlightQuestionMark() - getAbsentPaneltyMark()

    # we don't give negative final marks
    if result < 0:
        result = 0
        #print(0)

    mark_list2.append(result)
    #print(result)
    x+=1


#------------------------------------------------------------------------------
# plotting data

# convert it into a numpy array
mark_list = numpy.array(mark_list)

# plot the histogram distribution of marks

pylab.figure(num=None, figsize=(10, 6))
y, bin_edges = pylab.histogram(mark_list, bins=10)
bin_centers = 0.5*(bin_edges[1:]+bin_edges[:-1])
pylab.plot(bin_centers, y, '-')
#pylab.title('Histogram of marks with negative panalties')
#pylab.xlabel('marks')
#pylab.ylabel('number of students')
#pylab.grid(True)
#pylab.show()
#pylab.savefig('graph.pdf')


# convert it into a numpy array
mark_listi2 = numpy.array(mark_list2)

# plot the histogram distribution of marks

#pylab.figure(num=None, figsize=(10, 6))
y, bin_edges = pylab.histogram(mark_list2, bins=10)
bin_centers = 0.5*(bin_edges[1:]+bin_edges[:-1])
pylab.plot(bin_centers, y, '-')
pylab.title('Histogram of marks with negative panalties')
pylab.xlabel('marks')
pylab.ylabel('number of students')
pylab.grid(True)
#pylab.show()
pylab.savefig('negative-vs-positive.pdf')




'''
x_values = numpy.linspace(0, num_samples)
y_values = numpy.linspace(0, num_samples)

pylab.figure(num=None, figsize=(10, 6))
#pylab.subplot(211)
pylab.title('Impact of the negative marks')
pylab.xlabel('mark')
pylab.ylabel('number of students')
pylab.plot(x_values, y_values)
#pylab.xlim(0, max(time_sec)
#pylab.savefig('graph.pdf')
pylab.show()
'''



