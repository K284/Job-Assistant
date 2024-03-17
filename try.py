'''states = ['new delhi', 'jammu and kashmir', 'jharkhand', 'bihar', 'rajasthan', 'punjab', 'odisha', 'himachal pradesh',
          'madhya pradesh', 'manipur', 'meghalaya', 'karnataka', 'kerala', 'tamil nadu', 'uttar pradesh', 'maharashtra',
          'sikkim', 'nagaland', 'tripura', 'andhra pradesh', 'arunachal pradesh', 'assam', 'chhattisgarh', 'goa'
    , 'gujarat', 'haryana', 'telangana', 'uttarkhand', 'west bengal', 'ladakh']
sector = [['Information Technology', 'Telecommunications', 'Hotels', 'Media', 'Banking', 'Tourism'],
          ['Tourism', 'Agriculture', 'Service'], ['Agriculture' , 'Tourism'],
          ['Food Processing', 'Dairy','Textile', 'Leather', 'Renewable Energy', 'Tourism'],
          ['Textile', 'Rugs', 'Woolen goods', 'Vegetable oil', 'Dyes'],
          ['Agro-based industrial units', 'Machinery units', 'Chemical units'],
          ['Manufacturing', 'Mining', 'Quarrying', 'Electricity', 'Gas supply', 'Water supply', 'Construction'],
          ['Agriculture', 'Tourism', 'Pharmaceutical'],
          ['Textile manufacturing', 'Automobiles', 'Food processing', 'Engineering', 'Agriculture equipment manufacturing'],
          ['Ecotourism', 'Crafts making business', 'Soap making business', 'Jewellery making'],
          ['Florism', 'Tourism','Beautician','Handloom  and Handicrafts'],
          ["Automobile", 'Agro', 'Aerospace', 'Textile and Garment', 'Biotech',"Heavy Engineering Industries"],
          ['Handloom & Handicraft', 'Khadi & Village', 'Cashew', 'Tourism','Agriculture & Livestock',
           'Oil Refining & Petrochemicals','Ship Building'],
          ['Automobiles','Electronics Hardware','Software Services','Medical Tourism','Entertainment',
           'Petrochemicals','Textiles','Banking & Finance'],
          ['ITE','Agro and Food Processing','Electronics Manufacturing','Tourism','Renewable Energy',
           'Handloom and Textiles.'],['Manufacturing', 'Mass Media', 'International Trade', 'Petroleum', 'Tourism',
            'Fashion and Apparel', 'Aerospace'],['Pharmaceuticals','Eco-tourism','Food Processing','Breweries',
            'Cosmetics','Security Ink','Mattress','Corrugated Boxes'],
          ['Agro-based and Forest-based industries', 'Horticulture', 'Food processing', 'Mining', 'Tourism','Handlooms',
            'Handicrafts'],['Human Resources Development', 'Banking', 'Railway', 'Police', 'Agriculture', 'Defence',
            'Teaching','Tourism', 'Transport', 'Urban Development', 'Rural Development', 'Finance sector'],
          ['Automobiles and Auto components Industry', 'Spices', 'Mines and Minerals',
            'Textiles and apparels', 'IT industry', 'Bulk drugs and pharmaceuticals', 'Horticulture', 'Poultry farming'],
          ['agriculture', 'art and crafts', 'weaving', 'cane and bamboo', 'horticulture',
           'power and mineral-based industry'],['Railways', 'Defence','Agriculture','Banking','Teaching'],
          ['Agriculture','Food Processing','Handloom','Pharmaceutical Industry','fishing','tourism', 'horticulture', 'poultry farming'],
          ['fishing', 'agriculture', 'tourism','pharmaceuticals','Software Jobs','Hospitality Jobs',
           'Food & Packaged Food Jobs','Telecom Jobs','Insurance Jobs'],
          ['Agriculture','chemicals and petrochemicals','pharmaceutical', 'textile'],
          ['Agro-Based', 'Food Processing','Allied Industry','Automobiles and Automotive Components',
           'Footwear and Accessories','Handloom', 'Hosiery', 'Textile and Garments Manufacturing',
           'Health','Pharmaceutical Industry','Research and Development','Frontier Technologies'],
          ['Automobiles and auto components industry', 'spices', 'mines and minerals', 'textiles and apparels',
           'pharmaceutical', 'horticulture', 'poultry farming'],
          ['Floriculture', 'Horticulture', 'Pharmaceuticals','Biotechnology', 'FMCG','Electronics',
           'Hydro Power', 'Tourism','ICT '],['Social media','Scientific writing','Marketing','Cotton and textile industry',
            'Tea industry','Food processing industry','Tourism Industry','Information technology'],['Agriculture',
            'Horticulture','Milk & dairy','Tourism']]
a = open("Sectors.txt",'w')
for i in range(0,30):
    a.write(states[i]+' | '+str(sector[i])+'\n')'''

