import re
import nltk
from nltk.stem import PorterStemmer

nltk.download("punkt")
# Initialize Python porter stemmer
ps = PorterStemmer()


class BCI:
    def __init__(self):

        # defining the arrays for each
        self.claims = ["Additive Free", "Adulteration Free", "Alcohol Free", "Allergy Tested", "Aluminium Free",
                       "Ammonia Free", "Animal Oil Free", "Artificial Colorant Free", "Ayurvedic", "Beard Friendly",
                       "Biodegradable", "BPA Free", "Chemical Filter Free", "Chemical Free", "Chloride Free", "Clean",
                       "Climate Pledge Friendly", "Clinically Proven", "Color Free", "Compostable", "Cruelty Free",
                       "Dairy Free", "Dermatologically Formulated", "Dermatologically Recommended",
                       "Dermatologically Tested", "Detergent Free", "Dilution Free", "Disposable", "Drug Free",
                       "Dye Free", "Eco Friendly", "Essential Oil Free", "EWG Rated", "Extra Virgin", "Filler Free",
                       "Food Grade", "FormalDehyde Free", "Fragrance Free", "Gluten Free", "Glycol Free", "GMO Free",
                       "GMP Certified", "Hand Pressed", "Harsh Chemical Free", "Heavy Metal Free", "Herbal",
                       "Hexane Free", "Hypoallergenic", "Irritant Free", "Kosher", "Halal", "Lanolin Free",
                       "Made with Renewable Energy", "Microplastic Free", "Mineral Oil Free", "Nanoparticle Free",
                       "Natural/Organic", "Non Comedogenic", "Non Greasy", "Non Synthetic", "Nourishing", "Ocean Safe",
                       "Octinoxate Free", "Octocrylene Free", "Oil Free", "OMC Free", "Opthalmologist Tested",
                       "Oxybenzone Free", "PABA Free", "Palm Oil Free", "Paraben Free", "Paraffin Free",
                       "Pediatrician Tested", "Petrochemical Free", "Petrolatum Free", "Petroleum Free", "pH Balanced",
                       "Phthalate Free", "Plant Based", "Vegan", "Plant Scientist Certified", "Preservative Free",
                       "Pure", "Recyclable", "Recyclable Packaging", "Reef Friendly", "Residue Free",
                       "Safe Ingredients", "Salt Free", "Silicone Free", "SLS Free", "Soap Free", "Solvent Free",
                       "Soy Free", "Spotless", "Sulfate Free", "Sustainably Produced", "Sustainably Sourced",
                       "Talcum Free", "Toxin Free", "Traditionally Roasted", "Triclocarban Free", "Triclosan Free",
                       "Unrefined", "Untoasted", "USDA Certified", "Vegan", "Vegetarian", "Virgin"]

        self.ingredient_match = ["Acai berry", "Acerola fruit extract", "Amla", "Algae extract", "Amla fruit extract",
                                 "Apple blossom extract", "Apple blossom water", "Apple fruit extract",
                                 "Apricot kernel oil", "Apricot seed powder", "Aspen bark extract",
                                 "Atlas Cedar bark oil", "Avocado extract", "Avocado oil", "Babassu seed oil",
                                 "Balm mint leaf extract", "Bamboo stem extract", "Banana extract",
                                 "Basil extract (flowers and leaves)", "Basil oil", "Beeswax", "Beet extract",
                                 "Behentrimonium chloride", "Behenyl Alcohol", "Bentonite clay", "Benzoic acid",
                                 "Benzoin resin", "Benzyl alcohol", "Benzyl benzoate", "Benzyl salicylate",
                                 "Bergamot extract", "Bergamot fruit oil", "Bergamot peel oil", "Betaine", "BHT",
                                 "Birch leaf extract", "Birch sugar", "Bistort root extract", "Bitter cherry acid",
                                 "Bitter orange extract", "Bitter orange flower water", "Bitter orange oil",
                                 "Bitter orange peel extract", "Bitter orange peel oil", "Black Cherry Bark Extract",
                                 "Black dye", "Black pepper extract", "Black pepper fruit oil",
                                 "Black willow bark extract", "Blue dye", "Blueberry fruit extract",
                                 "Blueberry seed oil", "Borage seed oil", "Brilliant blue FCF", "Broccoli seed oil",
                                 "Brown dye", "Burr extract (Japanese chestnut)", "Butane", "Butcherbroom extract",
                                 "Butterfly bush flower extract", "Butylene glycol", "Butylphenyl Methylpropional",
                                 "Cade wood oil", "Caffeine", "Calcite", "Camelina seed oil", "Camphor",
                                 "Camphor bark oil", "Camu-camu fruit extract", "Candelilla wax",
                                 "Caprylic/Capric Triglyceride", "Caprylyl glycol", "Caramel (dye)", "Carbomer",
                                 "Carnauba wax", "Carrageenan (red algae)", "Carrot extract", "Carrot seed oil",
                                 "Castor seed oil", "Cedar wood oil", "Cedarwood oil", "Cellulose", "Cellulose gum",
                                 "Ceteayl alcohol", "Cetrimonium Chloride", "Cetyl alcohol", "Chamomile extract",
                                 "Chamomile flower extract", "Chamomile flower oil", "Chamomile flower water",
                                 "Chamomile oil", "Charcoal powder", "Chaulmoogra seed extract",
                                 "Chebulic myrobalan extract (fruit)", "Cherry Seed oil", "Chlorphenesin", "Cinnamal",
                                 "Cinnamon bark extract", "Cinnamon bark oil", "Cinnamyl alcohol", "Citral",
                                 "Citric acid", "Citronella oil", "Citronellol", "Clary sage flower oil",
                                 "Clary sage oil", "Clay", "Clove extract", "Clove flower oil", "Clove Leaf Oil",
                                 "Cocamidopropyl betaine", "Cocoa extract", "Cocoa seed butter", "Coco-glucoside",
                                 "Coconut extract", "Coconut fatty acids", "Coconut milk", "Coconut oil",
                                 "Coconut water", "Coenzyme Q10", "Coffee arabica seed powder", "Coffee extract",
                                 "Coffee seed oil", "Coriander extract", "Coriander fruit oil", "Coriander seed oil",
                                 "Corn grain extract", "Corn mint oil", "Corn oil", "Corn silk extract", "Corn starch",
                                 "Cornflower flower water", "Cotton extract", "Cotton seed oil", "Coumarin",
                                 "Crambe abyssinica (seed) oil", "Cranberry Seed Powder", "Crocus bulb extract",
                                 "Cucumber extract", "Cucumber juice", "Cyclopentasiloxane", "Cypress leaf oil",
                                 "Cypress oil", "Damask rose flower", "Damask rose flower extract",
                                 "Damask rose flower oil", "Damask rose wax", "Date extract", "Date syrup",
                                 "Decyl glucoside", "Dehydroacetic acid", "Derived from Xylitol", "Dimethicone",
                                 "Disodium EDTA", "Disodium Inosinate", "DMDM hydantoin", "Egg",
                                 "Eucalyptus leaf extract", "Eucalyptus oil", "Eugenol",
                                 "Evening Primrose leaf extract", "Evening primrose oil", "everlasting oil",
                                 "Fennel fruit extract", "Fennel oil", "Fenugreek seed extract", "Flower extract",
                                 "thyme leaf", "Frankincense gum oil", "Frankincense oil", "Frozen Ficoide Extract",
                                 "Fruit / Leaf bay rum tree extract", "Geraniol", "Geranium extract",
                                 "Geranium flower oil", "Geranium leaf oil", "Geranium oil", "Ginger extract",
                                 "Ginger root extract", "Ginger root oil", "Ginger water", "Ginkgo leaf extract",
                                 "Ginseng root extract", "Glucose", "Glutamic acid", "Glycerin", "Glyceryl oleate",
                                 "Glyceryl stearate", "Goat milk", "Goji berry", "Grape extract", "Grape leaf extract",
                                 "Grape seed extract", "Grape seed oil", "Grapefruit peel oil", "Grapefruit seed oil",
                                 "Green dye", "Green tea seed extract", "Guar gum", "Guarana seed extract",
                                 "Guava extract", "Hazelnut oil", "Hemidesmus indicus root extract", "Hemp seed oil",
                                 "Hexyl cinnamal", "Hibiscus flower extract", "Honey", "Honeysuckle flower extract",
                                 "Horsetail extract", "Hot Spring-water", "Hyaluronic acid", "Hybrid Lavender oil",
                                 "Hybrid sunflower oil", "Hydrogenated and ethoxylated castor oil",
                                 "Hydrogenated castor oil", "Hydrogenated coconut oil", "Hydrogenated jojoba oil",
                                 "Hydrogenated Vegetable oil", "Hydrolyzed corn protein", "Hydrolyzed keratin",
                                 "Hydrolyzed Milk protein", "Hydrolyzed silk", "Hydrolyzed wheat protein",
                                 "Hydroxycitronellal", "Iceland moss extract", "Illite Clay",
                                 "Indian Grossberry extract", "Isoeugenol", "Isopropyl alcohol", "Ivy extract",
                                 "Japanese Bayberry juice", "Japanese camellia leaf extract",
                                 "Japanese Honeysuckle flower extract", "Jasmine extract", "Jasmine flower extract",
                                 "Jasmine flower oil", "Jasmine oil", "Jojoba esters", "Jojoba seed oil",
                                 "Jujube leaves", "Juniper berry extract", "Kakadu Plum Extract", "Kaolin clay",
                                 "Karanja seed oil", "Kelp extract", "Key lime extract", "Lactic acid", "Lanolin",
                                 "Lanolin alcohol", "Lanolin wax", "Laurel Berry Oil", "Lauric acid",
                                 "Lavender essential oil", "Lavender extract", "Lavender flower oil",
                                 "Lavender leaf oil", "Lavender water", "Lazurite (CI 77007)", "Leaf Extract",
                                 "Stem of Eucalyptus Radiate", "Lecithin", "Lemon fruit extract", "Lemon oil",
                                 "Lemon peel essential oil", "Lemon peel extract", "Lemon peel extract",
                                 "Lemongrass leaf oil", "Lemongrass oil", "Levulinic acid", "Licorice root extract",
                                 "Lime seed oil", "Limonene", "Linalool", "Linden oil", "Linseed flower extract",
                                 "Linseed seed oil", "Long pepper extract", "Lotus flower extract", "Macadamia nut oil",
                                 "Macadamia nut oil", "Magnesium chloride", "Magnesium stearate", "Magnolia leaf oil",
                                 "Mallow flower extract", "Maltodextrin", "Mandarin fruit extract",
                                 "Mandarin fruit extract", "Mandarin fruit extract", "Mandarin oil",
                                 "Mandarin peel oil", "Mandarin peel oil", "Mango butter", "Mango butter",
                                 "Mango extract", "Mangosteen fruit extract", "Manjistha root extract",
                                 "Manuka leaf extract", "Marigold flower extract", "Marigold flower oil",
                                 "Marula seed oil", "May-Chang fruit oil", "Meadowfoam seed oil", "Melon extract",
                                 "Menthol", "Methylchloroisothiazolinone", "Methylisothiazolinone", "Methylparaben",
                                 "Mica", "Milk", "Milk protein", "Milk protein", "Moringa Leaf Extract",
                                 "Mountain savory oil", "Myrrh oil", "Nectarine extract", "Neem leaf extract",
                                 "Neroli flower oil", "Nettle extract", "Niaouli leaf oil", "Niaouli oil",
                                 "Noni fruit juice", "Nutmeg kernel oil", "Oleic acid", "Olive extract",
                                 "Olive Leaf extract", "Olive Leaf extract", "Olive oil", "Orange dye", "Orange dye",
                                 "Orange dye", "Orange dye", "Orange dye", "Orange dye", "Orange dye", "Orange dye",
                                 "Orange dye", "Orange dye", "Orange dye", "Orange dye", "Orange dye", "Orange dye",
                                 "Orange dye", "Orange dye", "Orange dye", "Orange dye (Rocou)", "Orange extract",
                                 "Orange fruit extract", "Orange leaf oil", "Palm oil", "Palmarosa oil",
                                 "Palmitic acid", "Palmitic acid", "Pansy extract", "Papaya fruit extract", "Paraffin",
                                 "Paraffin oil", "Paraffin wax", "Passion fruit extract", "Patchouli oil",
                                 "Peach kernel oil", "Pear extract", "Pearl powder", "PEG-40 Hydrogenated castor oil",
                                 "Pentylene glycol", "Peony root extract", "Peppermint leaf extract", "Peppermint oil",
                                 "Perfume", "Phenethyl alcohol", "Phenoxyethanol", "Phosphoric acid", "Phytic acid",
                                 "Pistachio nut oil", "Plantago asiatica extract", "Plum seed oil", "Polysorbate 20",
                                 "Pomegranate fruit extract", "Pomegranate seed oil", "Potassium acetate",
                                 "Potassium bicarbonate", "Potassium hydroxide", "Potassium sorbate",
                                 "Prickly pear extract (flower and stem)", "Prickly pear seed oil", "Propanediol",
                                 "Propolis extract", "Propylene Glycol", "Propylparaben", "Provitamin B5",
                                 "Prussian blue dye", "Pumice", "Pumpkin extract", "Pumpkin seed extract",
                                 "Pumpkin seed oil", "Purple dye", "Purple dye", "Purple dye", "Purple dye",
                                 "Purple dye", "Purple dye", "Purple dye", "Purple dye", "Purple dye", "Purple dye",
                                 "Purslane extract", "Purslane extract", "Radish root ferment filtrate", "Rapeseed oil",
                                 "Rapeseed oil", "Ravensara aromatica Leaf oil", "Red dye (Carmine)",
                                 "Red dye (Iron trioxide)", "Rice bran oil", "Rice bran oil", "Rice bran wax",
                                 "Rice bran wax", "Rice extract", "Rice starch", "Rosa Damascena flower water",
                                 "Rose hip flower extract", "Rose oil", "Rosehip fruit oil", "Rosehip seed oil",
                                 "Rosehip seed oil", "Rosemary extract", "Rosemary flower oil", "Rosemary leaf extract",
                                 "Rosemary leaf oil", "Rosemary leaf water", "Rosemary water", "Rosin",
                                 "Sacha inchi seed oil", "Sacred Lotus flower extract", "Safflower seed oil",
                                 "Saffron flower extract", "Sage extract", "Sage leaf extract", "Sage oil",
                                 "Salicylic acid", "Sandalwood oil", "Sandalwood oil", "Saponary leaf extract",
                                 "Saponified coconut oil", "Saponified coconut oil", "Saponified olive oil",
                                 "Saponified olive oil", "Saponified palm oil", "Saponified sweet almond oil",
                                 "Sclerotium rolfssii gum", "Sea buckthorn extract", "Sea buckthorn fruit oil",
                                 "Sea Buckthorn oil", "Sea buckthorn seed oil", "Sea salt", "Sea water", "Sea water",
                                 "Seaweed extract", "Seaweed extract", "Sesame seed oil", "Shea Butter",
                                 "Shea butter extract", "Shea oil", "Sheep milk", "Silica", "Silk extract",
                                 "Silver nitrate", "Snail extract", "Sodium acetate", "Sodium benzoate",
                                 "Sodium bicarbonate", "Sodium chloride", "Sodium citrate", "Sodium dehydroacetate",
                                 "Sodium fluoride", "Sodium hyaluronate", "Sodium hydroxide", "Sodium laureth sulfate",
                                 "Sodium lauryl sulfate", "Sodium levulinate", "Sodium salicylate", "Sorbic acid",
                                 "Sorbitan stearate", "Sorbitol", "Soybean Oil", "Soybean seed extract",
                                 "Spearmint extract (Flower/Leaf/stem)", "Spearmint leaf oil", "Spearmint leaf oil",
                                 "Squalane", "Stearic acid", "Strawberry seed extract", "Sucrose", "Sugar cane extract",
                                 "Sunflower seed extract", "Sunflower seed oil", "Sunflower seed oil unsaponifiables",
                                 "Sunflower wax", "Sweet almond extract", "Sweet almond kernel oil", "Sweet almond oil",
                                 "Sweet almond oil", "Sweet almond oil", "Sweet Marjoram leaf oil", "Sweet orange oil",
                                 "Sweet Orange peel essential oil", "Sweet Potato extract", "Synthetic beeswax",
                                 "Synthetic Mica", "Synthetic wax", "Talc", "Tangerine peel oil", "Tapioca starch",
                                 "Tartaric acid", "Tasmanian Pepper Extract", "Tea Leaf extract", "Tea Leaf oil",
                                 "Tea seed oil", "Tea tree Leaf extract", "Tea tree leaf oil", "Tetrasodium EDTA",
                                 "Thyme extract", "Thyme leaf extract", "Tiare flower", "Tiare flower extract",
                                 "Tiger grass extract", "Tin oxide", "Tocopheryl acetate", "Triethanolamine",
                                 "Turmeric root extract", "Urea", "UV filter (Titanium Dioxide)", "Vanilla",
                                 "Vanilla extract", "Vanilla oil", "Vanillin", "Vaseline", "Vegetable oil",
                                 "Verbena Leaf Extract", "Vetiver extract", "Viper venom", "Vitamin A", "Vitamin B6",
                                 "Vitamin E", "Walnut shell powder", "Watermelon extract", "Watermelon seed oil",
                                 "Wheat germ oil", "White dye", "White dye", "White dye", "White dye", "White dye",
                                 "White dye", "White dye", "White dye", "White dye", "White dye (calcium carbonate)",
                                 "White dye (Kaolin)", "White dye (Titanium dioxide)", "White pigment (Zinc Oxide)",
                                 "White truffle extract", "White willow bark extract", "Wild chamomile flower",
                                 "Wild chamomile oil", "Wild mint extract", "Wild mint oil", "Wild Thyme extract",
                                 "Wine extract", "Wintergreen leaf oil", "Witch hazel extract",
                                 "Witch hazel leaf extract", "Witch hazel water", "Xanthan Gum", "Yellow dye",
                                 "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye",
                                 "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye",
                                 "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye",
                                 "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye", "Yellow dye (Iron oxide)",
                                 "Yellow Melilot flower extract", "Ylang Ylang flower oil",
                                 "Ylang-ylang flower extract", "Zinc gluconate", "Zinc oxide", "Zinc sulfate",
                                 "Alcohol", "Alfalfa Powder", "Alkanet Root Extract", "Allantoin", "Allantoin",
                                 "Almond Butter", "Almond Meal", "Almond Oil", "Almond Oil, Bitter",
                                 "Aloe ferox leaf extract", "Aloe Leaf Powder", "Aloe vera extract",
                                 "Aloe vera flower extract", "Aloe Vera Juice", "Aloe Vera Juice",
                                 "Aloe Vera Leaf extract", "Aloe Vera Leaf juice powder", "Aloe vera leaf powder",
                                 "Aloe Vera Leaf water", "Alpha-isomethyl ionone", "Aluminium oxide",
                                 "Aluminum chlorohydrate", "Aluminum hydroxide",
                                 "Anacardium Occidentale (Cashew) seed oil", "Anhydrous Lanolin", "Anise alcohol",
                                 "Anise Oil", "Annatto Powder", "Apricot Kernel Oil", "Arabic gum", "Argan extract",
                                 "Argan kernel oil", "Argan leaf extract", "Arginine", "Arnica", "Arnica Extract",
                                 "Arnica flower extract", "Arnica flower oil", "Arrowroot Powder", "Ascorbic acid",
                                 "Ascorbyl palmitate", "Atlas Cedarwood Oil", "Avocado", "Avocado Butter",
                                 "Avocado Oil", "Babassu Oil", "Baking Soda", "Balsam Fir Needle Oil",
                                 "Baobab leaf extract", "Basil Oil", "Bay Laurel Oil", "Beef Tallow", "Beeswax",
                                 "Beet Powder", "Bentonite Clay", "Bergamot Oil FCF", "BHA FCC", "BHT FCC",
                                 "Bicarbonate of Soda", "Black Pepper Oil", "Bladderwrack Extract", "Borax",
                                 "Boric Acid", "Brilliant blue FCF", "Brown Sugar", "Bulgarian Lavender Oil", "Butter",
                                 "Buttermilk", "Buttermilk Powder", "C12-15 Alkyl Benzoate", "Cajeput Oil",
                                 "Calcium Carbonate USP", "Calendula Extract", "Calendula Oil", "Camellia Oil",
                                 "Camphor", "Candelilla Wax", "Canola Oil", "Carbomer", "Carbopol", "Cardamom Oil",
                                 "Carnauba Wax", "Carnauba Wax", "Carrot Seed Oil", "Castor Oil USP", "Catnip Oil",
                                 "Celery extract", "Celery seed extract", "Cetyl Alcohol NF", "Chamomile Extract",
                                 "Chamomile Oil, Roman", "Chamomille flower water", "Chitosan",
                                 "Chromium Hydroxide Green", "Chromium Oxide Green", "Cinnamon Leaf Oil",
                                 "Citric Acid USP", "Citronella Oil", "Clary Sage Oil", "Clay China", "Clay, Bentonite",
                                 "Clove Blossom Oil", "Clove Bud Oil", "Cocoa Butter", "Coconut Milk", "Coconut Oil",
                                 "Coconut Oil, Fractionated", "Coconut Powder", "Comfrey Extract",
                                 "Comfrey Root Powder", "Coriander Seed Oil", "Corn Oil", "Cornmeal", "Cornstarch",
                                 "Covi-Ox T-50", "Cream", "Crisco Shortening (US)", "Cucumber Extract",
                                 "Cucumber Juice", "Cyclomethicone", "Denatured alcohol", "Dill extract", "Dimethicone",
                                 "Dimethiconol", "Dipropylene Glycol USP", "DL-Panthonol", "D-Panthenol", "Panthenol",
                                 "DPG", "Echinacea Extract", "EDTA, Disodium", "EDTA, Tetrasodium", "Egg",
                                 "Egg, Whole Dried", "Emu Oil", "Emulsifying Wax NF - Polawax", "Epsom Salt USP",
                                 "Essential Oil(s)", "Eucalyptus Oil", "Evening Primrose Oil", "Fir Needle Oil",
                                 "Flavour", "Fractionated Coconut Oil", "Fragrance Oil", "Frankincense Oil",
                                 "Fumed Silica", "Geranium Oil", "Germaben II", "Germall Plus", "Germall Plus, Liquid",
                                 "German Blue Chamomile Oil", "Ginger Oil", "Glitter, Irridescent", "Glycerin 99.5%",
                                 "Glyceryl Monosteareate", "Goat Butter", "Goat Milk", "Grapefruit Oil",
                                 "Grapeseed Oil", "Green Tea Extract", "Guar Gum", "Hazelnut Oil", "Helichrysum Oil",
                                 "Hemp Seed Oil", "Honey", "Honey Powder", "Horse chestnut seed extract",
                                 "Hydrolyzed Silk Protein", "Hydrous Lanolin", "Hyssop Oil", "IPM", "IPP",
                                 "Iron Oxide, Black", "Iron Oxide, Red", "Iron Oxide, Yellow", "Jasmine Absolute",
                                 "Jojoba Oil", "Juniper Berry Oil", "Kaolin Clay", "Kelp Powder", "Kiwi fruit extract",
                                 "Kiwi fruit extract", "Kiwi seed oil", "Kukui Nut Oil", "Kukui nut oil", "Lactic Acid",
                                 "Lactose", "Lanolin", "Lard", "Lavandin Oil", "Lavender Flower Powder",
                                 "Lavender Oil 40/42", "Lavender Oil, Bulgarian", "Lavender Oil, Spike", "Lecithin",
                                 "Lemon Balm Extract", "Lemon Balm Oil", "Lemon Eucalyptus Oil", "Lemon Oil",
                                 "Lemongrass Oil", "Lime Oil", "LiquaPar Optima", "Liquid Germall Plus",
                                 "Macadamia Nut Oil", "Malic Acid", "Mallow Extract", "Mango Butter",
                                 "Marshmallow root extract", "Marshmallow Root Powder", "May Chang Oil",
                                 "Meadowfoam Seed Oil", "Melissa Oil", "Methylcellulose", "Mica", "Milk", "Milk Powder",
                                 "Milk Powder, Skim", "Mineral Oil", "Mink Oil", "MSM", "Myrrh Oil", "Myrtle Oil",
                                 "Neroli Oil", "Nettle Extract", "Nettle Leaf Powder", "Niaouli Oil",
                                 "Oakmoss Absolute", "Oat kernel extract", "Oat kernel oil", "Oatmeal", "Olive Oil",
                                 "Onion extract", "Optiphen Plus", "Orange Flower Distillate", "Orange Oil, Bitter",
                                 "Orange Oil, Blood", "Orange Oil, Sweet", "Orange Peel Powder", "Oregano Oil",
                                 "Palm Kernel Flakes", "Palmarosa Oil", "Patchouli Oil", "Peanut Oil", "Peanut oil",
                                 "Peppermint Distillate", "Peppermint Oil", "Petitgrain Oil", "Petrolatum", "Phenonip",
                                 "Pineapple extract", "Polawax", "Polysorbate 20", "Polysorbate 60", "Polysorbate 80",
                                 "Polysorbate 85", "Poppyseed", "Potassium Sorbate", "Propylene Glycol",
                                 "Pumice Powder", "Ravensara Oil", "Red Clay", "Red dye", "Red dye", "Red dye",
                                 "Red dye", "Red Iron Oxide", "Rice Amino Acids", "Rice Bran Oil", "Rice Bran Wax",
                                 "Rice Powder", "Roman Chamomile Distillate", "Roman chamomile flower extract",
                                 "Roman Chamomile flower oil", "Roman Chamomile Oil", "Rose Absolute",
                                 "Rose Distillate", "Rose Geranium Oil", "Rose Otto Oil", "Rosehip Oil",
                                 "Rosehip Powder", "Rosemary Extract", "Rosewood Oil", "Rosewood oil", "Rosin",
                                 "Safflower Oil", "Sage Oil", "Salt", "Salt, Epsom", "Salt, Sea", "Sandalwood Oil",
                                 "Seaweed Extract", "Seaweed extract", "Seaweed extract", "Sesame Oil",
                                 "Shea Butter, Natural", "Shea Butter, Refined", "Silk Amino Acids", "Sodium alginate",
                                 "Sodium Benzoate", "Sodium Laureth Sulfate", "Sorbitan Oleate", "Sorbitan Stearate",
                                 "Sorbitol", "Spanish Rosemary Oil", "Spearmint Oil", "Spearmint Powder",
                                 "Spike Lavender Oil", "Spinach Powder", "Spruce Oil", "Squalane", "Squalene",
                                 "St. John's Wort Oil", "Stearic Acid", "Stearyl Alcohol", "Stevia Extract",
                                 "Stevia Leaf Powder", "Stevia Liquid Extract", "Sugar", "Sunflower Oil", "Suttocide A",
                                 "Sweet Birch Oil", "Sweet Fennel Oil", "Sweet Marjoram Oil", "Sweet Orange Oil SD",
                                 "Talc", "Tallow", "Tangerine Oil", "TEA", "Tea Tree Oil", "Tetrasodium EDTA",
                                 "Titanium Dioxide", "Ultramarine Blue", "Ultramarine Pink", "Ultramarine Violet",
                                 "Urea", "Valerian Root Oil", "Vanilla", "Vetiver Oil", "Vinegar", "Vitamin A",
                                 "Vitamin E - Alpha Tocopherol", "Vitamin E Acetate", "Walnut Oil", "Water", "Water",
                                 "Wheatgerm Oil", "White Camphor Oil", "White Kaolin Clay", "Wintergreen, Oil of",
                                 "Witch Hazel Distillate", "Xanthan Gum", "Yarrow Extract", "Yarrow extract",
                                 "Yarrow Oil", "Yellow dye", "Yellow dye", "Ylang Ylang Oil", "Ylang Ylang Oil Extra",
                                 "Zinc Oxide USP", "Coconut", "Aamla", "Aamla", "Avocado", "Acacia Peptide", "Acai",
                                 "Acai", "Acai Oil", "Acmella Oleracea", "Acrylate Copolymer", "Agave", "Agave",
                                 "Arginine", "Argan", "Allantoin", "Almond", "Almond", "Almond", "Almond", "Almond",
                                 "Alnut", "Aloe Vera", "Aloe Vera", "Aloe Vera", "Aloe Vera", "Aloe Vera", "Aloe Vera",
                                 "Amber", "Amino Acids", "Aamla", "Aamla", "Aamla", "Amphoteric Surfactants",
                                 "Angelica", "Angelica", "Annatto Seed Oil", "Ant Oil", "Antioxidants", "Antioxidants",
                                 "Antioxidants", "Apple", "Apple", "Apricot", "Water", "Argan", "Argan", "Argan",
                                 "Argan", "Argan", "Argan", "Argan", "Argan", "Aritha", "Arnica",
                                 "Artemisia Capillaris", "Ayurvedic", "Avocado", "Avocado", "Avocado", "Avocado",
                                 "Avobenzone", "Avocado", "Avocado", "Avocado", "Avocado", "Ayurvedic", "Ayurvedic",
                                 "Ayurvedic", "Babassu", "Badam", "Black Orchid", "Bamboo", "Bamboo",
                                 "Bambusa Vulgaris", "Banana", "Banyan", "Baobab", "Basil", "Basil", "Batana", "Batana",
                                 "Beeswax", "Beetroot", "Benzoyl Peroxide", "Bergamot", "Berry", "Berry", "Berry",
                                 "Beeswax", "Beta Carotene", "Bha", "Bhringaraj", "Bhringaraj", "Bhringaraj",
                                 "Bhringaraj", "Bhringaraj", "Bhringaraj", "Biotin", "Bisabolol", "Castor", "Cumin",
                                 "Cumin", "Black Seed", "Black Seed", "Black Seed", "Black Curant", "Black Seed",
                                 "Blueberry", "Blueberry", "Boric Acid", "Bourbon", "Brahmi", "Brazil Nut",
                                 "Bhringaraj", "Bhringaraj", "Bhringaraj", "Bhringaraj", "Bhringaraj", "Bhringaraj",
                                 "Bhringaraj", "Bhringaraj", "Brown Seaweed", "Broyne", "Bsitosterol", "Babassu",
                                 "Burdock Root", "Castor", "Cactus", "Caffeine", "Calendula", "Calendula", "Calendula",
                                 "Camellia", "Camellia", "Camellia", "Camellia", "Camphor", "Candy", "Capixyl",
                                 "Cardamom", "Carnauba Wax", "Carotenoids", "Carrot", "Carrot", "Carrot", "Carrot",
                                 "Carrot", "Carrot", "Castor", "Castor", "Carrot", "Castor", "Cedar", "Cedarwood",
                                 "Cell Ox Shield", "Cell Ox Shield", "Centella", "Ceramide", "Ceramide", "Ceramide",
                                 "Cermaide", "Ceramide", "Cetrimonium Chloride", "Cetyl Alcohol", "Chaga Mushroom",
                                 "Chamomile", "Chamomile", "Chamomile", "Charcoal", "Chebe", "Cherry", "Cherry", "Chia",
                                 "Chicory Root", "Chocolate", "Chrysanthemum", "Cica", "Ciderwood", "Cinammon",
                                 "Cinnamon Leaf", "Citric Acid", "Citric Acid", "Citrus", "Clove", "Cobra Oil",
                                 "Cocamidopropyl Betaine", "Coconut", "Coconut", "Cocoa ", "Cocoa ", "Coco Glucoside",
                                 "Cocoa ", "Cocoa", "Cocoa Butter", "Cocoa Peptides", "Cocoa Butter", "Coco Glucoside",
                                 "Cocoa Butter", "Coconut", "Coconut", "Coconut", "Coconut", "Coconut", "Coconut",
                                 "Coffee", "Coffee", "Collagen", "Conditioning", "Copolyol", "Copper", "Corn", "Cotton",
                                 "Cotton", "Cranberry", "Cucumber", "Curry Leaf", "Curry Leaf", "Cyclomethicone",
                                 "Cyperus", "Cyperus", "Davana Blossom", "Diazolidinyl Urea", "Dimethicone",
                                 "Dioscorea Japonica Root", "Draksha", "Espom Salt", "Erythitol", "Ethylhexylglycerin",
                                 "eucalyptus", "Primrose Oil", "Ayurvedic", "Olive", "Facial Tissue", "Fatty Acids",
                                 "Fennel Seed Oil", "Fenugreek", "Fenugreek", "Fig", "Fig", "Finrangpani", "Fish Oil",
                                 "Flax", "Flax", "Flax", "Floral", "Floral", "Floral", "Frankincense", "Fresh Roses",
                                 "Strawberry", "Fruit Oil", "Gandha Kachura", "Garlic", "Geranium", "Ghergir",
                                 "Gingelly Oil", "Ginger", "Ginger", "Ginseng", "Ginseng", "Glycerin", "Glycerin",
                                 "Glyceryl Glucoside", "Glyceryl Oleate", "Glycolic Acid", "Glycyrrhetinic Acid",
                                 "Glycyrrhetinic Acid", "Glycerin", "Goji Berry", "Grape", "Grapeseed", "Grapeseed",
                                 "grapefruit", "Grapeseed", "Grapeseed", "Green Tea", "Green Tea", "Green Tea",
                                 "Green Tea", "Guava", "Hanzal Oil", "Hashish Oil", "Hectorite Clay",
                                 "Helianthus Annuus Seed Oil", "Helioplex", "Hemp", "Hemp", "Hemp", "Henna",
                                 "Herb AC Complex", "Ayurvedic", "Ayurvedic", "Hibiscus", "Hibsucis", "Hibiscus",
                                 "Hibiscus", "Homosalate", "Hibiscus", "Honey", "Honey", "Honey Suckle Jasmine",
                                 "Horsetail", "Horsetail", "Hyalurnoic Acid", "hyaluronic acid", "Hyalurnoic Acid",
                                 "Hydrocolloid", "Hydrocortisone", "Hydrocortisone", "Hyaluronic Acid", "Intra Cyclane",
                                 "Castor", "Castor", "Japa", "Jappuspa", "Jasmine", "Jasmine", "Jasmine",
                                 "Jeju Fermentation Oil", "Jojoba", "Jojoba", "Jojoba", "Jojoba", "Jojoba",
                                 "Juicy Peach", "Kakadu Plum", "Kale", "Kalonji", "Karipatta", "Karkar Oil", "Kelp",
                                 "Keratin", "Keratin", "Kokum ", "Kokum ", "Konjac", "Kukui", "Kukui",
                                 "Kumkumadi Taila", "L Cartinine", "Lactic Acid", "Lactobac", "Laminaria", "Laminaria",
                                 "Laminaria", "Lanolin", "Lao Benzion", "Lauroyl Sarcosinate", "Lavender", "Lavender",
                                 "Lavender", "Lavender", "Lavender", "Lemon", "Lemongrass", "Lemongrass", "Lha",
                                 "Licochalcone A", "Licorice", "Ligob Berry", "Lilac", "Lilochaloconea", "Lily", "Lily",
                                 "Lime", "Lemon", "Linseed", "Linseed", "Lolive", "Lotus", "Lotus", "Macadamia",
                                 "Macadamia", "Macadamia", "Macadamia", "Macadamia", "Macadamia", "Macadamia", "Mafura",
                                 "Mahabhringraj", "Malakangani Extracts", "Mandelic Acid", "Mango", "Mango", "Mango",
                                 "Mango", "Manketti Oil", "Manuka", "Maracuja", "Marigold", "Marine Algae",
                                 "Marine Algae", "Marula", "Marula", "Marula", "Aamla", "Marula", "Mayonnaise",
                                 "Meadowfoal Oil", "Meadowfoam", "Melatonin", "Menthol", "Menthyl Lactate",
                                 "Mesembryanthemum Crystallinum", "Mexoryl", "Mica", "Micellar Cleansing Water",
                                 "Micellar Cleansing Water", "Milk", "Mineral Oil", "Minerals", "Mongongo Oil",
                                 "Moringa", "Moringa", "Moringa", "Moringa", "Argan", "Argan", "Argan", "Argan",
                                 "Argan", "Mugwort", "Mulethi", "Murumuru", "Murumuru", "Murumuru", "Murumuru",
                                 "Murumuru", "Musk", "Mustard", "Tea Tree", "Neelbhrigandi", "Neelbhrigandi", "Neem",
                                 "Neem", "Neroli Oil", "Niacinamide", "Oak", "Oat", "Oat", "Oat", "Oat", "Oat",
                                 "Ocean Salted Sage", "Octinoxate", "Octisalate", "Octocrylene", "Octyldodecanol",
                                 "Coco", "Oil Pearls", "Olive", "Oleic Acid", "Olive ", "Olive", "Olive", "Olive",
                                 "Omega 3", "Omega 6", "Omega 9", "Onion", "Onion", "Onion", "Orange", "Aloe Vera",
                                 "Orchid", "Orchid", "Orchid", "Oregano", "Beeswax", "Oud/Oudh Accord",
                                 "Oud/Oudh Accord", "Oxynex St", "Palm Ash", "Palo Santo", "Ginseng", "Panthenol",
                                 "Panthenol", "Papaya", "Papaya", "Papaya", "papyrus", "Paraffin", "Parsol Tx",
                                 "Passionfruit", "Passionfruit", "Pataua", "Patchoulli", "Patchoulli", "Papaya",
                                 "Peach", "Peanut", "Pear", "Peony", "Peppermint", "Mint", "Peptide", "Peptide",
                                 "Pequi", "Perlite", "Persea", "Petrolatum", "Petroleum Jelly", "Phenol",
                                 "Phyto Phanere", "Phytolacca", "Pinus Pinaster Bark", "Piper Nigrum", "Pippali",
                                 "Pistachio", "Plantain Peel Extract", "Polyisobutene", "Pomegranate", "Powerfruit",
                                 "Oat", "Pear", "Primrose", "Vitamin B5", "Probiotics", "Proteins", "Vitamin A",
                                 "Pueraria Lobata Root", "Pulmeria", "Pumpkin", "Pumpkin", "Coconut", "Purifying Clay",
                                 "Quinoa", "Radix", "Radix Salviae Militiorhizae", "Raspberry", "Raspberry",
                                 "Shea Butter", "Red Algae", "Red Dahlia", "Onion", "Pimento", "Retinol", "Rice",
                                 "Rice", "Rice", "Rice", "Rice", "Rice", "Rice", "Rose", "Rose", "Rose", "Rosehip",
                                 "Rosehip", "Rosehip", "Rosehip", "Rosemary", "Rosemary", "Rosemary", "Rosemary",
                                 "Rose", "Roucou", "Saccharide Isomerate", "Safflower", "Safflower", "Safflower",
                                 "Saffron", "Salicylic Acid", "Salicylic Acid", "Salmon ", "Sandalwood", "Sandalwood",
                                 "Satin", "Sea Kelp", "Sea Salt", "Silica", "Sesa", "Sesame", "Sesame", "Sesame",
                                 "Shea Butter", "shea butter", "Shea Oil", "Shikakai", "Shiso", "Silica", "Silica",
                                 "Silk", "Silk", "Silymarin", "Smoothens", "Snail Oil", "Snake Oil", "Snake Oil",
                                 "Soap Wort", "Sodium", "Sodium Citrate", "Sodium Edta", "Sodium Hyaluronate",
                                 "Soft Rose", "Soy", "Soyabean", "Soyabean", "Soyabean", "Soyabean", "Soyabean",
                                 "Spearmint", "SPF", "SPF", "Spicy-Citrus Elmi", "Squalene", "Stearyl Alcohol",
                                 "Stemonae", "Stone", "StrawBerry", "Sugar", "Sulphur", "Sundrops", "Sunflower",
                                 "Sunflower", "Sunflower", "Sunflower", "Sweet Almond", "Sweet Almond", "Sweet Almond",
                                 "Sweet Cherry", "Tahitian Monoi", "Tamarind", "Tannic Acid", "Taurine", "Tea Tree Oil",
                                 "Tea Tree Oil", "Tea Tree Oil", "Tea Tree Oil", "Thiamidol", "Thyme", "Thyme",
                                 "Thymoquinone", "Tiare", "Vanilla", "Til", "Titanium Dioxide", "Tocopherol",
                                 "Tocopherol", "Tocopherol", "Tocopheryl", "Tomato", "Tonka Bean", "Trehalose",
                                 "Tremella Fuciformis", "Triethanolamine", "Coconut", "Basil", "Tural Redwood",
                                 "Turmeric", "Turmeric", "Urea", "Vanilla", "Vanilla", "Jelly", "Vegetable Oil",
                                 "Vetiver", "Vitamins", "Vigna Radiata", "Vitamin A", "Vitamin B", "Vitamin B3",
                                 "Vitamin B5", "Vitamin C", "Vitamins", "Vitamin D", "Vitamin E", "Vitamin E",
                                 "Vitamin F", "Vitamins", "Vitamins", "Vitamin A", "Vitamin C", "Walnut", "Walnut",
                                 "Water", "Water", "Water Mint", "Watermelon", "Wheat", "Wheat", "Wheat",
                                 "Wheat Germ Oil", "White Thyme", "White Cedar", "White Orange", "Petroleum",
                                 "White Tea", "Wild Berries", "Wild Geranium", "Witch Hazel", "Woody", "Ylang Ylang",
                                 "Ylang Ylang", "Yoghurt", "Yumlu Seed Extract", "Yuzu And Lemon", "Zinc", "Zinc Oxide",
                                 "Ginger"]
        # @title
        self.benefit = ["thermal protection", "Bouncy", "Maternity Care", "Anti Dryness", "Fast Absorbing", "Absorbant",
                        "Acne Control", "Acne Control", "Acne Control", "Acne Control", "Acne Control", "Shine",
                        "Healing", "Anti-Hairfall", "Hair Growth", "Nourishment", "Moisturization", "Hydration",
                        "Anti Ageing", "Anti Chafing", "Anti Itch", "Acne Control", "Anti Ageing", "Anti Ageing",
                        "Anti Ageing", "Anti Bacterial", "Anti Chafing", "Anti Chafing", "Anti Chap", "Anti Chap",
                        "Anti Dandruff", "Anti Dryness", "Anti Eye Sting", "Anti Fade", "Frizz Control",
                        "Anti Ageing""Anti Itch", "Anti Itch", "Lice Protection", "Anti Microbial", "Anti Shrinkage",
                        "Anti Ageing", "Acne Control", "Anti Ageing", "Anti Ageing", "Anti Ageing",
                        "Breakage Protection", "Anti Dandruff", "Anti Dryness", "Frizz Control", "Anti Fungal",
                        "Anti Inflammatory", "Anti Itch", "Treatment", "Fragrance", "Aroma Therapy", "Balance",
                        "Balance", "Balance", "Beautification", "Beautification", "Beautification", "Beautification",
                        "Blood Circulation", "Blue Light Protection", "Immunity Boosting", "Shine", "Bounce",
                        "Breakage Protection", "Breakage Protection", "Brightening", "Brightening", "Brightening",
                        "Brightening", "Brilliance", "Brittleness Protection", "UV Protection",
                        "Broad Spectrum UV Protection", "Bounce", "Calming", "Calming", "Calming", "Care", "Care",
                        "Cleansing", "Cleansing", "Cleansing", "Cleansing", "Cleansing", "Cleansing", "Cleansing",
                        "Color Protection", "Color Protection", "Comfort", "Comfort", "Comfort", "Comfort",
                        "Conditioning", "Conditioning", "Conditioning", "Conditioning", "Conditioning", "Conditioning",
                        "Anti Dandruff", "Frizz Control", "Anti Itch", "Cooling", "Cooling", "Cooling",
                        "Curl Enhancing", "Curl Enhancing", "Damage Protection", "Damage Protection",
                        "Damage Protection", "Damage Protection", "Anti Dandruff", "Anti Dandruff", "Anti Dandruff",
                        "Anti Dandruff", "Deep Cleanse", "Deep Cleanse", "Deep Cleanse", "Conditioning", "Nourishment",
                        "Defense", "Definition", "Enhancement", "Frizz Control", "Frizz Control", "Delicate",
                        "Thickening", "Volumizing", "De-pigmentation", "Detangling", "Detangling", "Detangling",
                        "Detangling", "Detoxification", "Detoxification", "Detoxification", "Dewy Skin", "Anti Dryness",
                        "Anti Dryness", "Anti Dryness", "Anti Dryness", "Anti Dryness", "Anti Dryness", "Anti Dryness",
                        "Anti Dryness", "Anti Dryness", "Durable", "Detangling", "Easy To Use", "Easy To Use",
                        "Easy To Use", "Eczema Protection", "Eczema Protection", "Sunburn Protection", "Bounce",
                        "Oil Control", "Frizz Control", "Breakout Protection", "Energizing", "Energizing", "Enrichment",
                        "Enrichment", "Even Skin Tones", "Even Skin Tones", "Exfoliation", "Exfoliation", "Exfoliation",
                        "Exfoliation", "Exfoliation", "Dark Spot Reduction", "Fast Absorbing", "Fast Drying",
                        "Anti Dandruff", "Odor Control", "Anti Ageing", "Anti Ageing", "Firming", "Firming",
                        "Curl Protection", "Frizz Control", "Moisturization", "Hydration", "Hold", "Freshness",
                        "Freshness", "Freshness", "Frizz Control", "Frizz Control", "Frizz Control", "Frizz Control",
                        "Frizz Control", "Frizz Control", "Frizz Control", "Frizz Control", "Frizz Control", "Gentle",
                        "Gentle", "Gentle", "Gloss", "Glow", "Shine", "Good Results", "Heart Health", "Anti Ageing",
                        "Anti Ageing", "Anti-Hairfall", "Hair Growth", "Damage Protection", "Anti Ageing",
                        "Damage Protection", "Smoothness", "curl", "Volumizing", "Nourishment", "Healing", "Healing",
                        "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Healthy Skin",
                        "Nourishment", "Heat Protection", "Heat Resistance", "Odor Control", "Bone Strength",
                        "Cholestrol Management", "Absorbant", "Hold", "Therapy", "Humidity Protection",
                        "Moisturization", "Hydration", "Hygenic Packaging", "Hygenic Packaging", "Hygenic Packaging",
                        "Hyperpigmentation", "Hyperpigmentation", "Cooling", "Immediate Relief", "Blood Circulation",
                        "Blood Circulation", "Dryness Improvement", "Metabolism Improvement", "Thickening",
                        "Volumizing", "Blood Microcirculation Improvement", "Metabolism Improvement",
                        "Inflammation Protection", "Instant Relief", "Instant Relief", "Invigoration", "Digestion",
                        "Invisible", "Invisible", "Itch Control", "Itch Control", "Itch Control", "Warmth", "Hold",
                        "Kissable", "Breakage Protection", "Flake Control", "Frizz Control", "Anti Irritation",
                        "Lifting", "Nourishment", "Lightweight", "Lightweight", "Lightweight", "Lightweight",
                        "Lightweight", "Lightweight", "Lightweight", "Moisture Lock", "Long Lasting", "Long Lasting",
                        "Long Lasting", "Shine", "Shine", "Shine", "Detangling", "Strength", "Softness", "Thickening",
                        "Volumizing", "Manageability", "Matte Finish", "Frizz Control", "Moisturization", "Hydration",
                        "Moisturization", "Hydration", "Muscle Relaxation", "No Clogging Pores", "Anti Dryness",
                        "Anti Eye Sting", "No Residue", "No Shine", "No White Cast", "Non Greasy", "Anti Irritation",
                        "Non Sticky", "Non Greasy", "Non Greasy", "Non Sticky", "Nourishment", "Nourishment",
                        "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment",
                        "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment",
                        "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment", "Nourishment",
                        "Nourishment", "Nourishment", "Oil Absorbing", "Oil Control", "Oil Control", "Pain Relief",
                        "pH Balance", "Anti Pigmentation", "Fragrance", "Fragrance", "Plump", "Plump",
                        "Pollution Control", "Pore Treatement", "Cleansing", "Anti Ageing", "Anti Ageing",
                        "Anti Ageing", "Maternity Care", "Skin Preservation", "Breakage Protection",
                        "Disease Prevention", "Anti Dryness", "Anti Ageing", "Breakage Protection", "Anti Chafing",
                        "Anti Dandruff", "Anti Dryness", "Anti Dryness", "Flake Control", "Anti Ageing", "Anti Dryness",
                        "Breakage Protection", "Anti Ageing", "Sunburn Prevention", "Sunburn Prevention",
                        "Healthy Skin", "Promotes", "Healing", "Nourishment", "Nourishment", "Nourishment",
                        "Healthy Skin", "Damage Protection", "Damage Protection", "Damage Protection",
                        "Damage Protection", "Damage Protection", "Anti Dryness", "Protection From Dehydration",
                        "Anti Dryness", "Rough Lip Protection", "Damage Protection", "Shine", "Purification",
                        "Purification", "Fast Absorbing", "Fast Absorbing", "Radiance", "Radiance", "Rebuilding",
                        "Rejuvination", "Scaling Reduction", "Blemish Reduction", "Anti Dandruff", "Frizz Control",
                        "Itch Control", "Itch Control", "Breakage Protection", "Anti Dandruff", "Dark Spot Reduction",
                        "Flake Control", "Frizz Control", "Breakage Protection", "Muscle Relaxation",
                        "Reactivity Reduction", "Scaling Reduction", "Scratch Reduction", "Anti Ageing", "Refreshing",
                        "Refreshing", "Refreshing", "Refreshing", "Regeneration", "Regeneration", "Rejuvination",
                        "Rejuvination", "Rejuvination", "Rejuvination", "Rejuvination", "Rejuvination", "Rejuvination",
                        "Relaxation", "Relaxation", "Relaxation", "Relaxation", "Relief", "Anti Dandruff",
                        "Anti Dryness", "Relief", "Digestion", "Anti Dryness", "Itch Control", "Tension Relief",
                        "Anti Dryness", "Remove", "Anti Dandruff", "Anti Dandruff", "Dead Skin Removal",
                        "Anti Dandruff", "Renewal", "Renewal", "Renewal", "Damage Repair", "Damage Repair",
                        "Damage Repair", "Damage Repair", "Damage Repair", "Damage Repair", "Damage Repair",
                        "Damage Repair", "Damage Repair", "Replenishment", "Replenishment", "Replenishment",
                        "Replenishment", "No Residue", "No Residue", "Resistance", "Restoration", "Restoration",
                        "Restoration", "Restoration", "Restoration", "Restoration", "Restoration", "Restoration",
                        "Revitalization", "Revitalization", "Revitalization", "Revitalization", "Revitalization",
                        "Revitalization", "Revival", "Revival", "Revival", "Richness", "Frizz Control",
                        "Roughness Relief", "Protection", "Protection", "Protection", "Sand Resistance", "Anti Itch",
                        "Anti Itch", "Treatment", "Scar Removal", "Scar Removal", "Sensitivity", "Sensitivity",
                        "Curl Enhancing", "Shimmer", "Shine", "Shine", "Shine", "Shine", "Shine", "Shine",
                        "Pain Relief", "Strength", "Silky Hair", "Silky Hair", "Silky Hair", "Silky Hair", "Silky Hair",
                        "Silky Hair", "Skin Cancer Protection", "Skin Cell Renewal", "Damage Protection", "Silky Hair",
                        "Anti Irritation", "Silky Hair", "Damage Protection", "Damage Protection", "Skin Care",
                        "Fragrance", "Smoothness", "Smoothness", "Smoothness", "Smoothness", "Smoothness", "Smoothness",
                        "Smoothness", "Smoothness", "Smoothness", "Smoothness", "Smoothness", "Smoothness",
                        "Smoothness", "Smoothness", "Smoothness", "Softness", "Softness", "Softness", "Softness",
                        "Softness", "Softness", "Softness", "Softness", "Softness", "Softness", "Soothing", "Soothing",
                        "Soothing", "Soothing", "Soothing", "Soothing", "Soothing", "Soothing", "Soothing", "Soothing",
                        "Soothing", "Soothing", "Soothing", "Split End Treatment", "Split End Treatment",
                        "Split End Treatment", "Strength", "Sting Free", "Strength", "Strength", "Strength", "Strength",
                        "Strength", "Strength", "Strength", "Strength", "Strength", "Strength", "Strength", "Strength",
                        "Maternity Care", "Strength", "Strength", "Strength", "Strength", "Strength", "Strength",
                        "Strength", "Strength", "Sun Protection", "Sun Protection", "UV Protection", "Suppleness",
                        "Suppleness", "Support", "Support", "Water And Sweat Resistance", "Tackling", "Frizz Control",
                        "Tan Protection", "Tear Free", "Tightening", "Tightening", "Tint", "Toning", "Toning",
                        "Travel Friendly", "Treatment", "Treatment", "Treatment", "Anti Dandruff", "Treatment",
                        "Unclog Pores", "Unclog Pores", "Velvety Finish", "Vitalization", "Water And Sweat Resistance",
                        "Water And Sweat Resistance", "Water And Sweat Resistance", "Water And Sweat Resistance",
                        "Weight Loss", "Lightweight", "Anti Ageing", "Yeast Infection Protection"]

        self.ingredient_match = list(dict.fromkeys(self.ingredient_match))
        self.benefit = list(dict.fromkeys(self.benefit))

    ##############################################
    def get_bci(self, string):
        output_text = self.remove_joining_elements(string)

        claimsI, string = self.regex_matching(self.claims, output_text)

        input_text = string
        string = self.remove_specific_words(string)

        result, ingre = self.find_words_after_no_or_free_of(input_text)
        for i in result:
            claimsI.append(i)

        ingredient = self.ingredients(ingre, self.ingredient_match)
        ingredient = list(dict.fromkeys(ingredient))

        ingre = self.remove_specific_words(ingre)

        benefitsF = []

        benefitsF, ingre = self.regex_matching(self.benefit, ingre)
        benef = ingre.split()
        for i in benef:
            k = ps.stem(i)
            if len(k) > 3:
                j = self.find_superset(k, self.benefit)
                if j == None:
                    pass
                elif self.start_or_end(j, k):
                    benefitsF.append(j)

        benefitsF = list(dict.fromkeys(benefitsF))
        claimsI = list(dict.fromkeys(claimsI))
        ingredient = list(dict.fromkeys(ingredient))

        final_array = [benefitsF] + [claimsI] + [ingredient]
        return (final_array)

    ####################################################################################################################################

    def listToString(self, s):

        # initialize an empty string
        str1 = ""

        # traverse in the string
        for ele in s:
            str1 += ele

        # return string
        return str1

    def find_subsets_in_array(self, array, user_input):
        # Convert user input to lowercase
        user_input_lower = user_input.lower()

        # Iterate through each word in the array
        for word in array:
            # Convert the word to lowercase
            word_lower = word.lower()

            # Check if the user input is a proper subset of the current word
            if set(user_input_lower).issubset(word_lower) and set(user_input_lower) != set(word_lower):
                # print(f'User input "{user_input}" is a proper subset of "{word}".')
                return word

    def find_superset(self, test_str, str_array):
        for i in str_array:
            if test_str.lower() in i.lower():
                return i

        return None

    def start_or_end(self, i, j):
        return i.lower().find(j.lower()) == 0

    def delete_word_with_substring(self, text, substring):
        # Build a regular expression to match words containing the substring
        pattern = re.compile(r'\b\w*{}\w*\b'.format(re.escape(substring)), re.IGNORECASE)

        # Replace matching words with an empty string
        result = pattern.sub('', text)

        return result

    def remove_specific_words(self, input_string):
        words_to_remove = ['a', 'an', 'the', 'this', 'they', 'are', 'were', 'no', 'free', 'oil', 'control', 'care',
                           'friendly', 'proven', 'recommended', 'rated', 'certified', 'packaging', 'produced',
                           'sourced', 'finish']

        # Create a regular expression pattern for the words to remove
        pattern = r'\b(?:' + '|'.join(map(re.escape, words_to_remove)) + r')\b'

        # Use re.sub to replace occurrences of the words with an empty string
        result_string = re.sub(pattern, '', input_string, flags=re.IGNORECASE)

        # Remove extra spaces
        result_string = ' '.join(result_string.split())

        return result_string

        # here it starts

    # for claims, put your input in input_text

    def remove_joining_elements(self, input_string):
        # Define a regular expression pattern for joining elements
        pattern = r'\b(and|but|or)\b'  # Add more conjunctions or characters as needed
        # Use re.sub to replace the matching patterns with a space
        result_string = re.sub(pattern, ' ', input_string)
        result_string = re.sub(",", "", result_string)
        result_string = re.sub("-", " ", result_string)
        result_string = re.sub("&", "", result_string)
        # Remove extra spaces
        result_string = ' '.join(result_string.split())

        return result_string

        # claims as it is find

    def regex_matching(self, array, user_input):
        # Convert all array elements to lowercase
        lowercase_array = [re.escape(s.lower()) for s in array]

        # Replace hyphens with spaces in the user input
        user_input_processed = re.sub(r'-', ' ', user_input.lower())

        # Create a regular expression pattern to match any term in the array
        pattern = re.compile(fr'\b(?:{"|".join(lowercase_array)})', re.IGNORECASE)

        # Find all matches in the processed user input
        matches = re.findall(pattern, user_input_processed)

        # Remove matched substrings from the input
        unmatched_substring = pattern.sub('', user_input_processed).strip()

        # Create the final output string with line breaks after each matched substring
        output_string = '\n'.join(matches)

        # Return the list of matched substrings and the user input without matches
        return list(set(matches)), unmatched_substring

    def find_words_after_no_or_free_of(self, text):
        # Define a regular expression pattern
        pattern = r'(?:no|without)\s+(\w+)|(\w+)\s+free'

        # Use re.findall to find all matches
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        matchesF = []
        result_text = text
        matches = [match[0] or match[1] for match in matches]

        for i in matches:
            k = ps.stem(i)
            j = self.find_superset(k, self.claims)
            if j == None:
                pass
            else:
                print(i, "-", j)
                matchesF.append(j)
                pattern = re.compile(r'\b\w*{}\w*\b'.format(re.escape(i)), re.IGNORECASE)
                result_text = re.sub(pattern, '', result_text)

        result_text = re.sub('  ', ' ', result_text)
        return matchesF, result_text

    # Ingredients here!

    def ingredients(self, user_input, string_array):
        matching_substrings = []

        for pattern in string_array:
            # Using re.escape to handle special characters in the pattern
            pattern_regex = re.compile(fr"\b{re.escape(pattern)}", re.IGNORECASE)

            # Find all occurrences of the pattern in the user input
            matches = re.findall(pattern_regex, user_input)

            # Add matching substrings to the result list
            matching_substrings.extend(matches)

        return matching_substrings

    def process_and_remove_duplicates(self, string_array):
        # Convert all strings to lowercase
        lowercase_strings = [s.lower() for s in string_array]

        # Remove duplicates while preserving the order
        unique_strings = list(dict.fromkeys(lowercase_strings))

        return unique_strings
