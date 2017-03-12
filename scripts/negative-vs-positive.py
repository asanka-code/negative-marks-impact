import random
import numpy
import matplotlib
import matplotlib.pyplot as plt
import pylab
import manju
import others
import settings

# embedding fonts in the generated pdf graphs
matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['text.usetex'] = True


#------------------------------------------------------------------------------
# Case 1: For students who get full marks on every other component, what is the
# variation of marks for diffeent number of absent days to sessions?

mark_list1 = list()
mark_list2 = list()
session = 60
while session > 2:
    mark1 = manju.getFinalMark(25,25,30,10,10,session)
    mark_list1.append(numpy.int(mark1))

    mark2 = others.getFinalMark(20,20,20,10,10,session)
    mark_list2.append(numpy.int(mark2))

    session-=1

mark_list1 = numpy.array(mark_list1)
mark_list2 = numpy.array(mark_list2)
x_values = numpy.arange(60, 2, -1)

print("mark_list1=%d", mark_list1)
print("mark_list2=%d", mark_list2)
print "x_values = ", x_values

pylab.figure(num=None, figsize=(10, 6))
#pylab.subplot(211)
pylab.title('Impact of the negative marks')
pylab.xlabel('number of present days')
pylab.ylabel('total mark')
pylab.grid(True)
line_manju = pylab.plot(x_values, mark_list1, label='with negative panalties')
line_others = pylab.plot(x_values, mark_list2, label='no negative panalties')
pylab.legend(loc='lower right')

#pylab.xlim(0, max(time_sec)
pylab.savefig('number-of-present-days-vs-total-mark.pdf')
#pylab.show()
#------------------------------------------------------------------------------





'''
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



