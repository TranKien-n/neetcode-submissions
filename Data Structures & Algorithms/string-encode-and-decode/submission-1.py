class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

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