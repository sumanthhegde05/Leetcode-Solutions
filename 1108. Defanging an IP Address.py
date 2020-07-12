class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=address.split(".")
        a="[.]".join(a)
        return a
