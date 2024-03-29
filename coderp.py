"""
BERTRAND Anthony

This file contains the class Hill.
The class Hill allows you to create an instance used in the 
encryption/decryption of strings following the Hill cipher method.

https://en.wikipedia.org/wiki/Hill_cipher#Encryption
"""

class Hill:
    IGNORED_CHAR = [" ", ",", ";", ".", "(", ")", "[", "]", "?", "!", "/", 
                    "\\", "é", "è", "à", "€", "$", "%", "\"", "\'", "ù",
                    "#", "&", "-", "_", "ç", "ê", "ë", "=", "+", "-", "*",
                    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    encrypt = None
    decrypt = None

    #--------------------------------------------------------------------------
    def __init__(self):
        self.encrypt = [[9, 4], [5, 7]]
        self.decrypt = [[5, 12], [15, 25]]

    #--------------------------------------------------------------------------
    def check_matrix(self, a, b, c, d):
        """check if the encrypt matrix is valid"""

        a, b, c, d = int(a), int(b), int(c), int(d)
        det = a*d - b*c
        if self.gcd(det, 26) != 1:
            return "invalide"
        detmod = 1
        while (det*detmod)%26 != 1:
            if detmod > 26:
                return "pb"
            detmod += 1
        self.encrypt = [[a, b], [c, d]]
        self.decrypt = [[(d*detmod)%26,(-b*detmod)%26],\
            [(-c*detmod)%26, (a*detmod)%26]]
        return "valide"

    #--------------------------------------------------------------------------
    def gcd(self, a, b):
        """find the greatest common divisor"""
        if(a < b):
            a, b = b, a
        r = a%b
        while(r != 0):
            a, b = b, r
            r = a%b
        return abs(b)
        
    #--------------------------------------------------------------------------
    def encrypt_letter(self, lt):
        """transform a letter into a number"""
        return ord(lt) - ord("a")

    #--------------------------------------------------------------------------  
    def encrypt_word(self, w):
        """transform the entire string into a list of numbers"""
        return list(map(self.encrypt_letter, w))
        
    #--------------------------------------------------------------------------
    def decrypt_letter(self, c):
        """transform a number into a letter"""
        return chr(c + ord("a"))
    
    #--------------------------------------------------------------------------
    def crypt_hill(self, n1, n2):
        """encrypt 2 letters"""
        tab = []
        tab.append((self.encrypt[0][0]*n1 + self.encrypt[0][1]*n2)%26)
        tab.append((self.encrypt[1][0]*n1 + self.encrypt[1][1]*n2)%26)
        return tab

    #--------------------------------------------------------------------------    
    def decrypt_hill(self, n1, n2):
        """decrypt 2 letters"""
        tab = []
        tab.append(int((self.decrypt[0][0]*n1 + self.decrypt[0][1]*n2)%26))
        tab.append(int((self.decrypt[1][0]*n1 + self.decrypt[1][1]*n2)%26))
        return tab
    
    #--------------------------------------------------------------------------
    def hill_encrypt(self, ascii):
        """encrypt a sentence with the hill method"""
        tab_ascii = []
        if len(ascii)%2 != 0:   
            for i in range(0, len(ascii)-1, 2):
                codage = self.crypt_hill(ascii[i], ascii[i+1])
                for j in range(len(codage)):
                    tab_ascii.append(codage[j])
            tab_ascii.append(ascii[len(ascii)-1])
        else:
            for i in range(0, len(ascii), 2):
                codage = self.crypt_hill(ascii[i], ascii[i+1])
                for j in range(len(codage)):
                    tab_ascii.append(codage[j])
        return tab_ascii

    #--------------------------------------------------------------------------
    def hill_decrypt(self, ascii):
        """decrypt a sentence with the hill method"""
        tab_ascii = []
        if len(ascii)%2 != 0:  
            for i in range(0, len(ascii)-1, 2):
                codage = self.decrypt_hill(ascii[i], ascii[i+1])
                for j in range(len(codage)):
                    tab_ascii.append(codage[j])
            tab_ascii.append(ascii[len(ascii)-1])
        else:
            for i in range(0, len(ascii), 2):
                codage = self.decrypt_hill(ascii[i], ascii[i+1])
                for j in range(len(codage)):
                    tab_ascii.append(codage[j])
        return tab_ascii

    #--------------------------------------------------------------------------    
    def code(self, s, way):
        """main function to encrypt/decrypt. It "removes" special caracters and put 
        them back to their initial places after the encryption.
        way==0 => encrypt, else decrypt"""

        # transforme une chaine de carac en liste d'entier (ASCII)  
        s = s.lower()
        encrypt = self.encrypt_word(s) 
        
        # enlève les carac spéciaux
        tab_ascii = []
        special_char = dict()
        for i in range(len(encrypt)):
            if encrypt[i] not in range(0, 26):
                special_char.setdefault(i, encrypt[i])
            else:
                tab_ascii.append(encrypt[i])

        # encrypte avec hill
        if way == 0:
            tab_ascii2 = self.hill_encrypt(tab_ascii)
        else:
            tab_ascii2 = self.hill_decrypt(tab_ascii)
        
        # remet les carac spéciaux
        for n in special_char.keys():
            tab_ascii2.insert(n, special_char.get(n))

        
        # transforme les nombres ascii en lettres
        tab_lettre = []
        for nb in tab_ascii2:
            tab_lettre.append(self.decrypt_letter(nb))

        # transforme le tableau en chaine de caractere
        new_s = ''
        for char in tab_lettre:
            new_s += char
        return new_s
    