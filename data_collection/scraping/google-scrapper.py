from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import os
import urllib3 
import argparse
import requests




def download_img(term, max):
    http = urllib3.PoolManager()
    searchterm = term # will also be the name of the folder
    url = "https://www.google.co.in/search?q="+searchterm+"&source=lnms&tbm=isch"
    # NEED TO DOWNLOAD CHROMEDRIVER, insert path to chromedriver inside parentheses in following line
    option = webdriver.ChromeOptions()
    option.add_argument('--kiosk')
    browser = webdriver.Chrome(r"D:\Users\SoraBeast\Documents\_projects\web-object-detection\scrapper\chromedriver.exe", chrome_options = option)
    browser.get(url)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    counter = 0
    succounter = 0

    if not os.path.exists(searchterm):
        os.mkdir(searchterm)

    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")

    for x in browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]'):
        try:
        
            counter = counter + 1
            print ("Total Count:", counter)
            print ("Succsessful Count:", succounter)
            print ("URL:",json.loads(x.get_attribute('innerHTML'))["ou"])

            img = json.loads(x.get_attribute('innerHTML'))["ou"]
            imgtype = json.loads(x.get_attribute('innerHTML'))["ity"]
            # req = http.request('GET',img, headers={'User-Agent': header})
            # req = http.request('GET',img)
            # raw_img = urllib3.connectionpool.HTTPConnectionPool.urlopen(req).read()
            
            # raw_img = http.urlopen(method = 'GET',url = img, headers={'User-Agent': header}).read()

            # raw_img = urllib3.urlopen(img).read()/
            response = requests.get(img, stream = True)
            File = open(os.path.join(searchterm , searchterm + "_" + str(counter) + "." + imgtype), "wb")
            
            for block in response.iter_content(1024):
                if not block:
                    break
                File.write(block)
            File.close()
            succounter = succounter + 1

            if succounter > max:
                return
        except Exception as e:
            print(e)
            print ("can't get img")

    print (succounter, "pictures succesfully downloaded")
    browser.close()




# Common plants
# target = [ "genus hibiscus",
#             "genus plumeria",
#             "genus pineapple",
#             "genus ginger",     #redo, better search term
#             "zingiberaceae",    # same as ginger
#             "genus anthurium",  
#             "genus heliconia",
#             "genus bougainvillea" ]

#Native plants
canoe = [
    "Aleurites moluccana – Kukui",
    "Artocarpus altilis – Breadfruit",
    "Cocos nucifera – Coconut Palm",
    "Cordia subcordata – Kou",
    "Cordyline fruticosa – Ti",
    "Dioscorea bulbifera – Air Yam",
    "Hibiscus tiliaceus – Hau",
    "Ipomoea cairica – Mile A Minute Vine",
    "Morinda citrifolia – Noni",
    "Pandanus tectorius – Hala",
    "Saccharum officinarum – Sugarcane",
    "Syzygium malaccense – Mountain Apple",
    "Thespesia populnea – Milo",
    "Zingiber zerumbet – Shampoo Ginger"
]
native = [
    "Argemone glauca – Pua Kala",
    "Cibotium spp. – Hapu'u",
    "Coprosma ernodeoides – 'Aiakanene",
    "Cordia subcordata – Kou",
    "Dicranopteris linearis – Old World Forkedfern",
    "Dodonaea viscosa – Florida Hopbush",
    "Geranium cuneatum – Hinahina",
    "Hibiscus brackenridgei – Ma'o Hau Hele",
    "Ipomoea indica – Oceanblue Morning-glory",
    "Ludwigia octovalvis – Mexican Primrose-willow",
    "Lycopodiella cernua – Staghorn Clubmoss",
    "Metrosideros polymorpha – 'Ohi'a Lehua",
    "Mucuna gigantea – Seabean",
    "Pandanus tectorius – Hala",
    "Rhus sandwicensis – Neneleau",
    "Sadleria cyatheoides – Amaumau Fern",
    "Scaevola sericea – Beach Naupaka",
    "Solanum americanum – American Black Nightshade",
    "Sophora chrysophylla – Mamane",
    "Styphelia tameiameiae – Pukiawe",
    "Thespesia populnea – Milo",
    "Vaccinium calycinum – Ohelo Kau La'au",
    "Vaccinium reticulatum – Ohelo 'Ai"
]
cultivated = [
    "Ananas bracteatus – Red Pineapple",
    "Ananas comosus – Pineapple",
    "Anthurium andraeanum – Anthurium",
    "Artocarpus altilis – Breadfruit",
    "Bougainvillea spp. – Bougainvillea",
    "Calathea burle-marxii – Ice Blue Calathea",
    "Costus comosus – Red Tower Ginger",
    "Costus woodsonii – Indian Head Ginger",
    "Dichorisandra thyrsiflora – Blue Ginger",
    "Dracaena reflexa – Song of India",
    "Etlingera elatior – Torch Ginger",
    "Heliconia psittacorum – Parakeet Heliconia",
    "Heliconia rostrata – Hanging Lobster Claw",
    "Hibiscus rosa-sinensis – Chinese Hibiscus",
    "Hibiscus schizopetalus – Coral Hibiscus",
    "Monstera deliciosa – Monstera",
    "Musa acuminata – Banana",
    "Musa ornata – Flowering Banana",
    "Otacanthus caeruleus – Brazilian Snapdragon",
    "Plumeria obtusa – Singapore Plumeria",
    "Plumeria rubra – Frangipani",
    "Rotheca myricoides – Blue Butterfly Bush",
    "Saccharum officinarum – Sugarcane",
    "Strelitzia reginae – Bird of Paradise",
    "Tapeinochilos ananassae – Indonesian Wax Ginger"
]

