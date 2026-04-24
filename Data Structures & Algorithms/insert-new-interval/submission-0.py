class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            print("i",i)
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                print("1",newInterval[1],intervals[i][0])
                return res+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                print("2",newInterval[0],intervals[i][1])
                res.append(intervals[i])
            else:
                newInterval=[
                    min(newInterval[0],intervals[i][0]),
                    max(newInterval[1],intervals[i][1]),
                ]
                print(newInterval)
        res.append(newInterval)
        return res