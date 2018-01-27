import random

class Patient(object):
    def __init__(self, ID, name, allergies = [], bedNum = None):
        self.ID = ID
        self.name = name
        self.allergies = allergies
        self.bedNum = bedNum

    def info(self):
        print "Name: ", self.name
        print "ID#: ", self.ID
        print "Allergies: ", self.allergies
        print "Bed Num: ", self.bedNum

    def addAllergy(self, newAllergy):
        self.allergies.append(newAllergy)
        return self


class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.fullBeds = []

    def admit(self, patient):
        #rolls for a random, empty bed
        if len(self.patients)+1 <= self.capacity:
            #rolls for a random bed that's not already full
            randBed = random.randint(1, self.capacity)
            while randBed in self.fullBeds:
                randBed = random.randint(1, self.capacity)
                print randBed
            patient.bedNum = randBed
            self.fullBeds.append(randBed)
            self.patients.append(patient)
            print "Admitted: ", patient.name
        else:
            print "Sorry, {} Hospital is at capacity :(".format(self.name)
            print ""
        return self
    
    def discharge(self, patient):
        self.fullBeds.remove(patient.bedNum)
        patient.bedNum = None
        self.patients.remove(patient)
        print "Discharged: ", patient.name
        return self

    def info(self):
        for patient in self.patients:
            if patient.bedNum is not None:
                patient.info()
                print ""

habiba = Patient(999909, "Habiba Mohamed")
lucian = Patient(666666, "Lucian el Chupa")
frankie = Patient(101010, "Frankie Binary")
excelcior = Patient(876543, "EXCELCIOR THE GREAT", ["Shellfish", "Ambien"])

sacredHeart = Hospital("Sacred Heart", 3)

sacredHeart.admit(habiba).admit(lucian).admit(excelcior).admit(frankie).info()
sacredHeart.discharge(dustin).admit(frankie).info()
  
