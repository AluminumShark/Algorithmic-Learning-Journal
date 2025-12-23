# Time: O(log n) for get(), O(1) for set() (amortized)
# Space: O(n)
class TimeMap:
    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        arr = self.mp[key]
        L, R = 0, len(arr) - 1
        ans = ""
        while L <= R:
            mid = (L + R) // 2
            ts, val = arr[mid]
            if ts <= timestamp:
                ans = val
                L = mid + 1
            else:
                R = mid - 1
        return ans

