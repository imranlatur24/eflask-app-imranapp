from flask import *
import sqlite3
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    try:
       action = req.get('queryResult').get('action')
       cityname = req.get('queryResult').get('queryText')
       not_yet = req.get('queryResult').get('queryText')
       
       #name = req.get('parameters').get('name.original')
       print('this is name of user '+not_yet)
       
    except AttributeError:
        return 'errro by json'
    print(req)
    print("Hallo world")
    #matching action value

    if action == "hi":
            return make_response(jsonify({'fulfillmentText': "I have a headphones",
                 "fulfillmentMessages":[
                  {"platform":"ACTIONS_ON_GOOGLE","simpleResponses":{"simpleResponses":[{"textToSpeech":"Hi! ","ssml":"","displayText":""}]},"message":"simpleResponses"},
      {"platform":"ACTIONS_ON_GOOGLE","suggestions":{"suggestions":[{"title":"test"},{"title":"ing"},{"title":"this"}]},"message":"suggestions"},
      {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["🙏🙏Hello! I’m Haia and I’m a robot agent 🤖. Welcome to Carnival Resort🏨"]},"message":"text"},
      {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["😊Not Yet","Yeah😎"],"title":"Are you already a client?😎"},"message":""},
      {"platform":"FACEBOOK","text":{"text":["🙏🙏Hello! I’m Haia and I’m a robot agent 🤖. Welcome to Carnival Resort🏨"]},"message":"text"},
      {"platform":"FACEBOOK","quickReplies":{"quickReplies":["😊Not Yet","Yeah😎"],"title":"Are you already a client?😎"},"message":""},
      {"platform":"SLACK","quickReplies":{"quickReplies":["test","ing","this"],"title":""},"message":"quickReplies"},
           ] }))

    elif action == "restartchat":
            return make_response(jsonify({'fulfillmentText': "I have a headphones",
                 "fulfillmentMessages":[
                  {"platform":"ACTIONS_ON_GOOGLE","simpleResponses":{"simpleResponses":[{"textToSpeech":"Hi! ","ssml":"","displayText":""}]},"message":"simpleResponses"},
      {"platform":"ACTIONS_ON_GOOGLE","suggestions":{"suggestions":[{"title":"test"},{"title":"ing"},{"title":"this"}]},"message":"suggestions"},
      {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["🙏🙏Hello! I’m Haia and I’m a robot agent 🤖. Welcome to Carnival Resort🏨"]},"message":"text"},
      {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["😊Not Yet","Yeah😎"],"title":"Are you already a client?😎"},"message":""},
      {"platform":"FACEBOOK","text":{"text":["🙏🙏Hello! I’m Haia and I’m a robot agent 🤖. Welcome to Carnival Resort🏨"]},"message":"text"},
      {"platform":"FACEBOOK","quickReplies":{"quickReplies":["😊Not Yet","Yeah😎"],"title":"Are you already a client?😎"},"message":""},
      {"platform":"SLACK","quickReplies":{"quickReplies":["test","ing","this"],"title":""},"message":"quickReplies"},
      {"platform":"twilio","text":{"text":["🙏🙏Hel’m Haia and I’m a robot agent 🤖. Welcome to Carnival Resort🏨"]},"message":"text"},
      {"platform":"twillo","quickReplies":{"quickReplies":["😊Not Yet","Yeah😎"],"title":"Are you already a client?😎"},"message":""},
           ] }))

        
                                 
    if action == "notyet":
           #if 'username'  request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "🙂Okay..!Follow the 3 more steps ..Enter Your Name Please ?"}))

    elif action == "uname":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
        
            return make_response(jsonify({'fulfillmentText': "👍Good..! "+not_yet+" Follow 2 more steps Enter Email Id Please ?"}))

    elif action == "errorresponse":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                        {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["💬Restart Chat","Contact Us"],"title":"Oops, sorry! I didn’t get it. 😥 Here’s what we’re going to do… Click on one of the buttons below to restart our conversation or contact us."},"message":""},
                        {"platform":"FACEBOOK","quickReplies":{"quickReplies":["💬Restart Chat","Contact Us"],"title":"Oops, sorry! I didn’t get it. 😥 Here’s what we’re going to do… Click on one of the buttons below to restart our conversation or contact us."},"message":""},                

            ]}))
    #Multicuisine 
    elif action == "multicuisine":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "🥳",
            "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["Jungle Theme Restaurant","Poolside Restaurants","Restro Bar"],"title":"Multi-Cuisine Restaurant"},"message":""},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["Jungle Theme Restaurant","Poolside Restaurants","Restro Bar"],"title":"Multi-Cuisine Restaurant"},"message":""},
                
                ]}))
    #Multicuisine 
    elif action == "weedingsmeetings":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "🥳",
            "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["Board Room","AC Conference Hall","Air-Cooled Banquet Hall","Party Lawn","Multi Purpose Hall","AC Luxurious Hall","Non-AC Party Hall","Mini Party Lawn"],"title":"Weddings & Meetings"},"message":""},
                 {"platform":"FACEBOOK","quickReplies":{"quickReplies":["Board Room","AC Conference Hall","Air-Cooled Banquet Hall","Party Lawn","Multi Purpose Hall","AC Luxurious Hall","Non-AC Party Hall","Mini Party Lawn"],"title":"Weddings & Meetings"},"message":""},

                ]}))
        
    elif action == "uemail":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "👌🏻Nice..!Follow wwwwwww1 more step Enter Your Mobile Number?"}))
        
    elif action == "uphone":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "🥳Awesome😎Thanks To Connect With Us",
            "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["🥳Awesome😎Thanks To Connect With Us"]},"message":"text"},
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["🏡Room Booking","Multi-Cuisine Restaurants","Weddings & Meetings","🎁Offers","⚙24*7 Support"],"title":"Select Anyone😎"},"message":""},
                  {"platform":"FACEBOOK","text":{"text":["🥳Awesome Thanks To Connect With Us😎"]},"message":"text"},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["🏡Room Booking","Multi-Cuisine Restaurants","Weddings & Meetings","🎁Offers","⚙24*7 Support"],"title":"Select Anyone😎"},"message":""},
    
                ]
            }))

    elif action == "yeah":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "Awesome😎Thanks To Connect With Us",
            "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["🥳Awesome😎Thanks To Connect With Us"]},"message":"text"},
                 # {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Carnival Resort","subtitle": "Marathi Tadaka","imageUri": "http://www.carnivalresort.in/assets/img/slider/1.jpg",
                     #   }},
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["🏡Room Booking","🍽Multi-Cuisine Restaurants","💍Weddings & 🤝Meetings","🎁Offers","⚙24*7 Support"],"title":"Select Anyone😎"},"message":""},
                  {"platform":"FACEBOOK","text":{"text":["🥳Awesome Thanks To Connect With Us😎"]},"message":"text"},
                 # {"platform":"FACEBOOK","card": { "title": "Carnival Resort","subtitle": "Marathi Tadaka","imageUri": "http://www.carnivalresort.in/assets/img/slider/1.jpg",
                 #       }},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["🏡Room Booking","🍽Multi-Cuisine Restaurants","💍Weddings & 🤝Meetings","🎁Offers","⚙24*7 Support"],"title":"Select Anyone😎"},"message":""},

                ]
            }))

    elif action == "roombooking":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["🏡Reception Rooms","🏡Deluxe Rooms","🏡Super Deluxe Rooms","🏡Executive Rooms"],"title":"Luxurious Rooms😎"},"message":""},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["🏡Reception Rooms","🏡Deluxe Rooms","🏡Super Deluxe Rooms","🏡Executive Rooms"],"title":"Luxurious Rooms😎"},"message":""},
                ]
            }))
    elif action == "reception":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    elif action == "contactus":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Carnival Resort Bot","subtitle":"+91 7710881086",
                                                             "imageUri":"http://www.carnivalresort.in/assets/img/slider/1.jpg",
                                                               "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/contact"
                                                                     }
        ]}},
               {"platform":"FACEBOOK","card": { "title": "Carnival Resort Bot","subtitle":"+91 7710881086",
                                                             "imageUri":"http://www.carnivalresort.in/assets/img/slider/1.jpg",
                                                               "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/contact"
                                                                     }
        ]}},
            ]
            }))



    elif action == "BoardRoom":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "BoardRoom","subtitle":"Capacity 14 people Air Conditioned Includes 42 LCD TV",
                                                             "imageUri":"http://www.carnivalresort.in/assets/img/services/chamber1.jpg",
                                                               "buttons": [
                                                                      {  "text": "click here for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
                {"platform":"FACEBOOK","card": { "title": "BoardRoom","subtitle":"Capacity 14 people Air Conditioned Includes 42 LCD TV","imageUri":"http://www.carnivalresort.in/assets/img/services/chamber1.jpg"}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))

    elif action == "Weeding_Meetings.Weeding_Meetings-ACConferenceHal":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                 {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "AC Conference Hall","subtitle":"1.Capacity 150 people 2.Air Conditioned Acoustically Treated 3.Includes Projector, Screen, White Board, Mic & Sounddea for Conferences 4. DJ Parties",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/senate1.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
                 {"platform":"FACEBOOK","card": { "title": "AC Conference Hall","subtitle":"1.Capacity 150 people 2.Air Conditioned Acoustically Treated 3.Includes Projector, Screen, White Board, Mic & Sounddea for Conferences 4. DJ Parties","imageUri":"http://www.carnivalresort.in/assets/img/services/senate1.jpg",
                                                  "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))

    elif action == "Weeding_Meetings.Weeding_Meetings-Air-CooledBanquetHall":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Air-Cooled Banquet Hall","subtitle":"1.Capacity 700 2.Air Cooled & Beautiful Interiors In built stage & sound system 3.Ideal for Engagements & Birthdays","imageUri":"http://www.carnivalresort.in/assets/img/services/heaven2.jpg",
                                                             "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
                {"platform":"FACEBOOK","card": { "title": "Air-Cooled Banquet Hall","subtitle":"1.Capacity 700 2.Air Cooled & Beautiful Interiors In built stage & sound system 3.Ideal for Engagements & Birthdays","imageUri":"http://www.carnivalresort.in/assets/img/services/heaven2.jpg",
                                                 "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    elif action == "Weeding_Meetings.Weeding_Meetings-PartyLawn":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Moon Light - The Party Lawn","subtitle":"1.Capacity 1500 people 2.Beautiful Landscape 3.Huge Stage with 2 rooms attached 4.Ideal for Weddings and Events in evening","imageUri":"http://www.carnivalresort.in/assets/img/services/moonlight1.jpg",
                                                             "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
                {"platform":"FACEBOOK","card": { "title": "Moon Light - The Party Lawn","subtitle":"1.Capacity 1500 people 2.Beautiful Landscape 3.Huge Stage with 2 rooms attached 4.Ideal for Weddings and Events in evening","imageUri":"http://www.carnivalresort.in/assets/img/services/moonlight1.jpg",
                                                 "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    elif action == "Weeding_Meetings.Weeding_Meetings-MultiPurposeHall":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "","subtitle":"1.Capacity 1500 people 2.Covered from top, open from sides3. Surrounded by greenery 4.A unique alternative to lawns in monsoon 5.Ideal for Weddings & Events in daytime","imageUri":"http://www.carnivalresort.in/assets/img/services/whitehouse1.jpg","buttons": [
                                                                      {  "text": "click here for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
                {"platform":"FACEBOOK","card": { "title": "The MultiPurpose Hall","subtitle":"1.Capacity 1500 people 2.Covered from top, open from sides3. Surrounded by greenery 4.A unique alternative to lawns in monsoon 5.Ideal for Weddings & Events in daytime","imageUri":"http://www.carnivalresort.in/assets/img/services/whitehouse1.jpg","buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    

    elif action == "multi_cuisine_rest.multi_cuisine_rest-jungletheme":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                 {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "The Jungle Book - Jungle Theme Restaurant","subtitle":"1.Latur's first forest themed Restaurant 2.Jungle Book themed PhotoBooth with a huge aquarium & Non-Veg Cuisinesal for families & kids","imageUri":"http://www.carnivalresort.in/assets/img/services/white-chilly4.jpg","buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/restaurant.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

                 {"platform":"FACEBOOK","card": { "title": "The Jungle Book - Jungle Theme Restaurant","subtitle":"1.Latur's first forest themed Restaurant 2.Jungle Book themed PhotoBooth with a huge aquarium & Non-Veg Cuisinesal for families & kids","imageUri":"http://www.carnivalresort.in/assets/img/services/white-chilly4.jpg","buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/restaurant.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    elif action == "multi_cuisine_rest.multi_cuisine_rest-poolside":
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                 {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Blue Lagoon - Poolside Restaurant","subtitle":"1.Serene Poolside setting Fresh Air 2. Veg & Non-Veg Cuisi 3.Ideal for families & couples","imageUri":"http://www.carnivalresort.in/assets/img/services/blue-lagoon1.jpg","buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/restaurant.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

                 {"platform":"FACEBOOK","card": { "title": "Blue Lagoon - Poolside Restaurant","subtitle":"1.Serene Poolside setting Fresh Air 2.Veg & Non-Veg Cuisi 3.Ideal for families & couples","imageUri":"http://www.carnivalresort.in/assets/img/services/blue-lagoon1.jpg",
                                                  "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/restaurant.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))

    elif action == "multi_cuisine_rest.multi_cuisine_rest-retrobar":
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                 {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Blue Lagoon - Poolside Restaurant","subtitle":"1.Bamboo themed Bar & Restaurant 2.Wide Range of Liquor & Cocktails 3.Veg & Non-Veg Cuisines 4.Ideal for friends & couples","imageUri":"http://www.carnivalresort.in/assets/img/services/Chill3.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/restaurant.php"
                                                                     }
        ]}},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

                {"platform":"FACEBOOK","card": { "title": "Blue Lagoon - Poolside Restaurant","subtitle":"1.Bamboo themed Bar & Restaurant 2.Wide Range of Liquor & Cocktails 3.Veg & Non-Veg Cuisines 4.Ideal for friends & couples","imageUri":"http://www.carnivalresort.in/assets/img/services/Chill3.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/restaurant.php"
                                                                     }
        ]}},
                {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
        #weddings & meetings
    elif action == "Weeding_Meetings.Weeding_Meetings-ACLuxuriousHall":
   
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
            {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Golden Leaf - The AC Luxurious Hall","subtitle":"1.Capacity 200 people 2.Most Luxurious Hall In Latur 3.JBL Sound System 4. Ideal For Grand Celebration",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/achall.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                         }
        ]}},
            {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
            {"platform":"FACEBOOK","card": { "title": "Golden Leaf - The AC Luxurious Hall","subtitle":"1.Capacity 200 people 2.Most Luxurious Hall In Latur 3.JBL Sound System 4. Ideal For Grand Celebration",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/achall.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                         }
        ]}},
                
            {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))

    elif action == "Weeding_Meetings.Weeding_Meetings-Non-ACPartyHall":
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
               {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Silver Star - The Non-AC Party Hall","subtitle":"1.Capacity 200 people 2.Ideal for Birthdays & Small gathering",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/lounge1.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                         }
        ]}},
            {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
            {"platform":"FACEBOOK","card": { "title": "Silver Star - The Non-AC Party Hall","subtitle":"1.Capacity 200 people 2.Ideal for Birthdays & Small gathering",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/lounge1.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                         }
        ]}},
                
            {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    elif action == "Weeding_Meetings.Weeding_Meetings-MiniPartyLawn":
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
               {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Food Court - The Mini Party Lawn","subtitle":"1.Capacity 100 people 2.Ideal for Birthdays & Small gathering",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/foodcourt2.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                         }
        ]}},
            {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},
            {"platform":"FACEBOOK","card": { "title": "Food Court - The Mini Party Lawn","subtitle":"1.Capacity 100 people 2.Ideal for Birthdays & Small gathering",
                                                              "imageUri":"http://www.carnivalresort.in/assets/img/services/foodcourt2.jpg",
                                                              "buttons": [
                                                                      {  "text": "click here👉 for more info",
                                                                         "postback": "http://www.carnivalresort.in/wedding-meeting.php"
                                                                         }
        ]}},
                
            {"platform":"FACEBOOK","text":{"text":["Awesome😎Let's sum up..when would you like to ✅ check in.."]},"message":"text"},

            ]
            }))
    
    elif action == "checkin":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Cool..😎 how many adults? 👨🏻‍🦳👩🏻‍🦳 (ex. 2 adults) ?"]},"message":"text"},
                {"platform":"FACEBOOK","text":{"text":["Cool..😎 how many adults? 👨🏻‍🦳👩🏻‍🦳 (ex. 2 adults) ?"]},"message":"text"},

            ]
            }))

    elif action == "adults":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["👂🏻Sounds Good.. date ⏰ for Check Out ? ✈️"]},"message":"text"},
                {"platform":"FACEBOOK","text":{"text":["👂🏻Sounds Good.. date ⏰ for Check Out ? ✈️"]},"message":"text"},

            ]
            })) 

    elif action == "checkout":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["👍Yes","No👎",],"title":"Is it 👍 ok for you?🙂"},"message":""},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["👍Yes","No👎",],"title":"Is it 👍 ok for you?🙂"},"message":""},

            ]
            }))

    elif action == "checkout.checkout-yes":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
            "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["Searching for available rooms.."]},"message":"text"},
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["🥳🥳I found 2 rooms🎉🥳"]},"message":"text"},
                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Reception Room ","subtitle": "from 228.22 EUR/Night",
                                                             "imageUri": "http://www.carnivalresort.in/assets/img/rooms/thumb/rec.jpg"}},
                {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["Book Now🔖"],"title":"1500?😎"},"message":""},

                {"platform":"PLATFORM_UNSPECIFIED","card": { "title": "Reception Room ","subtitle": "from 228.22 EUR/Night",
                                                             "imageUri": "http://www.carnivalresort.in/assets/img/rooms/thumb/rec.jpg"}},
                {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["Book Now🔖"],"title":"1200?😎"},"message":""},

                {"platform":"FACEBOOK","text":{"text":["Searching for available rooms.."]},"message":"text"},

                {"platform":"FACEBOOK","text":{"text":["I found 2 rooms🎉🥳"]},"message":"text"},
                {"platform":"FACEBOOK","card": { "title": "Reception Room ","subtitle": "from 1100 Rupees/Night",
                                                             "imageUri": "http://www.carnivalresort.in/assets/img/rooms/thumb/rec.jpg"}},
                {"platform":"FACEBOOK","quickReplies":{"quickReplies":["Book Now🔖"],"title":"1500?😎"},"message":""},

                {"platform":"FACEBOOK","card": { "title": "Reception Room ","subtitle": "from 800 Rupees EUR/Night",
                                                             "imageUri": "http://www.carnivalresort.in/assets/img/rooms/thumb/rec.jpg"}},
                {"platform":"FACEBOOK","quickReplies":{"quickReplies":["Book Now🔖"],"title":"1200?😎"},"message":""},
            ]
            }))
    elif action == "checkout.checkout-no":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
             "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["🏡Reception Rooms","🏡Deluxe Rooms","🏡Super Deluxe Rooms","🏡Executive Rooms"],"title":"Luxurious Rooms😎"},"message":""},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["🏡Reception Rooms","🏡Deluxe Rooms","🏡Super Deluxe Rooms","🏡Executive Rooms"],"title":"Luxurious Rooms😎"},"message":""},
                ]
            }))

    elif action == "booknow1":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
             "fulfillmentMessages":[
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["💸By Cash","💳Online"],"title":"Payment By"},"message":""},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["💸By Cash","💳Online Payment"],"title":"Payment By"},"message":""},
                ]
            }))

    elif action == "paybycash":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
             "fulfillmentMessages":[
                {"platform":"FACEBOOK","text":{"text":["Visit Us🏨 details sent on your mobile📱"]},"message":"text"},
                  {"platform":"PLATFORM_UNSPECIFIED","quickReplies":{"quickReplies":["No..Thank you.!","🏡Room Booking","🍽Multi-Cuisine Restaurants","💍Weddings & 🤝Meetings","🎁Offers","⚙24*7 Support"],"title":"Do you need any further help or support😎"},"message":""},
                  {"platform":"FACEBOOK","quickReplies":{"quickReplies":["No..Thank you.!","🏡Room Booking","🍽Multi-Cuisine Restaurants","💍Weddings & 🤝Meetings","🎁Offers","⚙24*7 Support"],"title":"Do you need any further help or support😎"},"message":""},
            
                ]}))

    elif action == "thankyou":
           #if 'username' in request.args:
            #return 'Hello ' + request.args['name']
            return make_response(jsonify({'fulfillmentText': "",
             "fulfillmentMessages":[
                {"platform":"PLATFORM_UNSPECIFIED","text":{"text":["🙏Thanks For Visiting Us..We will get back to you..!🙏🙏🙂"]},"message":"text"},
                {"platform":"FACEBOOK","text":{"text":["🙏Thanks For Visiting Us..We will get back to you..!🙏🙏🙂"]},"message":"text"},
                ]
            }))
        
@app.route("/") 
def home_view(): 
		return "<h1>Welcome 2 Imran Server</h1>"
