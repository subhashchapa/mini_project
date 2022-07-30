from random import sample
sc=0
def menu():
	print("1.add questions")
	print("2.take the quiz")
	print("3.get the score")
	print("4.exit")
def addquestions():
	print("1.add through console")
	print("2.add through file copy")
	cho=int(input("enter your console"))
	if cho==1:
		print("adding questions through console")
		qfile=open("qbank.txt","a");
		q=input("enter the question")
		op1=input("op1")
		op2=input("op2")
		op3=input("op3")
		op4=input("op4")
		ans=input("answer:")
		s=""
		s=q+','+op1+","+op2+","+op3+","+op4+","+ans+"\n"
		qfile.write(s)
		qfile.close()
	elif cho==2:
		print("adding questions through file")
		src=input("enter a filename")
		ifile=open(src,"r")
		qfile=open("qbank.txt","a")
		qfile.write(s)
		ifile.close()
		qfile.close()


def takequiz(ql):
	global sc
	for q in ql:
		l=q[0].split("\n")
		print(L[0])
		i=1
		for op in l[1:]:
			print(i,op)
			ans=int(input("enter ur answer:"))
		if(ans==q[-1]):
			sc=sc+1
		else:
			sc=sc-0.25
while True:
	menu()
	ch=int(input("enter your choice"))
	if ch==1:
		addquestions()
	elif ch==2:
		qfile=open("qbank.txt","r")
		for line in qfile:
			qc=(line.strip().split(","))
			ql=qc[0:5]
			s="\n".join(ql)
			print(s)
			questions.append(s,qc[5])
			n=int("how many questions you wanna add")
			rl=sample(range(len(questions)),n)
			ql=[]
			for i in rl:
				ql.append(questions[i])
			takequiz(ql)
	elif ch==3:
		print("thank u for subemitting:")
		print("your score is:",sc)
	elif ch==4:
		print("exit from application")
		exit()
