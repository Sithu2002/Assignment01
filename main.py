from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    first_name, set_first_name = use_state("")
    Last_name,set_Last_name=use_state("")
    Username,set_Username=use_state("")
    Email,set_Email=use_state("")
    password, set_password = use_state(0)



    def mysubmit(event):
        newtodo = {"first_name": first_name,"Last_name":Last_name,"Username":Username,"Email":Email,"password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  # function call to login function using the submitted data

    # looping data from alltodo to show on web



    list = []
    def handle_event(event):
        print(event)
        
        

    return html.div(
      {"style": 
                    {
                "display": "flex",
                "justify-content": "center",  # Centering horizontally
                "align-items": "center",      # Centering vertically
                "background-image": "url(https://c1.wallpaperflare.com/preview/98/528/893/sri-lanka-sri-lanka-peace.jpg)",  # Change URL here
                "background-color": "rgba(0,0,0,1)",
                "background-size": "cover",
                "height": "100vh",  # Adjust as needed
                "width": "100vw",   # Adjust as needed
                "margin": "15px",
                "padding": "15px",
            }

           },

        ## creating form for submission
        html.form(
        # Heading
               {"on submit": mysubmit},
                html.b(html.h1(
                    {"style": {"font-family": "Arial", "font-size": "40px","alignItems": "center","color":"rgba(255, 0, 0, 1)"}}
                    ,"Welcome to Sri Lanka🙏",)),
                html.br(),

                    html.b(html.h2(
                    {"style": {"font-family": "Arial", "font-size": "30px","alignItems": "center","color":"rgba(255, 0, 0, 1)"}}
                    ,'Sign-Up')),

                html.label(
                    {"style": {"font-family": "Arial", "font-size": "26px","alignItems": "center","color":"#e6fffa"}}
                    ,"First name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "First name",
                        "on_change": lambda event: set_first_name(event["target"]["value"]),
                    }
                    ),
                html.br(),

                html.label(
                    {"style": {"font-family": "Arial", "font-size": "26px","color":"#e6fffa"}}
                    ,"Last name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Last name",
                        "on_change": lambda event: set_Last_name(event["target"]["value"]),
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "26px","color":"#e0d6ff"}}
                    ,"Username"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Username",
                        "on_change": lambda event: set_Username(event["target"]["value"]),
                    }
                    ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "26px","color":"#e0d6ff"}}
                    ,"Gmail"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Email",
                        "on_change": lambda event: set_Email(event["target"]["value"]),
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "26px","color":"#e0d6ff"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                    }
                ),
                
                html.br(),
                html.p(""),
                # creating submit button on form
                html.button(
                    {
                        "type": "Create an Account",
                        "on_click":event(lambda event:mysubmit(event)),
                    },
                    "Create an Account",
                ),
    # add a button
                html.button(
                {
                    "type": "Reset",
                    "on_click":lambda event: set_first_name("") and set_Last_name("") and set_Username("") and set_Email("") and set_password(0),
                },
                "Reset",
                ),
                ),
        html.ul(list),  
        # html.img(
        # {
        # "src": "https://c1.wallpaperflare.com/preview/98/528/893/sri-lanka-sri-lanka-peace.jpg",
        # "class_name": "img-fluid",
        # "style": {"width": "1000px","height":"600px",
        # "justify_content": "right","margin_right":"0px",
        # "margin_left":"10px","margin_top":"20px","margin_bottom":"20px"},
        # "alt": "picture",}),
    )

app = FastAPI()

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI

app=FastAPI()

uri = "mongodb+srv://admin:admin123@cluster1.fchcxer.mongodb.net/"
# Create a new client and connect to the server
client=MongoClient(uri, server_api=ServerApi("1"))
DB=client["admin"]
collection=DB["assignment"]
# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



def login(
    login_data: dict,
):  # removed async, since await makes code execution pause for the promise to resolve anyway. doesnt matter.
    first_name= login_data["first_name"]
    Last_name=login_data["Last_name"]
    Username=login_data["Username"]
    Email=login_data["Email"]
    password = login_data["password"]

    # Create a document to insert into the collection
    document = {"first_name": first_name,"Last_name":Last_name,"Username":Username,"Email":Email,"password": password}
    # logger.info('sample log message')
    print(document)

    # Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}

configure(app, MyCrud)

