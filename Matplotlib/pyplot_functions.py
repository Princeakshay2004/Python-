import matplotlib.pyplot as mplt
import pandas as pd 

#matplotlib with pandas 

df1 =pd.DataFrame({
        "Name":['Akshay','Jivan','Ravi','Sudarshan','Aadarsh'],
        "Age":[22,34,12,42,32],
        "weight":[45,33,56,48,64]
})
    
# To plot line graph
mplt.plot(df1['Name'],df1['Age'],df1['weight'])
# To add grid lines
mplt.grid()
# To add lables on graph
mplt.xlabel("Names of Students")
mplt.ylabel("Heights & Weights ")
# To add title on graph
mplt.title("Students height age and weight Representation")
# To display the figure
mplt.show()