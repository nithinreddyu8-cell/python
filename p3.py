import pickle
while True:
    print('Main menu-operations on binary file')
    print('1.Create')
    print('2.Display')
    print('3.view 90% and above')
    print('4.Exit')
    opt=int(input('Enter your option:'))
    if opt==1:
        f=open('student.dat','wb')
        o=open('newstud.dat','wb')
        x=int(input('How many student data you want to input?'))
        for i in range(x):
            nam=input('Name:')
            L1=int(input('Language marks:'))
            L2=int(input('English marks:'))
            P=int(input('Physics marks:'))
            C=int(input('Chemistry marks:'))
            M=int(input('Mathematics marks:'))
            CS=int(input('Computer science marks:'))
            tot=L1+L2+P+C+M+CS
            per=(tot/600)*100
            t=[nam,L1,L2,P,C,M,CS,tot,per]
            g=[nam,L1,L2,P,C,M,CS,tot,per]
            pickle.dump(t,f)
            if per>=90:
                pickle.dump(g,o)
        f.close()
        o.close()
    elif opt==2:
        f=open('student.dat','rb')
        try:
            while True:
                p=pickle.load(f)
                print(p)
        except:
            f.close()
    elif opt==3:
        print("student with>90 Marks")
        f=open('newstud.dat','rb')
        try:
            while True:
                o=pickle.load(f)
                print(o)
        except:
            print('No student have scored 90% and above\n')
        f.close()
    else:
        break

               