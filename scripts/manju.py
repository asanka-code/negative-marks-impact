import random
import numpy
import settings

# marks for the seminar presentation
def getSeminarPresMarkRandom():
    mark = random.randint(0,25)
    return mark

# marks for the book chapter presentation
def getBookChapterPresMarkRandom():
    mark = random.randint(0,25)
    return mark

# marks for the single page review
def getSinglePageReviewMarkRandom():
    mark = random.randint(0,30)
    return mark

# marks for the active participation
def getActiveParticipationMarkRandom():
    mark = random.randint(0,10)
    return mark

# marks for the highlighting and questioning
def getHighlightQuestionMarkRandom():
    mark = random.randint(0,10)
    return mark

# panelty marks for being absent
def getAbsentPaneltyMarkRandom():
    total_panalty = 0
    x = 0
    while x < 60:
        panelty = numpy.random.choice([0,1], p=[settings.attendance_probability, 1-settings.attendance_probability])
        total_panalty = total_panalty + panelty
        x+=1

    #print("Total panalty: %d", total_panalty)
    return total_panalty

# panelty marks for being absent
def getAbsentPaneltyMark(presentCount):
    total_panalty = presentCount - 60
    total_panalty*=-1
    #print("Total panalty: %d", total_panalty)
    return total_panalty

# final mark calculation
def getFinalMarkRandom():
    # Now, just to test our possibilities for marks, let's roll the dice for "num_samples" times.
    mark_list = list()
    result = 0
    x = 0
    while x < settings.num_samples:
        result = getSeminarPresMarkRandom() + getBookChapterPresMarkRandom() + getSinglePageReviewMarkRandom() + getActiveParticipationMarkRandom() + getHighlightQuestionMarkRandom() - getAbsentPaneltyMarkRandom()

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
    result = seminarPresMark + bookChapterPresMark + singlePageReviewMark + activeParticipationMark + highlightQuestionMark - getAbsentPaneltyMark(presentCount)
    # we don't give negative final marks
    if result < 0:
        result = 0
    mark_list.append(result)

    # convert it into a numpy array
    mark_list = numpy.array(mark_list)
    return mark_list



