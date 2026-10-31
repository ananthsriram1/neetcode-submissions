"""
so you have a data structure, and in this data structure, you have a key value store. the trick is the timestamp. 

when you do the set stuff, thats whats in the actual data structure

the get is the main difficult part. 

you can guarantee all the timestamps of set are increasing


"""
from collections import defaultdict
import copy
class TimeMap:

    def __init__(self):
        #timestamps , min and max
        self.min_timestamp = float('inf')
        self.max_timestamp = float('-inf')

        #main data structure, nested dict
        self.mapping = defaultdict(lambda: defaultdict(str))

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr_copy = None
        if timestamp > self.max_timestamp and self.max_timestamp >= 0:
            curr_copy = copy.deepcopy(self.mapping[self.max_timestamp])

        self.max_timestamp = max(timestamp, self.max_timestamp)
        self.min_timestamp = min(timestamp, self.min_timestamp)

        if curr_copy:
            self.mapping[timestamp] = curr_copy

        self.mapping[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.mapping:
            return self.mapping[timestamp][key]
        elif timestamp > self.max_timestamp:
            return self.mapping[self.max_timestamp][key]

        seen = -1
        for time in self.mapping:
            if time < timestamp:
                seen = max(time, seen)
            else:
                return self.mapping[seen][key]

        return ""
