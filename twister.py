from PIL import Image 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["white"] 
background_weights = [100]

body = ["darkblue", "darkgreen", "darkpurple", "grey", "lightblue", "lightgreen", "lightpurple", "magenta", "orange", "red", "yellow"] 
body_weights = [9,9,9,1,9,9,9,9,9,9,9]

fenders = ["darkblue", "darkgreen", "darkpurple", "grey", "lightblue", "lightgreen", "lightpurple", "magenta", "orange", "red", "yellow"] 
fenders_weights = [9,9,9,1,9,9,9,9,9,9,9]

shadow = ["darkblue", "darkgreen", "darkpurple", "grey", "lightblue", "lightgreen", "lightpurple", "magenta", "orange", "red", "yellow"] 
shadow_weights = [9,9,9,1,9,9,9,9,9,9,9]

top = ["outline"] 
top_weights = [100]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

background_files = {
    "white": "white"
}

body_files = {
    "darkblue": "darkblue",
    "darkgreen": "darkgreen",
    "darkpurple": "darkpurple",
    "grey": "grey",
    "lightblue": "lightblue",
    "lightgreen": "lightgreen",
    "lightpurple": "lightpurple",
    "magenta": "magenta",
    "orange": "orange",
    "red": "red",
    "yellow": "yellow"
}

fenders_files = {
    "darkblue": "darkblue",
    "darkgreen": "darkgreen",
    "darkpurple": "darkpurple",
    "grey": "grey",
    "lightblue": "lightblue",
    "lightgreen": "lightgreen",
    "lightpurple": "lightpurple",
    "magenta": "magenta",
    "orange": "orange",
    "red": "red",
    "yellow": "yellow"
}

shadow_files = {
    "darkblue": "darkblue",
    "darkgreen": "darkgreen",
    "darkpurple": "darkpurple",
    "grey": "grey",
    "lightblue": "lightblue",
    "lightgreen": "lightgreen",
    "lightpurple": "lightpurple",
    "magenta": "magenta",
    "orange": "orange",
    "red": "red",
    "yellow": "yellow"
}

top_files = {
    "outline": "outline"
}

#Create a function to generate unique image combinations
TOTAL_IMAGES = 504 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Body"] = random.choices(body, body_weights)[0]
    new_image ["Fenders"] = random.choices(fenders, fenders_weights)[0]
    new_image ["Shadow"] = random.choices(shadow, shadow_weights)[0]
    new_image ["Top"] = random.choices(top, top_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)

#Return true if all images are unique

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

#add token id

i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

#print all images

print(all_images)

#get trait count

background_count = {}
for item in background:
    background_count[item] = 0

body_count = {}
for item in body:
    body_count[item] = 0

fenders_count = {}
for item in fenders:
    fenders_count[item] = 0

shadow_count = {}
for item in shadow:
    shadow_count[item] = 0

top_count = {}
for item in top:
    top_count[item] = 0

for image in all_images:
    background_count[image["Background"]] += 1
    body_count[image["Body"]] += 1
    fenders_count[image["Fenders"]] += 1
    shadow_count[image["Shadow"]] += 1
    top_count[image["Top"]] += 1

print(background_count)
print(body_count)
print(fenders_count)
print(shadow_count)
print(top_count)

#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:
    im1 = Image.open(f'./layers/background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/shadow/{shadow_files[item["Shadow"]]}.png').convert('RGBA')    
    im3 = Image.open(f'./layers/fenders/{fenders_files[item["Fenders"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/body/{body_files[item["Body"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/top/{top_files[item["Top"]]}.png').convert('RGBA')


    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    #Convert to RGB
    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

#Generate Metadata

#f = open('./metadata/all-traits.json',) 
#data = json.load(f)

#IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE/"
#PROJECT_NAME = "Balloon Animals"

#def getAttribute(key, value):
#    return {
#        "trait_type": key,
#        "value": value
#    }
#for i in data:
#    token_id = i['tokenId']
#    token = {
#        "image": IMAGES_BASE_URI + str(token_id) + '.png',
#        "tokenId": token_id,
#        "name": PROJECT_NAME + ' ' + str(token_id),
#        "attributes": []
#    }
#    token["attributes"].append(getAttribute("Background", i["Background"]))
#    token["attributes"].append(getAttribute("Back Legs", i["Back Legs"]))
#    token["attributes"].append(getAttribute("Body", i["Body"]))
#    token["attributes"].append(getAttribute("Ears", i["Ears"]))
#    token["attributes"].append(getAttribute("Front Legs", i["Front Legs"]))
#    token["attributes"].append(getAttribute("Head", i["Head"]))
#    token["attributes"].append(getAttribute("Neck", i["Neck"]))
#    token["attributes"].append(getAttribute("Tail", i["Tail"]))
#    token["attributes"].append(getAttribute("Outline", i["Outline"]))

#    with open('./metadata/' + str(token_id), 'w') as outfile:
#        json.dump(token, outfile, indent=4)
#f.close()