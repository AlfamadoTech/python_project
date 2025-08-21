# Unique voter system
registered_voters = {"John", "Smith", "Mike"}
#new voter name
new_voter = input('Enter your name here: ').title()
#Print message if voter already registered
if new_voter in registered_voters:
    print("Voter already registered")
#Add new voter to set of already registered voters
registered_voters.add(new_voter)
print(registered_voters)