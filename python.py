from cgitb import text


class car:
    
    def __init__(self, ismi, familyasi):
        self.ismi = ismi
        self.familyasi = familyasi
        
    def __str__(self):
        return f"meni ismim {self.ismi} familyam {self.familyasi}"
    
    
class Malibu(car):
    def __init__(self, ismi, familyasi, yoshi):
        super().__init__(ismi, familyasi)
        self.yoshi = yoshi
        
    def __str__(self):
        text = super(Malibu, self).__str__()
        text += f" bundan tashqari meni yoshim {self.yoshi}"
        return text

class Hobbi(Malibu):
    def __init__(self, ismi, familyasi, yoshi, hobbi):
        super().__init__(ismi, familyasi, yoshi, hobbi)
        self.hobbi = hobbi
        
    def __str__(self):
        hobbies = super(hobbies, self).__str__
        hobbies += f" meni hobbiyim {self.hobbi}"
        return hobbies
    
    

ism1 = Malibu("abdugani", "risliqboyev", 27, "fudbol oynash")
print(ism1) 