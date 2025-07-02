import matplotlib.pyplot as plt
y=[2,3,4,5,6]
x=["ac","tv","fridge","mobile","car"]
plt.bar(x,y,color="blue")
plt.xlabel("product name")
plt.ylabel("item")
plt.title("yearly sales bar")
plt.show()