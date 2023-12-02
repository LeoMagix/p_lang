#One Way to Delete Repeated Values in a List.
names = ['james', 'john', 'james', 'jimmy', 'james', 'james', 'jack']
print(names)

while 'james' in names:
    names.remove('james')
print(names)
