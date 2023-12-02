def show_msgs(messages):
    """List that stores a series of messages and prints them."""
    for message in messages:
        print(f"{message.title()}")
        print()

def send_messages(messages, sent_msgs):
    """Prints the message in the list, messages."""
    """And then moves it to a list of sent_msgs."""
    flag = True
    while flag:
        while messages:
            sent = messages.pop()
            
            print(f"\t{sent}")
            
            sent_msgs.append(sent)
        
        if messages == []:
            flag = False
            #break


mj = f"work ethic eliminates fear.- michael jordan"

bolt = f"competition is the easy part, the real work happens behind the scenes.- usain bolt"

giannis = f"Always want more but never be greedy.- giannis antetokounpo"

messages = [mj, bolt, giannis]

show_msgs(messages)

sent_msgs = []

print("\nThe following messages have been sent:")

send_messages(messages[:], sent_msgs)

print(f'\nArchived-\n{messages}')

print()

print(sent_msgs)

msgs = []

print(f"\nThese messages have been moved:")

send_messages(messages, msgs)

print(f'\n{messages}')
print()
print(msgs)

