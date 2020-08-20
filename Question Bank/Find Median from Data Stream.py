class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.l.append(num)
        self.l.sort()

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.l)%2!=0:
            return self.l[len(self.l)//2]
        else:
            return (self.l[len(self.l)//2]+self.l[len(self.l)//2-1])/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()