from analytics.data_analytics import data_analysis ,data_plotting
from src.file_manager import DATA_DIR
from .data_operations.request_operations import add_request, view_request ,update_request ,delete_request
import pandas as pd
from user_interface.user_interaction_handler import ai_menu
data_file = DATA_DIR/"requests.json"
data = pd.read_json(data_file)

async def Menu():
    print("Which funcitonlity you want to perform :" \
    " \n1. Add Request " \
    "\n2. View Request " \
    "\n3. Update Request"\
    "\n4. Delete Request"\
    "\n5. Data Analysis " \
    "\n6. Data Plotting " \
    "\n7. Ask Ai"\
    "\n8. Exit")
    option_selected = input().strip()
    if option_selected == "1" :
        add_request()
    elif option_selected =="2" :
        view_request()
    elif option_selected =="3" :
        update_request()
    elif option_selected =="4" :
        delete_request()
    elif option_selected == "5" :
        data_analysis(data=data)
    elif option_selected =="6":
        data_plotting(data=data)
    elif option_selected =="7" :
       await ai_menu()
    else :
        return
    
