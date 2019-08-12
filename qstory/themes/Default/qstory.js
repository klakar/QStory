// Initiate global variables
var story_title = [];
var story_content = [];
var story_location = [];
var story_zoom = [];
var current_page = 0;

// The QGIS plugin should create these lists and add them to the code here. (lists below are for tests and debugging only)

// First story page
story_title.push('#10 The Turquoise Coast, Turkey');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/TURKMAIN.jpg"><p><b>Why go now?</b> Rejoice in the revival! <br>If you Google “is Turkey safe”, you’ll get 1.5 billion answers. The real answer, of course, depends on where you want to visit. If it’s Turkey’s beautiful Turquoise Coast, the answer is definitely YES. The coastline is blessed with amazing beaches, fabulous landscapes, sensational food and brilliant hotels. Better still, it’s one of the cheapest summer destinations on the market. </p><p><b>Go with i-escape:</b> For beachside bliss on a budget, the lovely wooden cabins at Azur are surrounded by idyllic gardens, a pool, and stunning views. 4 Reasons is a Med-Zen chill-out hotel near Bodrum, with a lively bistro bar. For groups or families, try the 2 superb villas at Mandarin & Mango in the wilds of seaside Faralya.</p>');
story_location.push([30,38]);
story_zoom.push(8);

// Second story page
story_title.push('#9 Austria');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/AUSTRIAmain.jpg"> <p><b>Why go now?</b> The hills are alive…</p><p>Amazingly, Austria remains Europe’s best-kept secret. Hemmed in by jolly Germany and fancy Italy, you’d think the Austrians would be fed-up of their noisy neighbours, but not a chance. For they have secret wonders – 2 staggeringly beautiful cities, a culture that encourages genius (Mozart, Freud, Wittgenstein) and Europe’s most breathtaking Alpine wonderland. Go now.</p><p><b>Go with i-escape:</b> Our favourite new place in Salzburg is the stylish Hotel & Villa Auersperg close to the historic centre. In the heart of Vienna, try the ultra-spacious rooms of The Guesthouse. For Alpine splendour, you can’t beat the great value of Haus Hirt – voted ‘Best European Hotel 2018’ by our guests.</p>');
story_location.push([16.5,48]);
story_zoom.push(11);

// Third story page
story_title.push('#8 Alternative Morocco');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/MOROC.jpg"><p><b>Why go now?</b> Magic awaits beyond Marrakech.</p><p>The whole world fell in love with Morocco over the last decade, with special attention lavished on Marrakech. This year, the real Morocco is being re-discovered. Explore the untouched stretches of the Atlas Mountains, the boho surfing towns on the Atlantic coast, or the secluded sands of the Sahara Desert. Feed your wanderlust.</p><p><b>Go with i-escape:</b> In the High Atlas, the colourful Douar Samra guesthouse promises the most extraordinary arrival of your life. In Essaouira, the astonishing Salut Maroc is a must, as is the fabled Baoussala. For a truly unique experience, venture into the Sahara Desert and sleep below the stars at Camp Adounia.</p>');
story_location.push([-4,32.4]);
story_zoom.push(8);

// Story page
story_title.push('#7  Normandy, France');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/NORM1.jpg"><p><b>Why go now?</b> Discover a land of fairytales.</p><p>On 6 June, Normandy dominated the world’s media. The date marked the 75th anniversary of the D-Day landings, and the famous beaches witnessed a procession of world leaders paying their respects to those who fought, and died, in this decisive allied operation. Yet beyond Omaha and Juno, a quieter Normandy awaits. This is the Normandy of fairytale chateaus, dreamy meadows, fantasy coastlines and Monet’s magical garden. And don’t forget the heavenly cheese and cider!</p><p><b>Go with i-escape:</b> Families will adore the new Manoir de Surville set in peaceful farmlands. Kids will also love the vast grounds of 19th-century chateau Le Castel. Couples should try the romantic gite La Vie de Cocagne or the elegant country retreat La Louviere in southern Normandy (the food is delish).    </p>');
story_location.push([-0.2,49.4]);
story_zoom.push(10);

// Story page
story_title.push('#6  Oaxaca, Mexico');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/NEW123.jpg"><p><b>Why go now?</b> Mexico’s next big thing.</p><p>With better transport links and a generational shift in travellers wanting local culture, Mexico is witnessing a revolution. You can feel the buzz in its vibrant creative capital, Oaxaca – the birthplace of mezcal. The city and surrounding countryside offer truly authentic experiences: outrageous fiestas, fabulous street food, stunning colonial architecture and the jaw-dropping Monte Alban pyramid complex, now a World Heritage site. See it before the crowds arrive.</p><p><b>Go with i-escape:</b> Oaxaca city is blessed with affordable boutique hotels. Our 2 favourites are the stylish Casa Oaxaca, with its excellent cuisine and pool; and the intimate 3-bedroom colonial house La Casa de los Milagros (‘the House of Miracles’) in the heart of the city.    </p>');
story_location.push([-96.7,17]);
story_zoom.push(14);

// Story page
story_title.push('#5  Porto, Portugal');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/PORTO1.jpg"><p><b>Why go now?</b> Europe’s new capital of cool.</b><p>Five years ago, Porto was nowhere. Today, it’s on every hipster’s bucket list. Portugal’s second city is enjoying an amazing renaissance, largely thanks to its young citizens. Last year saw an explosion of new boutique shops, restaurants and lively bars. But the city also boasts Medieval architecture, blue flag beaches and the world’s most beautiful bookstore. And it’s only 2 hours from London!</p><p><b>Go with i-escape:</b> We love these stylish seafront self-catering apartments (for 2-5), just a tram ride from the historic centre. Rosa Et Al Townhouse is a great-value design hotel in Porto’s dynamic arty quarter. Just outside the city, Solar Egas Moniz is a charming new family-run guesthouse with fantastic prices (kids under 12 stay free).    </p>');
story_location.push([-8.56,41.13]);
story_zoom.push(13);

