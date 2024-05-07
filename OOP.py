
class Computer():

    def __init__(self,marka,model,cpu,ram,qiymet):  
        self.marka=marka
        self.model=model
        self.cpu=cpu
        self.ram=ram
        self.qiymet=qiymet


    def qiymet_deyis(self,qiymet):
        self.qiymet=qiymet
    
    

comp1=Computer("Toshiba","Satellite","Intel_I7","DDR3_6gb",1500)
comp2=Computer("Acer","Aspire","Intel_I9","DDR5_12gb",2000)
comp3=Computer("Lenovo","Vivobook","Intel_I5","DDR4_8gb",1800)
comp4=Computer("Asus","Zenbook","Intel_I7","DDR5_16gb",2200)

