class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        配列内の区間が重複していないか判定する。
        sortで開始時間が降順になる。
        [i]の終了時刻と[i+1]の開始時刻の大小関係を全て判定して実現。
        from LEETCODE (252. Meeting Rooms)
        https://leetcode.com/problems/meeting-rooms/
        """
        # Time: O(nlogn)
        # Space: O(1)
        
        # sortはlistの第一要素を比較する
        intervals.sort()
        
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
