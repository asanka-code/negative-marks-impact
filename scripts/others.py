import random
import numpy
import settings

# marks for the seminar presentation
def getSeminarPresMarkRandom():
    mark = random.randint(0,20)
    return mark

# marks for the book chapter presentation
def getBookChapterPresMarkRandom():
    mark = random.randint(0,20)
    return mark

# marks for the single page review
def getSinglePageReviewMarkRandom():
    mark = random.randint(0,20)
    return mark

# marks for the active participation
def getActiveParticipationMarkRandom():
    mark = random.randint(0,10)
    return mark

# marks for the highlighting and questioning
def getHighlightQuestionMarkRandom():
    mark = random.randint(0,10)
    return mark

# mark for being present
def getPresentMarkRandom():
    totalAttendance = 0.0
    x = 0
    while x < 60:
        attendence = numpy.random.choice([1,0], p=[settings.attendance_probability, 1-settings.attendance_probability])
        totalAttendance+=attendence
        x+=1

    # scale attendance from (0-60) to (0-20) scale
    totalAttendance = (totalAttendance/60)*20
    #print("Total attendance: %d", totalAttendance)
    return totalAttendance

# mark for being present
def getPresentMark(presentCount):
    totalAttendance = 0.0
    # scale attendance from (0-60) to (0-20) scale
    totalAttendance = (presentCount/60.0)*20.0
    #print("Total attendance: %d", totalAttendance)
    return round(totalAttendance)



# final mark calculation
def getFinalMarkRandom():
    # Now, just to test our possibilities for marks, let's roll the dice for "num_samples" times.
    mark_list = list()
    result = 0
    x = 0
    while x < settings.num_samples:
        result = getSeminarPresMarkRandom() + getBookChapterPresMarkRandom() + getSinglePageReviewMarkRandom() + getActiveParticipationMarkRandom() + getHighlightQuestionMarkRandom() + getPresentMarkRandom()

        # we don't give negative final marks
        if result < 0:
            result = 0
            #print(0)

        mark_list.append(result)
        #print(result)
        x+=1

    # convert it into a numpy array
    mark_list = numpy.array(mark_list)
    return mark_list

# final mark calculation
def getFinalMark(seminarPresMark, bookChapterPresMark, singlePageReviewMark, activeParticipationMark, highlightQuestionMark, presentCount):
    mark_list = list()
    result = seminarPresMark + bookChapterPresMark + singlePageReviewMark + activeParticipationMark + highlightQuestionMark + getPresentMark(presentCount)
    # we don't give negative final marks
    if result < 0:
        result = 0
    mark_list.append(result)

    # convert it into a numpy array
    mark_list = numpy.array(mark_list)
    return mark_list



