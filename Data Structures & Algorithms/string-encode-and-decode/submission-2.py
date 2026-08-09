class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        
        for s in strs:
            encoded_string.append(f'{len(s)}#{s}')

        encoded_string = ''.join(encoded_string)
        
        #return ''.join(f'{len(s)}#{s}' for s in strs)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            # Find the delimiter '#'
            j = s.find('#', i)
            # Extract length
            length = int(s[i:j])
            # Get the actual word using length
            decoded_strs.append(s[j+1:j+1+length])
            # Move to the next word
            i = j + 1 + length
        return decoded_strs