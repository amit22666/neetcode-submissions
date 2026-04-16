class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded = ''
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        i = 0
        decoded = []
        while i < len(s):
            # Find the delimiter #
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length]) #important catch last if not included
            i = j + 1 + length
        return decoded
