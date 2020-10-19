
class Hill:
    B = None
    B1 = None

    def __init__(self):
        self.B = [[9, 4], [5, 7]]
        self.B1 = [[5, 12], [15, 25]]
        
    def verifmatrice(self, a, b, c, d):
        a, b, c, d = int(a), int(b), int(c), int(d)
        det = a*d - b*c
        if self.pgcd(det, 26) != 1:
            return "invalide"
        detmod = 1
        while (det*detmod)%26 != 1:
            if detmod > 26:
                return "pb"
            detmod += 1
        self.B = [[a, b], [c, d]]
        self.B1 = [[(d*detmod)%26,(-b*detmod)%26],[(-c*detmod)%26, (a*detmod)%26]]
        return "valide"

    def pgcd(self, a, b):
        if(a < b):
            a, b = b, a
        r = a%b
        while(r != 0):
            a, b = b, r
            r = a%b
        return abs(b)
        
    
    
    def code_une(self, lt):
        return ord(lt) - ord("a")
        
    def code_mot(self, m):
        return list(map(self.code_une,m))
        
    def decode_une(self, c):
        return chr(c + ord("a"))
    
    def chifhill(self, n1, n2):
        tab = []
        tab.append((self.B[0][0]*n1 + self.B[0][1]*n2)%26)
        tab.append((self.B[1][0]*n1 + self.B[1][1]*n2)%26)
        return tab
        
    def dechifhill(self, n1, n2):
        tab = []
        tab.append(int((self.B1[0][0]*n1 + self.B1[0][1]*n2)%26))
        tab.append(int((self.B1[1][0]*n1 + self.B1[1][1]*n2)%26))
        return tab
    
    
    def coder(self, s):
        tab = []
        tabesp = []
        newS = ''
        s = s.lower()
        for i in range(len(s)):
            if s[i] == " ":
                tabesp.append(i)
        s = "".join(s.split(" "))
        code = self.code_mot(s)
        if len(s)%2 != 0:   
            for i in range(0, len(code)-1, 2):
                codage = self.chifhill(code[i], code[i+1])
                for j in range(len(codage)):
                    tab.append(codage[j])
            tab.append(code[len(code)-1])
        else:
            for i in range(0, len(code), 2):
                codage = self.chifhill(code[i], code[i+1])
                for j in range(len(codage)):
                    tab.append(codage[j])
        j=0   
        for i in range(len(tab)):
            if j in tabesp:
                newS = newS + " "
                j+=1
            newS = newS + self.decode_une(tab[i])
            j += 1
                
        return newS
    
    
    def decoder(self, s):
        tab = []
        tabesp = []
        newS = ''
        s = s.lower()
        for i in range(len(s)):
            if s[i] == " ":
                tabesp.append(i)
        s = "".join(s.split(" "))
        code = self.code_mot(s)
        if len(s)%2 != 0:  
            for i in range(0, len(code)-1, 2):
                codage = self.dechifhill(code[i], code[i+1])
                for j in range(len(codage)):
                    tab.append(codage[j])
            tab.append(code[len(code)-1])
        else:
            for i in range(0, len(code), 2):
                codage = self.dechifhill(code[i], code[i+1])
                for j in range(len(codage)):
                    tab.append(codage[j])
        j=0
        for i in range(len(tab)):
            if j in tabesp:
                newS = newS + " "
                j += 1
            newS = newS + self.decode_une(tab[i])
            j += 1
        
        return newS
        