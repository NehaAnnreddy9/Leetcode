from collections import defaultdict
class Twitter:

    def __init__(self):
        self.user_following = defaultdict(list)
        self.news_feed = []
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.news_feed.append([userId, tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        nf = self.news_feed[::-1]
        cnt = 10
        res = []
        for nfi in nf:
            if userId == nfi[0] or nfi[0] in self.user_following[userId]:
                res.append(nfi[1])
                cnt -= 1
                if cnt == 0: break
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].append(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.user_following[followerId]:
            self.user_following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)