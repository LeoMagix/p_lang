from invite_fn import invite, confirm_invite

invited_guests = ['usain bolt', 'michael jordan', 'elon musk', 'zara hadid', 'nikola tesla']

sent_invites = []

invite(invited_guests[:], sent_invites)

print("\nEnter name on the guest list.")

guest = input('').lower()

confirm_invite(guest, invited_guests)
