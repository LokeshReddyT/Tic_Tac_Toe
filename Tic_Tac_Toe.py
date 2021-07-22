'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

a=[[" "," "," "],[" "," "," "],[" "," "," "]]


def conditions():
  test=0
  for i in range(len(a)):
    if a[i][0]==a[i][1]==a[i][2]!=" ":
      if a[i][0]==1:
        print(players_names[1], "won the match")
        return 0
      else:
        print(players_names[0], "won the match")
        return 0
    if a[0][i]==a[1][i]==a[2][i]!=" ":
      if a[0][i]==1:
        print(players_names[1], "won the match")
        return 0
      else:
        print(players_names[0], "won the match")
        return 0
  if a[0][0]==a[1][1]==a[2][2]!=" ":
    if a[0][0]==1:
        print(players_names[1], "won the match")
        return 0
    else:
        print(players_names[0], "won the match")
        return 0
  if a[0][2]==a[1][1]==a[2][0]!=" ":
    if a[0][2]==1:
        print(players_names[1], "won the match")
        return 0
    else:
        print(players_names[0], "won the match")
        return 0
  for i in range(len(a)):
    for j in range(len(a[0])):
      if a[i][j]!=" ":
        test=test+1
  if test==9:
    print("Game Tie")
    return 0
  return 1
b={1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}
players_names=[]
print("Enter name of player no:- 1")
player_1=input()
players_names.append(player_1)
print("Your letter is 0")
print("Enter name of player no:- 2")
player_2=input()
players_names.append(player_2)
print("Your letter is 1")
die=0
while True:
  if die==2:
      die=0
  for i in range(len(a)):
    print("*-----*-----*-----*")
    print("| ",a[i][0]," | ",a[i][1]," | ",a[i][2]," |")
    if i==2:
      print("*-----*-----*-----*")
  while True:
    print(players_names[die],"select a square between 1 - 9")
    choice=int(input())
    u,k=b[choice]
    if a[u][k]==" ":
      a[u][k]=die
      break
    else:
      print("unable to select that square. choose another")
  die=die+1
  breaks=conditions ()
  if breaks==0:
    for i in range(len(a)):
      print("*-----*-----*-----*")
      print("| ",a[i][0]," | ",a[i][1]," | ",a[i][2]," |")
      if i==2:
        print("*-----*-----*-----*")
    break
  