// Story page
story_title.push('#4 The Balearic Islands for Families');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/BALEARIC1.jpg"><p><b>Why go now?</b> Adios, Club 18-30!</b><p>For the first time in a generation, the Balearics will be free of Club 18-30 revellers. The recent demise of the party brand is great news for Ibiza, Menorca and Mallorca, who can now focus on what they do best – providing sun-kissed family holidays with plenty of activities (picnic beaches, jeep safaris, cave tours, zip-lining), along with lots of stylish family hotels.</p><p><b>Go with i-escape:</b> For Ibiza, Agro Can Gall is a relaxed 11-room finca set in beautiful grounds. These 4 family rentals in Cala Carbo have pools and sea views, while Can Talaias, near San Carlo, is a wonderful boho agriturismo. For Mallorca, StayCatalina apartments (for 2-5) are lovely family options, as is Portixol, a super-stylish harbourside hotel near Palma. For Menorca, the small yet family-friendly Casa Alberti hotel has a real soul.    </p>');
story_location.push([2.9,39.5]);
story_zoom.push(9);

// Story page
story_title.push('#3 Sri Lanka');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/LANKA-MAIN.jpg"><p><b>Why go now?</b> Your entire bucket list on one island.</p><p>Here’s a striking thought: Sri Lanka is smaller than Ireland but it contains golden beaches, gorgeous waterfalls, wild elephants, sacred temples, epic mountain ranges, modern cities and probably your last chance to spot a leopard in the wild. And that’s just scratching the surface. Take a stunning train ride, surf the southern coasts, or just relax with the best cup of tea of your life.</p><p><b>Go with i-escape:</b> The Saffron House on the south coast is a stylish staffed villa, perfect for families (sleeps 4-8). On the east coast, new luxury tented resort Karpaha Sands occupies a deserted beach and has a wonderful vibe. Brand-new Rukgala Retreat is a tranquil wellness retreat in the Knuckles Mountains, an hour from Kandy. And chic Serendipity Villa (for 2-5) on a golden beach in Galle was voted ‘Best Long-haul Rental 2018’ by our guests.     </p>');
story_location.push([81.4,7.7]);
story_zoom.push(9);

// Story page
story_title.push('#2 Scotland');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/SCOT.jpg"><p><b>Why go now?</b>  It will stir your soul like no place on earth.</p><p>Suddenly, everybody’s talking about Scotland. Is it the Brexit bounce? Who knows, but the majestic lochs and dramatic glens of bonnie Scotland are the UK’s prime destination this year. With a new high-speed train network, a surging interest in the Highlands, and Edinburgh being voted Britain’s most attractive city, you’d be aff ye heid not to visit.</p><p><b>Go with i-escape:</b>  Mhor 84 motel is a fabulous gateway to the Scottish Highlands, with great food and terrific prices. 15 Glasgow is an opulent B&B townhouse near the city centre. In Edinburgh, The Dunstane is a luxurious small hotel in a grand Victorian villa in peaceful Haymarket, while the gorgeous Georgian apartments at The Chester Residence are perfect for weekend breaks.     </p>');
story_location.push([-2.9,56.9]);
story_zoom.push(8);

// Story page
story_title.push('#1 South Africa');
story_content.push('<img width=100% src="https://www.i-escape.com/blog/wp-content/uploads/2018/12/AFRICA1.jpg"><p><b>Why go now?</b> Because it will change your life.</p><p>A country that literally has it all – incredible landscapes, jaw-dropping beaches, a world-class city, fabulous wine, and the ‘Big Five’ – South Africa is surely the world’s most beautiful destination. Rich in history, diverse in culture, it’s also a country blessed with eternal sunshine. But what makes South Africa truly special is that even now, in 2019, there are still many hidden places that will actually change your life. Just go.</p><p><b>Go with i-escape:</b> Boschendal is a historic wine estate with luxury cottages, just 45 minutes from Cape Town. Oceans Wilderness is a super-stylish 15-room hotel on pristine Wilderness Beach, between Cape Town and Port Elizabeth. And Madikwe Safari Lodge offers some of the greatest ‘Big Five’ safaris in South Africa (stay 5 nights, pay for 3!)    </p>');
story_location.push([25,-29]);
story_zoom.push(7);

// create the navigation controls
function addNavigation() {
    var html_source = '<button onClick="previousPage()">Previous</button>';
    html_source += '<button onClick="nextPage()">Next</button>';
    html_source += '<button onClick="firstPage()">Reset</button>';
    document.getElementById('story_footer').innerHTML = html_source;
}

// update the story page
function doPage(page) {
    // Open Layers
    document.getElementById('story_header').innerHTML = story_title[page];
    document.getElementById('story_body').innerHTML = story_content[page];
    map.getView().setCenter(ol.proj.transform(story_location[page], 'EPSG:4326', 'EPSG:3857'));
    map.getView().setZoom(story_zoom[page]);

}

// advance story by one page
function nextPage() {
    current_page++;
    if (current_page == story_content.length) {
        current_page = 0;
    }
    doPage(current_page);
}

// go back one page in story
function previousPage() {
    current_page--;
    if (current_page == -1) {
        current_page = story_content.length - 1;
    }
    doPage(current_page);
}

// go to first story page == RESET
function firstPage() {
    current_page = 0;
    doPage(current_page);
}


// add navigation controls
addNavigation();

// set the start page
firstPage();