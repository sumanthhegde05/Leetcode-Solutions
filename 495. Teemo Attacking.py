class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        value = 0
        if len(timeSeries) == 0:
            return value
        value = duration
        if len(timeSeries) == 1:
            return value
        for i in range(1,len(timeSeries)):
            if timeSeries[i]-timeSeries[i-1] < duration:
                value += timeSeries[i]-timeSeries[i-1]
            else:
                value += duration
        return value