'''def city():
    f = open('States', 'r')
    s = f.readlines()
    st = input("Enter your state: ")
    for line in s:
        if st.lower() in line:
            with open("Sectors.txt", 'r') as g:
                for line in g:
                    if st in line:
                        print(line)
                        break
                else:
                    print("State Not found. Try Again")

    f.close()

def feedback(c):
    with open('FB', 'a+') as Fb:
        Fb.write(c+'\n')

def detail(a,info2):#file to save age,info1
    logindetail=str([a,info2])
    print("Your details:", logindetail)
    LD=open("logindetaile.txt","a+")
    LD.write(logindetail+"\n")
    LD.close()

def register():
    name=input("Please enter your name:")
    eid=input("Please enter your email id:")
    import random
    idf = random.random()
    ids = random.randint(0,10)
    ID=idf+ids*1000
    print("Generated userid for your future use=",ID)
    info2=[name,eid,ID]
    detail(a,info2)



def login():
    print("WELCOME BACK!")
    eid=input("Please enter your email id to retrive your details and past records:")
    LD=open("logindetaile.txt","r")
    id = LD.read()
    if eid in id:
        print("\nSuccessfully logined!!")
    else:
        print("THIS USERID IS NOT FOUND!!PLEASE CHECK")


def sector(sec):
    with open('secdetails.txt','r') as file:
        for line in file:
            if sec.lower() in line.lower():
                print(line)
                break
        else:
            print("Not found. Try Again!!")
def criteria():
    print()








a= int(input("Age: "))
if 18> a>=0:
    print("W are sorry u cant use this program.")
while a>=18:
    print("\n1.Register or Login 2. Enter State 3. Enter Sector 4. Feedback 5. Exit")
    ch = input("\nEnter your choice: ")
    if ch == "1":
        r = input("\nWould you like to register yourself?[y/n]:")
        if r == 'n':
            ln = input("\nThen do you want to login yourself?[y/n]:")
            if ln == "n":
                print("\nNot registering yourself would mean you will be able to use this program only once.")
                R = input("\nAre you sure you do not want to register?[Y/N]:")
                if R.lower() == 'y':
                    pass
            else:
                login()
        else:
            register()
            print("\nSuccessfully registered!!")
    elif ch == "2":
        city()
    elif ch == "3":
        sec = input("\nWhich sector do you want to select? ")
        sector(sec)
    elif ch == "4":
        c = input("\nPlease give feedback about us: ")
        feedback(c)
    elif ch == "5":
        print("\nThank you for using this program")
        break
    else:
        print("\nWrong option. Try Again!!!")
'''
from tkinter import *
from tkinter import messagebox

def sector():
    global sec
    sec = sectorr.get()
    with open('secdetails.txt', 'r') as p:
        for lline in p:
            if sec in lline:
                frame10 =Tk()
                frame10.geometry('2000x100')
                l = lline.split(".")
                k = 0
                for i in l:
                    secdetLabel = Label(frame10, text=i).grid(row=k, column=0)
                    k += 1
            #but = Button(frame10, text="Done Reading", command=criteria).grid(row=4, column=0)
                break
        else:
            messagebox.showwarning("Warning","Not found. Try Again!!")

st = input("State: ")
f = open('States', 'r')
s = f.readlines()
for line in s:
    if st.lower() in line.lower():
        with open("Sectors.txt", 'r') as g:
            for linee in g:
                if st.lower() in linee.lower():
                    frame9 = Tk()
                    frame9.geometry('1000x100')
                    statelabel = Label(frame9,text = linee).grid(row = 0,column = 0)
                    sectorLabel = Label(frame9, text="Enter the sector chosen:").grid(row=1, column=0)
                    sectorr = StringVar()
                    sectorEntry = Entry(frame9, textvariable=sectorr).grid(row=1, column=1)
                    button = Button(frame9,text = "Ok",command = sector).grid(row = 2,column = 0)
                    break

            else:
                messagebox.showwarning("Warning","State Not found. Try Again")
frame9.mainloop()
