class Solution:
    def powerfulInteger(self, intervals, k):
        # code here
        events = []
        
        for start, end in intervals:
            events.append((start, 1))     # interval starts
            events.append((end + 1, -1))  # interval ends

        events.sort()
        count = 0
        max_powerful = -1
        
        for i in range(len(events)):
            pos, delta = events[i]
            count += delta
            
            # If the current count is >= k, the current position is in a powerful range
            if count >= k:
                # look ahead to the next position (or stay if it's last event)
                next_pos = events[i+1][0] if i + 1 < len(events) else pos
                max_powerful = max(max_powerful, next_pos - 1)

        return max_powerful
        
