class Nguoi(object):
    def getGender(self):
        return "Unknown"


class Nam(Nguoi):
    def getGender(self):
        return "Nam"


class Nu(Nguoi):
    def getGender(self):
        return "Nữ"


# Test
aNam = Nam()
aNu = Nu()

print(aNam.getGender())  # Output: Nam
print(aNu.getGender())   # Output: Nữ
