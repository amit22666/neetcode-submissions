class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # trick
                p1 , p2 = i+j, i+j+1

                # add karo existing value ke saath
                sum_ = mul + result[p2]

                result[p2] = sum_ % 10 # current digit
                result[p1] += sum_ // 10 # carry digit add karo
        # leading zeros hatoo
        print(result)
        res_str = "".join(map(str, result)).lstrip("0")
        print(res_str)

        return res_str

# Python map kya karta hai?
# map(function, iterable) ek iterator return karta hai.

# Har element of iterable pe function apply karta hai.

#         Why map(str, result)?
# map(str, result) converts each integer in the list into a string.

# result array mein digits integer form mein hote hain.

# map(str, result) har digit ko string banata hai.

# "".join(...) un strings ko ek continuous number string bana deta hai.

# .lstrip("0") starting ke extra zeros hata deta hai.