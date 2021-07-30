coach = "William"
def yesNoQuestion(prompt):
    ans = ""
    while True:
        try:
            ans = input(prompt)
            ans = ans.upper()
            if ans[0] != 'Y' and ans[0] != 'N':
                print("Please Enter (Y)es or N(o)")
                continue
            else:
                break
        except:
            print("Please enter (Y)es or N(o)")
            continue
    return ans[0] == 'Y'

online = yesNoQuestion("online? ")

name = input("Name: ")
while len(name) > 30:
  print("ENTER THE NAME!")
  name = input("name: ")


def printer(name,list_of_activities):
  print("Hiya,")
  print("Today "+name+" worked on:")
  for activity in list_of_activities:
    print(" -",activity)

  print("\nUntil next time at the Coder School",end="")
  print(" online!" if online else "!")
  print("- "+coach+" (Code Coach)")

def getActivities():
  stuff = []
  while True:
    activity = input("Enter: ")
    if activity == "":
      break
    else:
      stuff.append(activity)
  return stuff

printer(name, getActivities())