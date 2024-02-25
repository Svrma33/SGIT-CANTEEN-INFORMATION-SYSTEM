import pickle


Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday = 0,1,2,3,4,5,6

outlet = {'Mac Donald':['assets/mcdonald.png','assets/Macs_Menu.png'],
          'Malay Stall':['assets/malaybbq.png','assets/MBBQ_Menu.png'],
          'Beverages Stall':['assets/drinks.png','assets/Beverages_Menu.png'],
          'KFC':['assets/kfc.png','assets/KFC_Menu.png'],
          'Yong Tau Foo Stall':['assets/ytfoo.png','assets/YTF_Menu.png']
          }

main_database = {'Mac Donald':{'Lunch': {'Title': 'Mac Donald Lunch/Dinner',
                                         'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (1100,2400),
                                                             (Saturday,):(1200,2400),
                                                             (Sunday,):(1200,2200)
                                                            },
                                         'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
                                                  ('♣ Filet O Fish: ₹329',
                                                   '♣ McChicken: ₹329',
                                                   '♣ Vanilla Cone: ₹67',
                                                   '♣ Chicken Nuggets - 6pc: ₹384\n',),
                                                },
                                         'Hours': 'Opening Hours\nMonday - Sunday : 7am to 12 midnight\n\nAfter Hours\nMonday - Friday: 11am to 12 midnight\nSaturday: 11am to 12 midnight\n\nBreakfast Hours\nMonday - Friday: 7am to 11am\nSaturday: 7am to 12pm\nSunday: 10am to 12pm',
                                         'Queue': 2,
                                         'Location': 'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                         'Review': 'assets/Mac_Review.txt'},
                               
                               'Breakfast':{'Title': 'Mac Donald Breakfast',
                                            'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday,): (700,1100),
                                                                (Saturday,):(700,1200),
                                                                (Sunday,):(1000,1200)
                                                               },
                                            'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
                                                     ('♣ Big Breakfast: ₹580',
                                                      '♣ Hotcakes: ₹496',
                                                      '♣ Breakfast Wrap Chicken: ₹400',
                                                      '♣ Hotcakes: ₹384\n',),
                                                    },
                                           'Hours': 'Opening Hours\nMonday - Sunday : 7am to 12 midnight\n\nBreakfast Hours\nMonday - Friday: 7am to 11am\nSaturday: 7am to 12pm\nSunday: 10am to 12pm\n\nAfter Hours\nMonday - Friday: 11am to 12 midnight\nSaturday: 11am to 12 midnight',
                                           'Queue': 2,
                                           'Location': 'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                           'Review': 'assets/Mac_Review.txt',}
                               },
                 
                 'Malay Stall':{'Malay Stall':{'Title': 'Malay BBQ Stall',
                                               'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (830,2130),
                                                                    (Saturday,): (830,1700)
                                                                   },
                                               'Menu': {
                                                 (Monday,): ['Monday\'s Menu',
                                                             '♣ Mee rebus : ₹300',
                                                             '♣ Mee Soto: ₹329',
                                                             '♣ Chicken Rice: ₹317',
                                                             '♣ Fried Rice Seafood: ₹384',
                                                             '*special dish'],
                                                (Tuesday,): ['Tuesday\'s Menu',
                                                             '♣ Mee Soto: ₹329',
                                                             '♣ Chicken Rice: ₹317',
                                                             '♣ Mee rebus : ₹300',
                                                             '♣ Nasi kerabu: ₹467',
                                                             '♣ Fried Rice Seafood: ₹384',
                                                             '*special dish'],
                                               (Wednesday,):['Wednesday\'s Menu',
                                                             '♣ Mee Soto: ₹329',
                                                             '♣ Chicken Rice: ₹317',
                                                             '♣ Fried Rice Seafood: ₹384'],
                                                (Thursday,):['Thursday\'s Menu',
                                                             '♣ Nasi Briyani: ₹384',
                                                             '♣ Mee Soto: ₹329',
                                                             '♣ Chicken Rice: ₹317',
                                                             '♣ Fried Rice Seafood: ₹384',
                                                             '*special dish'],
                                                 (Friday,): ['Friday\'s Menu',
                                                             '♣ Mee Soto: ₹329',
                                                             '♣ Mee rebus : ₹300',
                                                             '♣ Chicken Rice: ₹317',
                                                             '♣ Fried Rice Seafood: ₹384',
                                                             '♣ Laksa: ₹384',
                                                             '*special dish'],
                                               (Saturday,): ['Saturday\'s Menu',
                                                             '♣ Mee Soto: ₹329',
                                                             '♣ Nasi Ayam Penyet: ₹384',
                                                             '♣ Chicken Rice: ₹317',
                                                             '♣ Nasi kerabu: ₹467',
                                                             '♣ Fried Rice Seafood: ₹384',
                                                             '*special dish'],
                                                    },
                                              'Hours': 'Opening Hours\nMonday - Friday: 8:30am to 9:30pm\nSaturday: 8:30am to 5pm\nSunday: Closed',
                                              'Queue': 3,
                                              'Location': 'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                              'Review': 'assets/MBBQ_Review.txt'}
                                },
                 
                'Beverages Stall':{'Beverages Stall':{'Title': 'Beverages Stall',
                                                       'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (830,2130),
                                                                           (Saturday,): (830,1700),
                                                                          },
                                                        'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday):
                                                                 ('♣ Coffee: ₹58',
                                                                 '♣ Ice Milo: ₹83',
                                                                 '♣ Canned Drinks: ₹83',
                                                                 '♣ Banana Milkshake: ₹175'),
                                                                 },
                                                        'Hours': 'Opening Hours\nMonday - Friday: 8:30am to 9:30pm\nSaturday: 8:30am to 5pm\nSunday: Closed',
                                                        'Queue': 1,
                                                        'Location': 'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                                        'Review': 'assets/drinks_Review.txt'}
                                   },
                                   
                 'KFC':{'Lunch':{ 'Title': 'KFC Lunch/Dinner',
                                  'Operating Hours': {(Monday,Tuesday,Wednesday,Thursday,Friday): (1100,2200),
                                                      (Saturday,Sunday): (1100,2000)
                                                     },
                                  'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday):
                                           ('♣ Cheese Fries: ₹392',
                                            '♣ Original Recipe Chicken: ₹296',
                                            '♣ Whipped Potato (Medium): ₹284',
                                            '♣ Zinger: ₹442\n'),
                                          },
                                 'Hours': 'Opening Hours\nMonday - Sunday: 7:30am to 10pm\n\nAfter Hours\nMonday - Sunday: 11am to 10pm \n\nBreakfast Hours\nMonday - Friday: 7:30am to 11am',
                                 'Queue': 2,
                                 'Location':'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                 'Review': 'assets/KFC_Review.txt',
                                 },
                        'Breakfast':{'Title': 'KFC Breakfast',
                                    'Operating Hours': {
                                        (Monday,Tuesday,Wednesday,Thursday,Friday): (730,1100),
                                        },
                                    'Menu': {(Monday,Tuesday,Wednesday,Thursday,Friday):
                                             ('♣ Original Recipe Platter: ₹525',
                                              '♣ Original Recipe Porridge: ₹292',
                                              '♣ Original Recipe Twister: ₹375',
                                              '♣ Riser Burger: ₹342\n'),
                                             },
                                    'Hours': 'Opening Hours\nMonday - Sunday: 7:30am to 10pm\n\nBreakfast Hours\nMonday - Friday: 7:30am to 11am \nSaturday - Sunday: No Breakfast\n\nAfter Hours\nMonday - Sunday: 11am to 10pm ',
                                    'Queue': 2,
                                    'Location':'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                    'Review': 'assets/KFC_Review.txt'}
                                     },
                'Yong Tau Foo Stall':{'Yong Tau Foo Stall':{ 'Title': 'Yong Tau Foo Stall',
                                                            'Operating Hours': {
                                                                (Monday,Tuesday,Wednesday,Thursday,Friday): (830,2130),
                                                                (Saturday,): (830,1700),
                                                                },
                                                            'Menu': {
                                                                (Monday,): ['Monday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: ₹317',
                                                                            '♣ Noodle or Rice: ₹42',
                                                                            '♣ Spicy Soup Base: ₹50',
                                                                            '♣ Bak Chor Mee: ₹317',
                                                                            '*special dish'],
                                                                
                                                                (Tuesday,): ['Tuesday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: ₹317',
                                                                            '♣ Noodle or Rice: ₹42',
                                                                            '♣ Spicy Soup Base: ₹50',
                                                                            '♣ Fried Yee Mee: ₹484',
                                                                            '♣ Bak Chor Mee: ₹317',
                                                                            '*special dish'],
                                                                
                                                                (Wednesday,):['Wednesday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: ₹317',
                                                                            '♣ Noodle or Rice: ₹42',
                                                                            '♣ Spicy Soup Base: ₹50',
                                                                            '♣ Mamak Mee: ₹400',
                                                                            '*special dish'],
                                                                
                                                                (Thursday,): ['Thursday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: ₹317',
                                                                            '♣ Noodle or Rice: ₹42',
                                                                            '♣ Spicy Soup Base: ₹50',
                                                                            '♣ Cheong Fun: ₹375',
                                                                            '*special dish'],
                                                                
                                                                (Friday,): ['Friday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: ₹317',
                                                                            '♣ Noodle or Rice: ₹42',
                                                                            '♣ Spicy Soup Base: ₹50',
                                                                            '♣ Fish Ball Noodle: ₹525',
                                                                            '*special dish'],
                                                                
                                                                (Saturday,):['Saturday\'s Menu',
                                                                            '♣ 6 pc ingredients with rice or\nnoodle: ₹317',
                                                                            '♣ Noodle or Rice: ₹42',
                                                                            '♣ Spicy Soup Base: ₹50'],
                                                                     },
                                                            'Hours': 'Opening Hours\nMonday to Friday: 8:30am to 9:30pm \nSaturday: 8:30am to 5pm \nSunday: Closed',
                                                            'Queue': 3,
                                                            'Location': 'Sanskar Educational Group, Opp. Jindal Pipes ltd,\nNH-24, Jindal Nagar, Ghaziabad, Uttar Pradesh 201302',
                                                            'Review': 'assets/YTF_Review.txt',}
                                     },
                }

#---Pickle dump method to store our database---------
with open("Data.txt",'wb') as file:
    pickle.dump(outlet,file)
    pickle.dump(main_database,file)


#---Pickle load method to read the database that will be used in main.py---------
with open("Data.txt",'rb') as file:
    outlet = pickle.load(file)
    main_database = pickle.load(file)