introduced = [
    "Abrus precatorius – Rosary Pea",
    "Ageratum spp. – Ageratum",
    "Aleurites moluccana – Kukui"
    "Allamanda cathartica – Allamanda",
    "Alpinia purpurata – Red Ginger",
    "Alpinia zerumbet – Shell Ginger"
    "Anemone hupehensis – Japanese Thimbleweed",
    "Araucaria columnaris – Cook Pine",
    "Archontophoenix alexandrae – Alexandra Palm",
    "Arthrostemma ciliatum – Pinkfringe",
    "Arundina graminifolia – Bamboo Orchid",
    "Asystasia gangetica ssp. micrantha – Small Chinese Violet",
    "Barleria repens – Coral Creeper",
    "Breynia disticha – Snowbush",
    "Buddleja asiatica – Dogtail",
    "Calathea crotalifera – Rattlesnake Plant",
    "Canna indica – Indian Shot",
    "Carica papaya – Papaya",
    "Castilleja arvensis – Field Indian Paintbrush",
    "Casuarina equisetifolia – Common Ironwood",
    "Cecropia obtusifolia – Trumpet Tree",
    "Cestrum nocturnum – Night-blooming Jasmine",
    "Citharexylum caudatum – Juniper Berry",
    "Clerodendrum indicum – Turk's Turban",
    "Clidemia hirta – Koster's Curse",
    "Clusia rosea – Autograph Tree",
    "Coccoloba uvifera – Sea Grape",
    "Cocos nucifera – Coconut Palm",
    "Coffea arabica – Coffee",
    "Commelina diffusa – Climbing Dayflower",
    "Cordyline fruticosa – Ti",
    "Costus speciosus – Crepe Ginger",
    "Costus woodsonii – Indian Head Ginger",
    "Crassocephalum crepidioides – Redflower Ragleaf",
    "Crocosmia × crocosmiiflora – Montbretia",
    "Delonix regia – Royal Poinciana",
    "Desmodium intortum – Greenleaf Ticktrefoil",
    "Dioscorea bulbifera – Air Yam",
    "Emilia fosbergii – Florida Tasselflower",
    "Emilia sonchifolia – Lilac Tasselflower",
    "Epipremnum pinnatum – Golden Pothos",
    "Falcataria moluccana – Moluccan Albizia",
    "Geranium homeanum – Australasian Geranium",
    "Grevillea robusta – Silk Oak",
    "Hedychium coronarium – White Ginger",
    "Hedychium flavescens – Yellow Ginger",
    "Hedychium gardnerianum – Kahili Ginger",
    "Heliconia bihai – Macaw Flower",
    "Heliconia latispatha – Expanded Lobster Claw",
    "Heliconia psittacorum – Parakeet Heliconia",
    "Heterocentron subtriplinervium – Pearlflower",
    "Heterotheca grandiflora – Telegraphweed",
    "Hibiscus tiliaceus – Hau",
    "Hippobroma longiflora – Madam Fate",
    "Ipomoea alba – Moonflower",
    "Ipomoea cairica – Mile A Minute Vine",
    "Ipomoea obscura – Obscure Morning-glory",
    "Ipomoea ochracea – Fence Morning-glory",
    "Ipomoea triloba – Littlebell",
    "Justicia betonica – Squirrel's Tail",
    "Kalanchoe pinnata – Air Plant",
    "Lantana camara – Lantana",
    "Leucaena leucocephala – White Leadtree",
    "Macaranga mappa – Bingabing",
    "Macroptilium atropurpureum – Purple Bushbean",
    "Macroptilium lathyroides – Wild Bushbean",
    "Malvaviscus penduliflorus – Mazapan",
    "Mangifera indica – Mango",
    "Medinilla magnifica – Rose Grape",
    "Melinis minutiflora – Molasses Grass",
    "Melochia umbellata – Melochia",
    "Merremia tuberosa – Woodrose",
    "Miconia calvescens – Velvet Tree",
    "Mimosa pudica var. unijuga – Sensitive Plant",
    "Momordica charantia – Bitter Melon",
    "Morinda citrifolia – Noni",
    "Odontonema cuspidatum – Mottled Toothedthread",
    "Otacanthus caeruleus – Brazilian Snapdragon",
    "Oxalis debilis var. corymbosa – Pink Wood Sorrel",
    "Paederia foetida – Stinkvine",
    "Passiflora edulis f. flavicarpa – Liliko'i",
    "Passiflora vitifolia – Perfumed Passionflower",
    "Persea americana – Avocado",
    "Phaius tancarvilleae – Nun's-hood Orchid",
    "Phymatosorus grossus – Musk Fern",
    "Pistia stratiotes – Water Lettuce",
    "Pluchea carolinensis – Cure For All",
    "Plumbago auriculata – Plumbago",
    "Polygonum capitatum – Pinkhead Smartweed",
    "Psidium cattleianum – Strawberry Guava",
    "Psidium guajava – Guava",
    "Rhizophora mangle – Red Mangrove",
    "Ricinus communis – Castor Bean",
    "Rubus argutus – Sawtooth Blackberry",
    "Rubus rosifolius – West Indian Raspberry",
    "Sanchezia spp. – Sanchezia",
    "Schefflera actinophylla – Octopus Tree",
    "Schinus terebinthifolius – Brazilian Peppertree",
    "Senna alata – Emperor's Candlesticks",
    "Setaria palmifolia – Palmgrass",
    "Solenostemon scutellarioides – Coleus",
    "Spathodea campanulata – African Tulip Tree",
    "Spathoglottis plicata – Philippine Ground Orchid",
    "Sphagneticola trilobata – Wedelia",
    "Stachytarpheta spp. – Porterweed",
    "Syzygium malaccense – Mountain Apple",
    "Thevetia peruviana – Be-still Tree",
    "Thunbergia alata – Blackeyed Susan Vine",
    "Thunbergia fragrans – White Lady",
    "Thunbergia grandiflora – Bengal Trumpet",
    "Tibouchina urvilleana – Princess-flower",
    "Tropaeolum majus – Nasturtium",
    "Verbascum blattaria – Moth Mullein",
    "Verbascum thapsus – Common Mullein",
    "Zingiber zerumbet – Shampoo Ginger"
]
target = canoe
for t in target:
    print("================= downloading {} =================== ", t)
    download_img(t, max)