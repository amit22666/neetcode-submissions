// # but 2nd appoach
// # n ka n+1 ke saath or karenege toh result milega
// # wo result wo smallest number milega. jiska n ke saath and krne pr n milta hai
// # yeh kaam x times repeat krna hai


class Solution {
    public long minEnd(int n, int x) {
        long ans = x;
        n -= 1;
        while (n -- > 0) {
            ans =(ans + 1)  | x;
        }
        return ans;
    }
}