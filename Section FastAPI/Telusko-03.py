# Uvicorn server runs on port 8000
# currently our frontend is running on Port 3000

# How to run the main.py
#     we can run the code using terminal, but it ll print on the terminal, 
#     We want it on th web page, How to do:
#         The function should be called by the web page
#         FUnction should now return , not print

# Nwo server should also be running
#     We need to use the webserver Uvicorn
#     uvicorn file_name --reload
#             we might get an error as:
#             Error loading ASGI app. Import string "main" must be in format "<module>:<attribute>".
# module is our file.
# Attribute is missing:
#     We are using Web Framework that is FastAPI. WE need to mention that
#     We need to create object of FastAPI AND import Fastapi
#     once object is created, we need to pass that as well in the command

#     uvicorn file_name:attribute(object)_name --reload

# Server is now running, but shows not found , why is it so ?
#     What shows in website at PORT8000
#      {   
#       "detail": "Not Found"
#     }

#     Concept of  RestAPI
#         There are 2 things : CLient and Server
#         Job of Server:
#             To give services,
#             Server can be File server, Web server . Eg: File Server - gives file to whoever who is asking for this file
#                 Eg File Server : If CLient A request for file to the Server. File Server searches for the file, got the file and then gives response.
#                     Communication here happens by FTP/SFTP
#                 Eg Web Server : If CLient A request for a data to the Server. Web Server searches for the data , got the data and then gives response.
#                       Data here can be in format of HTML/JSON
#                         Why these specific format ?
#                         - In real world, we all use Webpages
#                             So when client says to give the website: amazon.com
#                             Server says : Take the webpage and view on the browser
  
