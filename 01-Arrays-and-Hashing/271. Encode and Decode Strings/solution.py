from typing import List

class Codec:
    """
    Encode and Decode Strings
    Uses length prefix with delimiter for unambiguous encoding.
    """
    
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: length + '#' + string content
        Example: ["hello", "world"] -> "5#hello5#world"
        """
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return ''.join(res)
        
    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.
        """
        res = []
        L = 0
        while L < len(s):
            R = L
            # Find the '#' delimiter
            while s[R] != '#':
                R += 1
            # Extract length
            length = int(s[L:R])
            R += 1  # Move past '#'
            # Extract the word
            word = s[R:R + length]
            res.append(word)
            L = R + length
        return res


# Alternative: Your codec can be used like this
# codec = Codec()
# result = codec.decode(codec.encode(strs))

