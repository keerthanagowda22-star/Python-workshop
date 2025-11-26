class aadhar:

    def __init__(self,name,aadhar_number,dob,finger_print,retina):
        self.name=name
        self.aadhar_number=aadhar_number
        self.dob=dob
        self.finger_print=finger_print
        self.__retina=retina

    def display_userdata(self):
        print(f"retina:{self. __retina} aadhar number: {self.aadhar_number}")

    def getretina(self):
        return self.__retina

var=aadhar("keer",64816619,"5 dec 2003","hggggg","tttttttt")

var.display_userdata()
retina_var=var.getretina()
print(retina_var)