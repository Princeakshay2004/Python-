import matplotlib.pyplot as mplt


x=[2,4,6,8,10]
y=[1,3,5,7,9]

fig,ax=mplt.subplots(2,2)


ax[0,0].plot(x,y, label='Avg ages',linestyle=":")
ax[0,0].legend()
ax[0,0].set_title("Line Graph")

ax[0,1].bar(x,y, label='Avg ages')
ax[0,1].legend()
ax[0,1].set_title("Bar Graph")

ax[1,0].pie(x, labels=y,autopct="%1.1f%%")
ax[1,0].legend(loc="upper left")
ax[1,0].set_title("Pie Graph")

ax[1,1].scatter(x,y,label="AVG age")
ax[1,1].legend()
ax[1,1].set_title("Scatter Graph")

fig.suptitle('Comprasion Of Plots')
mplt.tight_layout()
mplt.show()
