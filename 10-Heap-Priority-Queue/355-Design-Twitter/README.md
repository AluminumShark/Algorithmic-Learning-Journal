# 355. Design Twitter

## Problem Description

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets in the user's news feed.

Implement the `Twitter` class:

- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.
- `List<Integer> getNewsFeed(int userId)` Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- `void follow(int followerId, int followeeId)` The user with ID `followerId` started following the user with ID `followeeId`.
- `void unfollow(int followerId, int followeeId)` The user with ID `followerId` started unfollowing the user with ID `followeeId`.

**Example:**
```
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return [5].
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return [6, 5].
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return [5].
```

## Solution

### Approach: Merge K Sorted Lists with Heap

**Key Insight:** Getting the news feed is essentially **merging K sorted lists** (where K = number of followees + 1 for self).

Each user's tweet timeline is a sorted list (sorted by time). To get the 10 most recent tweets from all followees, we need to merge these sorted lists efficiently.

### Data Structures

1. **`tweets`**: `defaultdict(list)` - stores tweets as `(timestamp, tweetId)` for each user
2. **`followees`**: `defaultdict(set)` - stores the set of users that each user follows
3. **`time`**: global timestamp counter (increments with each tweet)
4. **Min-Heap**: for merging K sorted lists

### Algorithm for `getNewsFeed`

1. **Collect sources**: Get all followees + self
2. **Initialize heap**: Add the most recent tweet from each source
   - Heap entry: `(-timestamp, tweetId, userId, index)`
   - Use negative timestamp for max-heap behavior (most recent first)
3. **Extract top 10**: While heap is not empty and we have < 10 tweets:
   - Pop the most recent tweet
   - Add it to the result
   - If that user has more tweets, push their next most recent tweet to the heap
4. Return the result

**Why this works:**
- Each user's tweets are already sorted by time (chronological order)
- We only need to compare the "heads" of these sorted lists
- Heap gives us the maximum (most recent) among all current candidates
- We process exactly the tweets we need (at most 10 per user)

### Visual Example

```
User 1 tweets: [(10, a), (7, b), (3, c)]  ← sorted by time
User 2 tweets: [(9, d), (5, e)]
User 3 tweets: [(8, f), (6, g), (4, h)]

Heap operations:
Initial: [(-10, a, 1, 0), (-9, d, 2, 0), (-8, f, 3, 0)]
Pop (-10, a) → result = [a], push (-7, b, 1, 1)
Pop (-9, d)  → result = [a, d], push (-5, e, 2, 1)
Pop (-8, f)  → result = [a, d, f], push (-6, g, 3, 1)
Pop (-7, b)  → result = [a, d, f, b], push (-3, c, 1, 2)
...continue until we have 10 tweets

Result: [a, d, f, b, g, e, h, c] (most recent to least recent)
```

### Complexity Analysis

**Time Complexity:**

- `postTweet`: O(1) - append to list
- `follow`: O(1) - add to set
- `unfollow`: O(1) - remove from set
- `getNewsFeed`: O(F + 10 log F) where F = number of followees
  - O(F) to initialize heap with one tweet from each followee
  - O(10 log F) to extract 10 tweets (each heap operation is O(log F))
  - In practice: O(F log F) worst case if we need to process many tweets

**Space Complexity:**

- O(U + T) where U = number of users, T = total number of tweets
- `tweets`: O(T) - stores all tweets
- `followees`: O(U²) worst case if everyone follows everyone
- Heap during `getNewsFeed`: O(F) - at most one tweet per followee in heap

### Edge Cases Handled

1. **Self-following**: User's own tweets are always in their news feed (added to sources)
2. **Prevent self-follow**: Check `followerId == followeeId` in follow method
3. **Unfollow non-existent**: Check if followee exists before removing
4. **Empty feeds**: Handle users with no tweets
5. **Less than 10 tweets**: Return all available tweets

## Key Concepts

### 1. Merge K Sorted Lists Pattern

This problem is a classic application of the **Merge K Sorted Lists** pattern:
- **Input**: K sorted lists (each user's tweet timeline)
- **Goal**: Find the top 10 elements across all lists
- **Tool**: Min-heap (or max-heap with negative values)
- **Optimization**: We don't need to merge completely, just extract 10 elements

### 2. Lazy Evaluation

Instead of pre-computing and storing merged feeds, we compute them on-demand:
- **Pros**: No stale data, saves space, efficient for infrequent queries
- **Cons**: Slower query if user follows many people

**Real Twitter**: Uses a combination of both approaches (pre-computed + real-time merge)

### 3. Timestamp as Global Order

Using a global timestamp ensures total ordering of tweets:
- Avoids issues with concurrent tweets at the same millisecond
- Simplifies the merging logic (no tie-breaking needed)

### 4. Heap with Indices

The heap stores `(time, tweetId, userId, index)` to track:
- Which tweet we're currently at for each user
- How to fetch the next tweet from that user's timeline

This is the standard iterator-based approach for merging sorted sequences.

## Alternative Approaches

### 1. Pre-compute Feeds (Push Model)

**Idea**: Maintain a pre-computed feed for each user
- When someone posts, update all followers' feeds
- `getNewsFeed` becomes O(1), but `postTweet` becomes O(F)

**Trade-off**: Good for read-heavy workloads, bad for users with many followers

### 2. Simple Merge with Sorting

**Idea**: Collect all tweets from followees and sort
```python
def getNewsFeed(self, userId):
    tweets = []
    for uid in self.followees[userId] | {userId}:
        tweets.extend(self.tweets[uid])
    tweets.sort(reverse=True)
    return [tid for _, tid in tweets[:10]]
```

**Time**: O(T log T) where T = total tweets from all followees
**Worse than heap**: Heap is O(T + 10 log F), which is better when T >> 10

## System Design Considerations

In a real Twitter-like system:

1. **Caching**: Cache recent feeds
2. **Pagination**: Support infinite scroll beyond 10 tweets
3. **Fanout on write**: For popular users (celebrities), use push model
4. **Fanout on read**: For normal users, use pull model (like our solution)
5. **Hybrid approach**: Combine push and pull based on follower count
6. **Database**: Use time-series databases or ordered key-value stores

## Related Problems

- [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)
- [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)
