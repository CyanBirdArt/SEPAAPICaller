################# Development List:
# Make the userQueryFunction a drop down of all the options
# Put in a save as option to name the file output

import requests
import csv
import tkinter as tk
  
def main():   
    root=tk.Tk()
    
    # setting the windows size
    root.geometry("600x400")
    
    # declaring string variable
    # for storing variables
    userQueryFunctionVar=tk.StringVar()
    userQueryArgumentsVar=tk.StringVar()
    userReturnFieldsVar=tk.StringVar()
    userReturnFieldsVar.set("&returnfields=all")
    
    def submit():
    
        userQueryFunctionResult=userQueryFunctionVar.get()
        userQueryArgumentsResult=userQueryArgumentsVar.get()
        userReturnFieldsResult=userReturnFieldsVar.get()
        
        print("The userQueryFunction is : " + userQueryFunctionResult)
        print("The userQueryArguments is : " + userQueryArgumentsResult)
        print("The userReturnFields is : " + userReturnFieldsResult)

        userQueryFunction = userQueryFunctionResult # Chosen by user from list of options as defined here: https://timeseriesdoc.sepa.org.uk/api-documentation/api-function-reference/principal-query-functions/
        userQueryArguments = userQueryArgumentsResult 
        userReturnFields = "&returnfields=all" # If not changed have all fields else enter fields manually

        ## Defining variables that will make up the url
        APIRootURL = "https://timeseries.sepa.org.uk/KiWIS/KiWIS?" # Required & Hard coded, 
        backEndConfig = "service=kisters&type=queryServices&datasource=0&request=" # Required & Hard coded,
        queryFunction = userQueryFunction           # Required, Chosen by user from finite list of options
        queryArguments = userQueryArguments         # Updated by user, have hard coded options then also free text  
        returnFields = userReturnFields             # Default to return all fields but option for user to enter manually
        returnFormat = "&format=csv"                # Hard coded, always csv for output by this script

        if queryFunction == "":
            print("queryFunction is required")

        # Concatinating the url from above variables
        url = APIRootURL + backEndConfig + queryFunction + queryArguments + returnFields + returnFormat

        # API call to get data using the url
        response = requests.get(url)

        # If get response is true (200 response code) then carry on with script
        if response:
            print('Success!')

            # Text from api get call
            output = response.text
            # Splitting text by ';' as this is the delimiter in data
            output = output.split(';')
            filepathToSave = '.\Outputs\SEPA_API_Data_' + queryArguments + returnFields + '.csv'
            with open(filepathToSave, 'w', newline='\n') as outfile:
                writer = csv.writer(outfile,delimiter=',',quotechar=' ')
                writer.writerow(output)
        else:
            # Else an error has occured 
            print('An error has occurred in get request to api.')
            
        userQueryFunctionVar.set("")
        userQueryArgumentsVar.set("")
            
    # creating a label for variable using widget Label
    userQueryFunction_label = tk.Label(root, text = 'Query Function', font=('calibre',10, 'bold'))
    
    # creating a entry for input variable using widget Entry
    userQueryFunction_entry = tk.Entry(root,textvariable = userQueryFunctionVar, font=('calibre',10,'normal'))
    
    # creating a label
    userQueryArguments_label = tk.Label(root, text = 'Query Arguments', font = ('calibre',10,'bold'))
    
    # creating a entry 
    userQueryArguments_entry=tk.Entry(root, textvariable = userQueryArgumentsVar, font = ('calibre',10,'normal'))

    # creating a label
    userReturnFields_label = tk.Label(root, text = 'Return Fields', font = ('calibre',10,'bold'))
    
    # creating a entry 
    userReturnFields_entry=tk.Entry(root, textvariable = userReturnFieldsVar, font = ('calibre',10,'normal'))
    
    # creating a button using the widget
    # Button that will call the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    
    # placing the label and entry in
    # the required position using grid
    # method
    userQueryFunction_label.grid(row=0,column=0)
    userQueryFunction_entry.grid(row=0,column=1)
    userQueryArguments_label.grid(row=1,column=0)
    userQueryArguments_entry.grid(row=1,column=1)
    userReturnFields_label.grid(row=2,column=0)
    userReturnFields_entry.grid(row=2,column=1)
    sub_btn.grid(row=3,column=1)


    # performing an infinite loop
    # for the window to display
    root.mainloop()

if __name__=="__main__":
    main()







