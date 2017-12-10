from datetime import *

#Classes lies aux differents utilisateurs du projet
class Client:
    def __init__(self, nomInit, prenomInit, emailInit, passwordInit):
        self.__nom=nomInit
        self.__prenom=prenomInit
        self.__email=emailInit
        self.__password=passwordInit
        self.__myExpenses=[]
    def changeEmail(self, newEmail):
        self.__email=newEmail
    def __str__(self):
        return "Client " + self.__prenom + " " + self.__nom
    def

class Admin:
    def __init__(self, username, prenom, nom, email, password):
        self.__username=username
        self.__prenom=prenom
        self.__nom=nom
        self.__email=email
        self.__password=password
        self.__expenses=[]
    def changePassword(self, nemPassword):
        self.__password=nemPassword
    def giveUsername(self):
        return self.__username
    def addexpense(self, expenseid):
        self.__expenses=Admin.__expense.append(expenseid)

class expense:
    __prefix="EXP-"
    __nombre=0
    def __init__(self,):
        self.__expenseAmount=0
        self.__identifiant=expense.__prefix + str(expense.__nombre)
        self.__involvedUsers=[]
        expense.__nombre+=1
    def newExpense(self, creator, payer, amount):
        self.__creator=creator
        self.__expenseAmount=amount
        self.__involvedUsers=expense.__involvedUsers.append((payer, 1))
        self.__createdDate=datetime.now()
        nusers=[]
        restart=False
        while restart == False:
            print "Avec combien de users partager la dépense ?"
            x=input("?")
            counter=0
            while counter < x:
                print "Avec quel user? Spécifiez le username du user #" + (counter + 1)
                y=input("?")
                nusers=nusers.append((y,0))
                counter+=1
            print "Validez que les users suivants doivent être ajoutés:"
            print "-"*70
            userscount=nusers.count()
            for user,pctg in nusers:
                print "username :" + user + "; proportion à appliquer par défaut : " + str(1/userscount)
            x=input("Yes or No?")
            if str(x).lower == "y":
                for user,proportion in nusers:
                    user.addexpense(self.__identifiant)
                    self.__involvedUsers=expense.__involvedUsers.append((user, 1/userscount))
                restart=True
            else:
                print "restarting new expense"
                break






#Autres classes

user1 = Admin("Mr.Patate", "Martin", "Duluins", "martin.duluins@gmail.com", "Welcome")


print 'created'
print user1.giveUsername()

firstExpense=expense()
