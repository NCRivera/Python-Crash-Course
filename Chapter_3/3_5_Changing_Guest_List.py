#3-5. Changing Guest List

guests = ['maria', 'celia', 'sheldy']

print("You, " + guests[0].title() + " are formally invited to my dinner, tomorrow night.")
print("You, " + guests[1].title() + " are formally invited to my dinner, tomorrow night.")
print("You, " + guests[2].title() + " are formally invited to my dinner, tomorrow night.")
new_invitee = "Rosalyn"
print("Unfortunately, " + guests[1].title() + " will not be coming so I will now invite " + new_invitee + ".")
guests[1] = new_invitee

print("You, " + guests[1].title() + " are formally invited to my dinner, tomorrow night.")
