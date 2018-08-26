#3-6. More Guests
guests = ['maria', 'celia', 'sheldy']

print("You, " + guests[0].title() + " are formally invited to my dinner, tomorrow night.")
print("\nYou, " + guests[1].title() + " are formally invited to my dinner, tomorrow night.")
print("\nYou, " + guests[2].title() + " are formally invited to my dinner, tomorrow night.")
new_invitee = "rosalyn"
print("\nUnfortunately, " + guests[1].title() + " will not be coming so I will now invite " + new_invitee.title() + ".")
guests[1] = new_invitee

print("You, " + guests[1].title() + " are formally invited to my dinner, tomorrow night.")

print("\nI wanted to let all of you know that we now have a bigger table. \nSo I will be inviting more people to the party")

new_guest_1 = 'flor'
print("\nI will now invite " + new_guest_1.title() + ".")
guests.insert(0, new_guest_1)

new_guest_2 = 'Juan'
print("\nI will now invite " + new_guest_2.title() + ", as well.")
guests.insert(2, new_guest_2)

new_guest_3 = 'Pauline'
print("\nAnd finally, \nI will now invite " + new_guest_3.title() + ".")
guests.append(new_guest_3)

print("\nThe new guest list is now: ")

for invitee in guests:
    print(invitee.title())

print("\nAnd time to send the new invitations\n")

for invited in guests:
    message = ", you are formally invited to my party."
    print(invited.title() + message + "\n")