ratings = [
  4.4,
  4.5,
  3.8,
  3.8,
  3.75, 
  4.1,
  4.1,
  4.5,
  3.9,
  4.1,
  3.8,
  4.1,
  4.1,
  3.9,
  3.55,  
  4.0,
  3.55,  
  3.9,
  4.0,
  3.9,
  4.2,
  4.1,
  3.55,  
  4.0
]
print(len(ratings))

online_response = [
    
  [  # CMF by Nothing Phone 2 Pro (White, 128 GB)
    "Loving the clean Android experience and the unique Glyph lights! The camera takes great photos in daylight.",
    "Battery life is solid, lasts me the whole day with moderate usage. Fast charging is super convenient.",
    "The design really stands out, I always get asked about it. Performance is smooth for everyday apps.",
    "The screen is bright and clear, great for watching videos. Haptics feel premium for the price.",
    "Sometimes the Glyph interface can be a bit gimmicky, but overall I really enjoy this phone."
  ],
  [  # Nothing Phone (3a) (Blue, 256 GB)
    "The transparent back is so cool! It definitely turns heads. Performance is good for the price.",
    "Camera is decent for social media, especially in good lighting. Battery life is okay, could be better.",
    "The software is very close to stock Android, which I appreciate. No unnecessary bloatware.",
    "Feels comfortable in the hand. The display is nice and vibrant for the price range.",
    "The Glyph interface is fun and customizable, adds a unique touch to notifications."
  ],
  [  # REDMI A3X (Olive Green, 64 GB)
    "Great budget phone for basic use. Calls and messaging work perfectly. Battery lasts a long time.",
    "Simple and easy to use interface, good for someone who doesn't need a lot of fancy features.",
    "The screen is decent for the price. It's a good value for money as a secondary phone.",
    "Build quality feels okay for a budget device. Not the fastest, but gets the job done for basic tasks.",
    "Camera is acceptable for quick snaps in good light."
  ],
  [  # REDMI A3X (Ocean Green, 64 GB)
    "Same as the Olive Green one, it's a reliable and affordable option for everyday tasks.",
    "Battery life is a major plus, I don't have to worry about charging it constantly.",
    "Good for calls, texts, and light browsing. Don't expect high-end performance for gaming.",
    "The color is nice. It's a straightforward phone without too many frills.",
    "A solid choice if you need a basic smartphone without spending a lot."
  ],
  [  # Nothing Phone (3a) Pro (Grey, 256 GB)
    "The 'Pro' version feels more premium. The camera is definitely better, takes sharper photos.",
    "Performance is noticeably smoother, especially with multitasking. More RAM makes a difference.",
    "Still love the Glyph interface, and it seems even more refined on this model.",
    "Battery life is improved compared to the standard (3a). Fast charging is still great.",
    "The design is still unique and eye-catching. A good upgrade if you liked the original."
  ],
  [  # Motorola g45 5G (Brilliant Blue, 128 GB)
    "The 120Hz display is smooth for scrolling and gaming. 5G connectivity is a plus for future-proofing.",
    "Camera takes decent photos in good lighting, the ultrawide lens is handy. Battery lasts a full day.",
    "Feels well-built for the price. Performance is adequate for daily tasks and some casual gaming.",
    "Clean Android experience without too much bloatware is a big plus. Updates are fairly regular.",
    "Good value for money if you're looking for a 5G phone with a smooth display."
  ],
  [  # SAMSUNG Galaxy F05 (Twilight Blue, 64 GB)
    "Reliable Samsung phone for basic use. Battery life is excellent, lasts me well over a day.",
    "Simple and easy to navigate interface. Good for people who prefer a familiar Android experience.",
    "The screen is decent for everyday viewing. Call quality is clear.",
    "Build quality is typical for a Samsung budget phone, feels sturdy enough.",
    "Camera is okay for basic snaps, nothing too impressive but gets the job done."
  ],
  [  # vivo T4x 5G (Pronto Purple, 128 GB)
    "Fast charging is a game-changer, the phone charges up really quickly. Performance is smooth for daily use.",
    "The display is vibrant and sharp, good for watching videos and browsing social media.",
    "Camera takes good photos in daylight, portrait mode works well. Design is also quite stylish.",
    "Battery life is decent, easily lasts a full day with moderate usage.",
    "Good overall package with a focus on charging speed and display quality."
  ],
  [  # MOTOROLA g05 (Forest Green, 64 GB)
    "Clean Android experience with no bloatware. Easy to use and navigate.",
    "Battery life is very good, lasts a long time on a single charge. Reliable for everyday tasks.",
    "Decent performance for basic apps and calls. Good value for a budget smartphone.",
    "Feels comfortable to hold. The screen is adequate for general use.",
    "A solid, no-frills phone for those who prioritize simplicity and battery life."
  ],
  [  # MOTOROLA g35 5G (Guava Red, 128 GB)
    "5G connectivity at an affordable price. Battery life is good, lasts through the day.",
    "Decent performance for everyday tasks and light gaming. The display is okay for the price.",
    "Clean Android experience is a plus. Camera is acceptable for casual photos.",
    "Feels reasonably well-built. A good option if you want 5G on a budget.",
    "The color is nice and stands out. Overall a decent value proposition."
  ],
  [  # REDMI A3X (Midnight Black, 64 GB)
    "Basic but reliable smartphone for essential tasks. Good battery life.",
    "Simple interface, easy for anyone to use. Affordable price point.",
    "Decent screen for basic viewing. Call quality is good.",
    "Build quality is acceptable for the price. Does what it needs to without being fancy.",
    "A good option for first-time smartphone users or as a secondary device."
  ],
  [  # SAMSUNG Galaxy M35 5G (Moonlight Blue, 128 GB)
    "Large battery ensures all-day usage. Smooth performance for everyday apps and multitasking.",
    "Vibrant and immersive display, great for media consumption. Good camera for the price segment.",
    "Typical Samsung build quality, feels solid. Feature-rich with the Samsung ecosystem.",
    "5G connectivity for faster speeds. A well-rounded mid-range smartphone.",
    "Offers a good balance of features, performance, and battery life."
  ],
  [  # MOTOROLA g35 5G (Leaf Green, 128 GB)
    "Affordable 5G phone with a decent battery. Smooth enough for daily use.",
    "Clean Android software is a highlight. Acceptable camera for the price.",
    "Feels comfortable in the hand. The display is adequate for everyday viewing.",
    "Good value if you're looking for 5G on a budget without too many extras.",
    "The green color is nice. A practical and functional smartphone."
  ],
  [  # Motorola g45 5G (Pink Lavender, 128 GB)
    "Smooth 120Hz display makes scrolling and animations feel fluid. 5G ready.",
    "Capable camera system for capturing everyday moments. Battery life is reliable.",
    "Decent performance for multitasking and light gaming. Clean Android experience.",
    "Feels well-made for its price point. A good all-around 5G smartphone.",
    "The pink lavender color is attractive. Offers a good balance of features and price."
  ],
  [  # REDMI A5 (Just Black, 64 GB)
    "Ultra-budget phone for basic calling and texting. Long-lasting battery.",
    "Very simple and easy to use, ideal for those who don't need advanced features.",
    "Decent enough screen for basic viewing. A very affordable option.",
    "Lightweight and easy to carry. Does the essentials without any frills.",
    "A good choice if you need a very inexpensive smartphone for basic communication."
  ],
  [  # POCO C71 (Desert Gold, 64 GB)
    "Entry-level smartphone for first-time users. Affordable and easy to handle.",
    "Battery life is decent for basic usage. Simple and straightforward interface.",
    "Acceptable performance for calls, messages, and light browsing.",
    "Lightweight design. A good starting point for smartphone use.",
    "Offers basic smartphone functionality at a very competitive price."
  ],
  [  # REDMI A5 (Pondicherry Blue, 64 GB)
    "Another very affordable option for basic smartphone needs. Good battery life.",
    "Simple to operate, suitable for those who aren't tech-savvy. Compact design.",
    "Adequate screen for basic tasks. A budget-friendly way to stay connected.",
    "Lightweight and easy to carry around. Does the job for essential functions.",
    "A solid choice if you need a very inexpensive and simple smartphone."
  ],
  [  # POCO C75 5G (Enchanted Green, 64 GB)
    "Budget-friendly 5G smartphone. Aims to provide fast connectivity at a low cost.",
    "Decent battery life for everyday use. Basic performance for essential tasks.",
    "The display is adequate for general viewing. Offers 5G without breaking the bank.",
    "Simple and functional design. A good option for those wanting 5G on a tight budget.",
    "Likely focuses on providing 5G access and decent battery life."
  ],
  [  # REDMI 13 5G (Orchid Pink, 128 GB)
    "Affordable 5G smartphone with a decent amount of storage. Good battery life.",
    "Reasonable performance for everyday tasks and some light gaming.",
    "The display is adequate for media consumption. Offers 5G at an accessible price.",
    "Stylish design with the orchid pink color. A good value proposition for a 5G phone.",
    "Likely balances features, performance, and price in the budget 5G segment."
  ],
  [  # POCO C75 5G (Aqua Bliss, 64 GB)
    "Another affordable 5G option from POCO. Focuses on providing fast connectivity.",
    "Decent battery life for daily usage. Basic performance for essential apps.",
    "The display is suitable for general use. A budget-friendly way to experience 5G.",
    "Simple and functional design. Targets users looking for affordable 5G.",
    "Likely emphasizes 5G capabilities and battery life at its price point."
  ],
  [  # Motorola Edge 50 Fusion (Marshmallow Blue, 128 GB)
    "Premium mid-range phone with a beautiful display. Excellent camera performance.",
    "Smooth and fast performance for multitasking and gaming. Long-lasting battery with fast charging.",
    "Stylish and sleek design. Clean Android experience with useful Motorola additions.",
    "Great for media consumption and photography enthusiasts. A well-rounded device.",
    "Offers a flagship-like experience without the top-tier price tag."
  ],
  [  # MOTOROLA g35 5G (Midnight Black, 128 GB)
    "Affordable 5G smartphone with a reliable battery. Decent performance for everyday tasks.",
    "Clean and user-friendly Android interface. Acceptable camera for the price.",
    "Comfortable to hold and use. A good option for those wanting 5G on a budget.",
    "Provides a solid and dependable smartphone experience without unnecessary extras.",
    "Good value for money if 5G connectivity is a priority."
  ],
  [  # REDMI A5 (Jaisalmer Gold, 64 GB)
    "Very basic and affordable smartphone for essential functions. Long battery life.",
    "Simple to use interface, ideal for those with minimal smartphone needs.",
    "Decent screen for basic viewing. A very budget-friendly option.",
    "Lightweight and easy to handle. Does the fundamental tasks adequately.",
    "A good choice for a very inexpensive and straightforward smartphone."
  ],
  [  # Infinix Note 50s 5G+ (Burgundy Red, 128 GB)
    "Budget-friendly 5G phone with a large display. Big battery for extended use.",
    "Decent performance for everyday tasks and media consumption. Good value for money.",
    "Stylish design with the burgundy red color. Aims to offer a lot of features at an affordable price.",
    "Likely focuses on providing a large screen and long battery life for entertainment.",
    "A competitive option in the budget 5G segment with a focus on multimedia."
  ]
]
people = [
    
  [  # CMF by Nothing Phone 2 Pro (White, 128 GB)
    "I bought it because of camera i saw in online but after purchase it seems different in quality not better than nothing 2a in camera. It seems its not 16mp front but 8 mp camera",

    "The incoming call voice had some disturbance even noise reduction on. Please tell me to correct",
    "Dnt go with paper spec, it is far superior. One of best all rounder phone under 20k",
    "Performance is not good",
    "speaker is very bad. Don't buy it."
  ],
  [  # Nothing Phone (3a) (Blue, 256 GB)
    "Best for value Nice performance.Audio quality also good Just required little more improvements",
    "he camera is awesome, UI is simple and clean",
    "Good phone, but software has lots of issues.Android Auto doesn't work with my Skoda Slavia And the screen flickered when I had bloomberg news app installed",
    "Worth for this budget for normal users",
    "Bettery is only six hour Phone hot soon N hang problem also"
  ],
  [  # REDMI A3X (Olive Green, 64 GB)
    "Cheap and best. Fine design.But sometimes it hang. However it is best at this price",
    "Over heat phone waste money don't purchase",
    "Average phone as per it's price.",
    "Not good phone",
    "Very bad, very hang from the starting."
  ],
  [  # REDMI A3X (Ocean Green, 64 GB)
    "Worth of money",
    "Too slow the processor is lacking too much",
    "Battary backup note good",
    "Very cool phone price range better phone.",
    "Good"
  ],
  [  # Nothing Phone (3a) Pro (Grey, 256 GB)
    "Very nice and beautiful phone",
    "Just buy it bro .. damn sure you will not regret. Love this phone.Go with the grey . It is better . It looks better.",
    "Good mobile no doubt",
    "Delivers sharp, detailed close up shot with excellent clarity .Bloatware free with smooth navigation and ai powered features for enhanced performance",
    "It takes 3 hour's to fully charge"
  ],
  [  # Motorola g45 5G (Brilliant Blue, 128 GB)
    "Good Phone, was searching for this colour in images to see how it looks in real, so posting it for someone who might be looking to buy in this colour",

    "Heating problem and charger is also not working",
    "Mobile is the very good all feature right only camera full zoom picture not good",
    "Very smooth and 120hz refresh rate smoother experience gaming is very super",
    "Product is not bad"
  ],
  [  # SAMSUNG Galaxy F05 (Twilight Blue, 64 GB)
    "Phone looks is very nice, but one thing Phone Charger is necessary, but nowadays Samsung is not provide a charger, its unfair.",

    "Not happy",
    "Processor is very slow",
    "Very bad product data usage very very bad",
    "Nice phone on budget. Good for senior citizens"
  ],
  [  # vivo T4x 5G (Pronto Purple, 128 GB)
    "Excellent Performance with good Battery Backup.Camera is Decent.",
    "Worth every penny. All in one smartphone. Recommended.",
    "Good",
    "Don't buy",
    "Not satisfied with the camera"
  ],
  [  # MOTOROLA g05 (Forest Green, 64 GB)
    "Mobile bad not working properly",
    "This mobile is very good mobile Display very clean",
    "Very good nice. I liked.These are very good phones for the money. We really liked them .",
    "I newly opened this phone and i was checking the phone the phone was lagging too much i didn't installed anything yet but it's too much lagging I m not satisfied by your product worst experience I have ever seen.",

    "Software not working and phone to much hanging"
  ],
  [  # MOTOROLA g35 5G (Guava Red, 128 GB)
    "The camera is good at this price range .Ram could be increased to 6gb atleast",
    "For the price excellent mobile and very very prompt delivery from Flipkart. Was delivered in six hours",
    "At this price range every thing is very good.Battery 🔋 not feels like 5000mh draining very fast but you know a long display and performance good enough.When I open the box it seems like I am not who open it first . Screen has many fingerprints and screen tape have many bubbles .And the end nice product by Motorola 👍😊",

    "Wifi network issue. Laggy ui.",
    "Waste phone 📱 hanging...not working best"
  ],
  [  # REDMI A3X (Midnight Black, 64 GB)
    "Nice phone I am very happy with phone",
    "Very bad, very hang from the starting",
    "The delivery boy was denying to open the box as it was the open box delivery. After that he started abusing and shouting worst experience not going to order anything from flipkart now. Please make sure customer satisfaction is the most important thing and this type of people make our experience worst.",

    "Average phone as per it's price.",
    "Average phone... good for aged people or as a secondary device."
  ],
  [  # SAMSUNG Galaxy M35 5G (Moonlight Blue, 128 GB)
    "This is perfect Phone is this segment 🔥🔥Best in camera",
    "Too good phone and bigg display ossm expressions I",
    "The camera quality is awesome😁 ...the display also awesome😄...the battery life is too awesome😃...but only one problem ..u can't do heavy games...😅All-rounder phone...📱",

    "Only heavy weight this is only one drawback ......all phone is awesome and excellent...camera, display, battery backup and performance is fantastic and very very awesome love you samsung",

    "Battery is Horrible It reduces damn fast, and even Camera is not that good."
  ],
  [  # MOTOROLA g35 5G (Leaf Green, 128 GB)
    "Awesome",
    "Budget friendly 5G phone with good configuration.",
    "Poor",
    "Very poor Quality too much heating like heater",
    "nice product"
  ],
  [  # Motorola g45 5G (Pink Lavender, 128 GB)
    "Good Phone, was searching for this colour in images to see how it looks in real, so posting it for someone who might be looking to buy in this colour",

    "BEST BUDGET 5G PHONE!",
    "Heating problem and charger is also not working",
    "Slow process I ansewer call after 1 minute",
    "Budget phone with all features and exclusive experience to use"
  ],
  [  # REDMI A5 (Just Black, 64 GB)
    "Please Camera improve",
    "Double touch screen on function no.power key ,back,manu,key alternative is better.",
    "Not cover not processing working slow",
    "Very nice product I am so happy",
    "Good"
  ],
  [  # POCO C71 (Desert Gold, 64 GB)
    "Camera is not good Display is blur little bit",
    "Comfortable for Family members",
    "Value for money 👍, also love the style of this phone 😍",
    "Don't bye this product he is very bad product please all Flipkart usares don't buy this product please",
    "Sound quality is bad and slow work this mobile"
  ],
  [  # REDMI A5 (Pondicherry Blue, 64 GB)
    "It's a budget friendly phone.",
    "Not cover not processing working slow",
    "Phone is getting heat",
    "Good price range",
    "Thise price range in The good all rounder smartphone."
  ],
  [  # POCO C75 5G (Enchanted Green, 64 GB)
    "No back case and only 10W charger is provided. In description they mentioned 18W charger in box and back case also. Good for Parents.",

    "Battery problem Camera problem",
    "It's budget phone",
    "Excellent in this budget",
    "Very delicate. Stopped working after 1 month."
  ],
  [  # REDMI 13 5G (Orchid Pink, 128 GB)
    "It is quite pleasant. Totally recommended",
    "he phone was good and butter smooth but the delivery experience by Ekart was too bad very bad service by Ekart",
    "Mobile is good and best for handling.",
    "Very Bad Product, Within a month The Speaker not working properly, i Can't hear the voice from other end without speaker mode.",

    "ery Bad Product, Within a month The Speaker not working properly, i Can't hear the voice from other end without speaker mode."

  ],
  [  # POCO C75 5G (Aqua Bliss, 64 GB)
    "Only Best 5G smartphone with enough budget,loved it to gift my grandmother",
    "Whether gaming or streaming, the display delivers every time. The refresh rate is smooth, and the colors pop beautifully. Its acutely great for an LCD display",

    "Good mobile according to price",
    "Go for it 😀",
    "What poco is offering for the price is just awesome.Decent camera, decent display decent everything in this phone.Price to quality is very very good"
  ],
  [  # Motorola Edge 50 Fusion (Marshmallow Blue, 128...
    "Really nice product.",
    "Front camera is below average",
    "Mobile has a technical problem as it gets hanged again and again......",
    "Worst phone don't buy, heating and low performance",
    "Camera could have been better, it AI puts extra light effect in every shoot. Official Gallery app, music app, app lock features are missing which is now a days are necessary features."

  ],
  [  # MOTOROLA g35 5G (Midnight Black, 128 GB)
    "Good mobile",
    "Poor",
    "Budget friendly 5G phone with good configuration.",
    "Battery drainage is to fast.",
    "Good product"
  ],
  [  # REDMI A5 (Jaisalmer Gold, 64 GB)
    "Like this phone Redmi A5",
    "It's a budget friendly phone.",
    "Sound and mike issue and heating problem",
    "Excellent work",
    "Phone is getting heat"
  ],
  [  # Infinix Note 50s 5G+ (Burgundy Red, 128 GB)
    "Power off on key. Volume key not good.... Very bad quality",
    "Poor photo (blurry and looks fake) and worst video recording from front camera in direct sunlight",
    "Budget phone is very superb phone",
    "Normal",
    "Phone power button not working very disappointed"
  ]
]
print(len(people))
print(len(online_response))
