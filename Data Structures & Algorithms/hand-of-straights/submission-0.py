class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # two usecases - learn
        # group into size of 3 with straight property
        # [1,2,3,4,5] n = 3 -> OUTPUT = FALSE
        #  [1,1,2,3,3,3] n = 3 -> OUTPUT = FALSE
        # For second one there is no two left

        # we don't have to make group in this question
        # - we will act based on frequency

        if len(hand) % groupSize != 0:
            return False # if we cannot divide into groups

        freqMap = Counter(hand)

        for num in hand:
            start = num
            while freqMap[start-1]: # isse chota exist krta hai
                start = start - 1 # try to reach to start of group
            # reached at the start of group


            while start <= num:
                while freqMap[start]:
                    for i in range (start, start+groupSize): # next member is +1
                        if not freqMap[i]:
                            return False
                        freqMap[i] = freqMap[i] - 1
                start = start + 1
        return True         