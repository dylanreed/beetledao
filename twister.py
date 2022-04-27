from PIL import Image 
from IPython.display import display 
import random
import json

#Inject all the shapes and set their weights

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

#background = ["balloon", "basket case", "black and blue", "nervous", "orange is the new green", "pretty", "too bright"]  
#background_weights =  [15, 15, 14, 14, 14, 14, 14]

body = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
body_weights = [14, 15, 15, 14, 14, 14, 14]

leftbackleg = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
leftbackleg_weights = [14, 14, 15, 15, 14, 14, 14]

leftear = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
leftear_weights = [14, 14, 14, 15, 15, 14, 14]

leftfrontleg = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
leftfrontleg_weights = [14, 14, 14, 14, 15, 15, 14]

neck = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
neck_weights = [14, 14, 14, 14, 14, 15, 15]

nose = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
nose_weights = [15, 14, 14, 14, 14, 14, 15]

rightbackleg = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
rightbackleg_weights = [15, 15, 14, 14, 14, 14, 14]

rightear = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
rightear_weights = [14, 15, 15, 14, 14, 14, 14]

rightfrontleg = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  
rightfrontleg_weights = [14, 14, 15, 15, 14, 14, 14]

tail = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  
tail_weights = [14, 14, 14, 15, 15, 14, 14]

outline = ["black"]  
outline_weights = [100]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name
# Add more shapes and colours as you wish

#background_files = {
#    "balloon": "balloon",
#    "basket case": "basket-case",
#    "black and blue": "black-blue",
#    "nervous": "nervous",
#    "orange is the new green": "orange-green",
#    "pretty": "pretty",
#    "too bright": "too-bright"
#}

body_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

leftbackleg_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

leftear_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

leftfrontleg_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

neck_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

nose_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

outline_files = {
    "black": "black",
    #"grey": "grey",
    "white": "white"
}

rightbackleg_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

rightear_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

rightfrontleg_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}

tail_files = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "indigo": "indigo",
    "violet": "violet"
}
#Create a function to generate unique image combinations
TOTAL_IMAGES = 100 # Number of random unique images we want to generate ( 2 x 2 x 2 = 8)

all_images = [] 

def create_new_image():

    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    #new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Body"] = random.choices(body, body_weights)[0]
    new_image ["Left Back Leg"] = random.choices(leftbackleg, leftbackleg_weights)[0]
    new_image ["Left Ear"] = random.choices(leftear, leftear_weights)[0]
    new_image ["Left Front Leg"] = random.choices(leftfrontleg, leftfrontleg_weights)[0]
    new_image ["Neck"] = random.choices(neck, neck_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    new_image ["Outline"] = random.choices(outline, outline_weights)[0]
    new_image ["Right Back Leg"] = random.choices(rightbackleg, rightbackleg_weights)[0]
    new_image ["Right Ear"] = random.choices(rightear, rightear_weights)[0]
    new_image ["Right Front Leg"] = random.choices(rightfrontleg, rightfrontleg_weights)[0]
    new_image ["Tail"] = random.choices(tail, tail_weights)[0]


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

#background_count = {}
#for item in background:
#    background_count[item] = 0

body_count = {}
for item in body:
    body_count[item] = 0

leftbackleg_count = {}
for item in leftbackleg:
    leftbackleg_count[item] = 0

leftear_count = {}
for item in leftear:
    leftear_count[item] = 0

leftfrontleg_count = {}
for item in leftfrontleg:
    leftfrontleg_count[item] = 0

neck_count = {}
for item in neck:
    neck_count[item] = 0

nose_count = {}
for item in nose:
    nose_count[item] = 0

outline_count = {}
for item in outline:
    outline_count[item] = 0

rightbackleg_count = {}
for item in rightbackleg:
    rightbackleg_count[item] = 0

rightear_count = {}
for item in rightear:
    rightear_count[item] = 0

rightfrontleg_count = {}
for item in rightfrontleg:
    rightfrontleg_count[item] = 0

tail_count = {}
for item in tail:
    tail_count[item] = 0

for image in all_images:
    #background_count[image["Background"]] += 1
    body_count[image["Body"]] += 1
    leftbackleg_count[image["Left Back Leg"]] += 1
    leftear_count[image["Left Ear"]] += 1
    leftfrontleg_count[image["Left Front Leg"]] += 1
    neck_count[image["Neck"]] += 1
    nose_count[image["Nose"]] += 1
    outline_count[image["Outline"]] += 1
    rightbackleg_count[image["Right Back Leg"]] += 1
    rightear_count[image["Right Ear"]] += 1
    rightfrontleg_count[image["Right Front Leg"]] += 1
    tail_count[image["Tail"]] += 1


#print(background_count)
print(body_count)
print(leftbackleg_count)
print(leftear_count)
print(leftfrontleg_count)
print(neck_count)
print(nose_count)
print(outline_count)
print(rightbackleg_count)
print(rightear_count)
print(rightfrontleg_count)
print(tail_count)


#Generate Metadata for all Traits

METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)


#Generate Images

for item in all_images:

    #im1 = Image.open(f'./layers/background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./layers/body/{body_files[item["Body"]]}.png').convert('RGBA')
    im3 = Image.open(f'./layers/left back leg/{leftbackleg_files[item["Left Back Leg"]]}.png').convert('RGBA')
    im4 = Image.open(f'./layers/left ear/{leftear_files[item["Left Ear"]]}.png').convert('RGBA')
    im5 = Image.open(f'./layers/left front leg/{leftfrontleg_files[item["Left Front Leg"]]}.png').convert('RGBA')
    im6 = Image.open(f'./layers/neck/{neck_files[item["Neck"]]}.png').convert('RGBA')
    im7 = Image.open(f'./layers/nose/{nose_files[item["Nose"]]}.png').convert('RGBA')
    im8 = Image.open(f'./layers/right back leg/{tail_files[item["Tail"]]}.png').convert('RGBA')
    im9 = Image.open(f'./layers/right ear/{rightbackleg_files[item["Right Back Leg"]]}.png').convert('RGBA')
    im10 = Image.open(f'./layers/right front leg/{rightear_files[item["Right Ear"]]}.png').convert('RGBA')
    im11 = Image.open(f'./layers/tail/{rightfrontleg_files[item["Right Front Leg"]]}.png').convert('RGBA')
    im12 = Image.open(f'./layers/outline/{outline_files[item["Outline"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im2, im3)
    com2 = Image.alpha_composite(com1, im4)
    com3 = Image.alpha_composite(com2, im5)
    com4 = Image.alpha_composite(com3, im6)
    com5 = Image.alpha_composite(com4, im7)
    com6 = Image.alpha_composite(com5, im8)
    com7 = Image.alpha_composite(com6, im9)
    com8 = Image.alpha_composite(com7, im10)
    com9 = Image.alpha_composite(com8, im11)
    com10 = Image.alpha_composite(com9, im12)
    #com11 = Image.alpha_composite(com10, im12)
    #Convert to RGB
    rgb_im = com10.convert('RGB')
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