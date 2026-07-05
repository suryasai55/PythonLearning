class Contact:
    def __init__(self,name,mobile,mail):
        self.name=name
        self.mobile=mobile
        self.mail=mail

    def display(self):
        print("Name:",self.name)
        print("phone Number:",self.mobile)
        print("E-mail:",self.mail)
        print("-----------------------------")
        
class Contact_Manager(Contact):
    def __init__(self,contacts):
        self.contacts=contacts
    def add_contact(self):
        name=input("Enter the name:")
        for i in self.contacts:
            if i.name.lower()==name.lower():
                print("Contact already exists")
                return
        mobile=int(input("Enter mobile no."))
        mail=input("Enter the mail:")
        self.contacts.append(Contact(name,mobile,mail))
        print("Contact added successfully")
        
    def display(self):
        print("===========Contact List===================")
        for contact in self.contacts:
            contact.display()

    def update(self):
        sname=input("enter the name to update:")
        for contact in self.contacts:
            if contact.name.lower() == sname.lower():
                print("What do you need to update:")
                print("\n1.mobile number")
                print("\n2.email")
                choice=int(input("Enter the choice 1 or 2:"))
                if choice==1:
                    new_mobile=int(input("Enter new mobile number:"))
                    contact.mobile=new_mobile
                elif choice==2:
                    new_mail=input("enter the mail")
                    contact.mail=new_mail
        
    def delete(self):
        d=input("Enter the contact name you want to delete")
        for contact in self.contacts:
            if d.lower()==contact.name.lower():
                self.contacts.remove(contact)
contact=[]
manager=Contact_Manager(contact)
while True:
    print('''choose the following operation:
                1.Add Contaact
                2.Display
                3.Update
                4.Delete
                5.Exit''')
    try:
        choice=int(input("Enter the choice"))
        if choice==1:
            manager.add_contact()
        elif choice==2:
            manager.display()
        elif choice==3:
            manager.update()
        elif choice==4:
            manager.delete()
        elif choice==5:
            print("Thank you for using this application")
            break
    except Exception as e:
        print(e)
        
