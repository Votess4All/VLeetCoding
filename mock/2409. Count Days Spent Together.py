from itertools import accumulate

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.prefixsum = list(accumulate(days, initial=0))

        alice = [self.convertDays(arriveAlice), self.convertDays(leaveAlice)]
        bob = [self.convertDays(arriveBob), self.convertDays(leaveBob)]
        
        left = max(alice[0], bob[0])
        right = min(alice[1], bob[1])
        
        return max(right-left+1, 0)
    
    def convertDays(self, date):
        month, day = date.split("-")
        
        month = int(month[1]) if month[0] == "0" else int(month)
        day = int(day[1]) if day[0] == "0" else int(day)
        total_days = self.prefixsum[month-1] + day
        return total_days

if __name__ == "__main__":
    arriveAlice = "09-01"
    leaveAlice = "10-19"
    arriveBob = "06-19"
    leaveBob = "10-20"
    
    print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))