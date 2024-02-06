class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for stng in strs:
            for c in stng: encoded_str += str(ord(c)) + '.'
            encoded_str += ','
                
        return encoded_str
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> List[str]:
        strs_decoded = []
        strs1 = s.split(',')[:-1]
        for stng in strs1:
            strs2 = stng.split('.')[:-1]
            elem = [chr(int(ns)) for ns in strs2]
            strs_decoded.append(''.join(elem))
        return strs_decoded
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))