st={10,50,5,12,15}

"""TO ADD ONE ELEMENT"""
st.add(90)
st.add('Bigdata')


"""TO ADD MULTIPLE ELEMENTS"""
st.update([12,'Python'])
print(st)


"""DELETING ONE ELEMENT"""
st.remove('Python')    or pop()
print(st)

"""DELETING MULTIPLE ELEMENT"""
st.difference_update([50,5])
print(st)