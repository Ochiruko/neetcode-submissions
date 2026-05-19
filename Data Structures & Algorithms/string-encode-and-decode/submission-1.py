def encode_str(s: str) -> str:
    return "@" + s.replace("\\", "\\\\").replace("@", "\\@")

def decode_str(s: str, pos: int) -> tuple[str, int]:
    pos += 1 # skip the @
    from_pos = pos
    while pos < len(s) and s[pos] != '@':
        if s[pos] == '\\':
            pos += 1
        pos += 1
    decoded = s[from_pos:pos].replace("\\@", "@").replace("\\\\", "\\")
    return (decoded, pos)

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_strs = []
        for s in strs:
            encoded_strs.append(encode_str(s))
        return "".join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        pos = 0
        decoded_strs = []
        while pos < len(s):
            (decoded_str, new_pos) = decode_str(s, pos)
            pos = new_pos
            decoded_strs.append(decoded_str)
        return decoded_strs