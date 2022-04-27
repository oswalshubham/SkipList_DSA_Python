import time
import SkipList
from typing import List
import random


class DictPerformanceAnalyzer:
    def __init__(self) -> None:
        self.INPUT_SIZES = [10000, 50000, 100000, 200000]
        self.NUM_TRIALS = 1000
        self.INSERT_TIME_INDEX = 0
        self.DELETE_TIME_INDEX = 1
        self.FIND_TIME_INDEX = 2
        self.CLOSESTKEYAFTER_TIME_INDEX = 3
        self.keys = [0]*(self.INPUT_SIZES[len(self.INPUT_SIZES)-1] + self.NUM_TRIALS)
        self.cumTimes = [[0 for i in range(len(self.INPUT_SIZES))]for j in range(4)]
        pass
    


    def populate(self, dict : SkipList.OrderedDictionary, nextInputSize):
        currentSize = dict.size()
        while currentSize < nextInputSize:
            dict.insertElement(self.keys[currentSize], self.keys[currentSize])
            currentSize+=1


    def measurePerformance(self, dict : SkipList.OrderedDictionary):
        lst = []
        print("Input Sizes         :  10000   50000   100000   200000")
        for i in range(len(self.keys)):
            lst.append(2*i)

        random.shuffle(lst)

        for i in range(len(self.keys)):
            self.keys[i] = lst[i]

        for i in range(len(self.INPUT_SIZES)):
            #1
            size  = self.INPUT_SIZES[i]
            self.populate(dict, size)
            #2
            arr1 = []
            for j in range(size):
                arr1.append(self.keys[j])
            #3
            arr1.sort()
            #4
            sample_successful = self.keysForSuccessfulFind(arr1, self.NUM_TRIALS)
            sample_unsuccessfulfind = self.keysForUnsuccessfulFind(arr1, self.NUM_TRIALS)
            sample_closestkeyAfter = self.keysforClosestKeyAfter(arr1,self.NUM_TRIALS)
            sample_insert = []
            for j in range(size, size+self.NUM_TRIALS):
                sample_insert.append(self.keys[j])

            start_time = time.time()
            for ele in sample_successful:
                dict.findElement(ele)
            end_time = time.time()
            successfulFindtime = end_time - start_time 

            start = time.time()

            for keys in sample_unsuccessfulfind:
                dict.findElement(keys)

            end = time.time()

            unsuccessfulFindTime = end-start

            averageFindtime = (successfulFindtime + unsuccessfulFindTime)/(2*self.NUM_TRIALS)
            averageFindtime *= 1000
            self.cumTimes[self.FIND_TIME_INDEX][i] = averageFindtime

            
            start_time = time.time()

            for ele in sample_closestkeyAfter:
                dict.closestKeyAfter(ele)

            end_time = time.time()

            closestKeyAftertime = end_time - start_time 
            closestKeyAftertime = closestKeyAftertime*1000

            self.cumTimes[self.CLOSESTKEYAFTER_TIME_INDEX][i] = closestKeyAftertime/self.NUM_TRIALS

            insert_start = time.time()
            for ele in sample_insert:
                dict.insertElement(ele, ele)

            insert_end = time.time()

            insertTime = insert_end - insert_start
            insertTime = insertTime*1000
            self.cumTimes[self.INSERT_TIME_INDEX][i] =insertTime/self.NUM_TRIALS

            remove_start = time.time()
            for ele in sample_insert:
                dict.removeElement(ele)

            remove_end = time.time()

            deleteTime = remove_end - remove_start
            deleteTime = deleteTime*1000
            self.cumTimes[self.DELETE_TIME_INDEX][i] = deleteTime/self.NUM_TRIALS

        self.dumpPerformanceStats()

    def keysForSuccessfulFind(self,array, sampleSize)->List:
        result = []
        i=0
        while i<sampleSize:
            index = random.randint(0, len(array)-1)
            key = array[index]
            if key in result:
                continue
            else:
                result.append(key)
                i+=1

        return result

    def keysForUnsuccessfulFind(self, array, sampleSize)->List:
        result = [] 
        i=0
        while i<sampleSize:
            index = random.randint(0, len(array)-1)
            key = array[index]-1
            if key in result:
                continue
            else:
                result.append(key)
                i+=1

        return result

    def keysforClosestKeyAfter(self, array, sampleSize):
        result = [] 
        i=0
        while i<sampleSize:
            index = random.randint(0, len(array)-1)
            key = array[index]-1
            if key in result:
                continue
            else:
                result.append(key)
                i+=1

        return result

    def dumpPerformanceStats(self):
        #rounding to 3 decimal 
        for i in range(4):
            for j in range(len(self.INPUT_SIZES)):
                self.cumTimes[i][j] = round(self.cumTimes[i][j], 3)

        for i in range(4):
            if i == 0:
                print("Average Insert Time  : ", end = " ")
            elif i == 1:
                print("Average Delete Time  : ", end = " ")
            elif i == 2:
                print("Average Find Time    : ", end = " ")
            else:
                print("ClosestKeyAfter Time : ", end = " ")

            print(self.cumTimes[i])


dict = SkipList.SkipList()
pa = DictPerformanceAnalyzer()
pa.measurePerformance(dict)




