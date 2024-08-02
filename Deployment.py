import pandas as pd
import pickle 
import streamlit as st

# Load the pre-trained encoder and model
preprocessor = pickle.load(open('ML/Encoder/encoder.pkl','rb'))
model = pickle.load(open('ML/Model/model.pkl','rb'))

# Mapping for cleaning up user inputs
clean_imputs = {
    "As new": "AS_NEW",
    "Good": "GOOD",
    "Just Renovated": "JUST_RENOVATED",
    "To Be Done Up": "TO_BE_DONE_UP",
    "To Renovate": "TO_RENOVATE",
    "To Restore": "TO_RESTORE",
    "House": "House",
    "Villa": "Villa",
    "Town House": "Town_House",
    "Apartment Block": "Apartment_Block",
    "Mixed Use Building": "Mixed_Use_Building",
    "Bungalow": "Bungalow",
    "Mansion": "Mansion",
    "Exceptional Property": "Exceptional_Property",
    "Country Cottage": "Country_Cottage",
    "Chalet": "Chalet",
    "Manor": "Manor_House",
    "Other Property": "Other_Property",
    "Farmhouse": "Farmhouse",
    "Apartment": "Apartment",
    "Ground Floor": "Ground_Floor",
    "Duplex": "Duplex",
    "Flat Studio": "Flat_Studio",
    "Penthouse": "Penthouse",
    "Service Flat": "Service_Flat",
    "Loft": "Loft",
    "Kot": "Kot",
    "Triplex": "Triplex",
    "Not Installed": "NOT_INSTALLED",
    "Semi Equipped": "SEMI_EQUIPPED",
    "Installed": "INSTALLED",
    "USA Installed": "USA_INSTALLED",
    "USA Hyper Equipped": "USA_HYPER_EQUIPPED",
    "Recognized Flood Zone":"RECOGNIZED_FLOOD_ZONE",
    "Possible Flood Zone":"POSSIBLE_FLOOD_ZONE",
    "Not in a flood zone": "NON_FLOOD_ZONE",
    "None of the above":None}

# Set up the Streamlit app
st.set_page_config(page_title="Real Estate Prediction Machine", page_icon='house')
st.title('🏠 Real Estate Price Prediction Machine 🏠')
st.header("Welcome to my prediction machine!")

st.write("You can find the source code and more infos on my github: [Click here](https://github.com/benozfirat/immo_eliza)")
st.divider()

st.write("1. Enter the property details below. \n",
         "2. Click on the Predict button to get the estimated price.\n")

st.image("https://miro.medium.com/v2/resize:fit:1200/0*NCO1DF14J42HEQWR.jpg", use_column_width=True)

st.divider()

st.header("Type 🏷️")

# Radio button for selecting type of sale
TypeOfSale = st.radio("Type of Product:",["Sale","Rent"])
if TypeOfSale == "Sale":
    TypeOfSale = "residential_sale"
else:
    TypeOfSale = "residential_monthly_rent"

# Radio button for selecting type of property
TypeOfProperty = st.radio("Type of Property:", ["House","Appartment"])
if TypeOfProperty == "House":
    TypeOfProperty = 0
    # Dropdown for selecting subtype of property
    SubtypeOfProperty = st.selectbox('Subtype:', ("House","Villa","Town House","Apartment Block","Mixed Use Building","Bungalow","Mansion","Exceptional Property","Country Cottage","Chalet","Manor","Farmhouse","Other Property"))
    SubtypeOfProperty = clean_imputs[SubtypeOfProperty]
else:
    TypeOfProperty = 1
    # Dropdown for selecting subtype of property
    SubtypeOfProperty = st.selectbox('Subtype:', ('Apartment','Apartment Block', 'Ground Floor', 'Duplex', 'Flat Studio', 'Penthouse', 'Service Flat', 'Loft', 'Kot', 'Triplex'))
    SubtypeOfProperty = clean_imputs[SubtypeOfProperty]

st.divider()

st.header("Localisation 📍")

# Radio button for selecting region
Region = st.radio("Region:",["Brussels","Flanders","Wallonie"], index=2)

# Dropdown for selecting province
Province = st.selectbox("Province",("Antwerp","Brussels","East Flanders","Flemish Brabant","Hainaut",
                                    "Limburg","Liège","Luxembourg","Namur","Walloon Brabant","West Flanders"),index=6)

# Dropdown for selecting district
District = st.selectbox("District:",("Aalst","Antwerp","Arlon","Ath","Bastogne","Brugge","Brussels",
                                    "Charleroi","Dendermonde","Diksmuide","Dinant","Eeklo","Gent",
                                    "Halle-Vilvoorde","Hasselt","Huy","Ieper","Kortrijk","Leuven",
                                    "Liège","Maaseik","Marche-en-Famenne","Mechelen","Mons","Mouscron",
                                    "Namur","Neufchâteau","Nivelles","Oostend","Oudenaarde","Philippeville",
                                    "Roeselare","Sint-Niklaas","Soignies","Thuin","Tielt","Tongeren",
                                    "Tournai","Turnhout","Verviers","Veurne","Virton","Waremme"),index=19)

# Text input for postal code
PostalCode = st.text_input("Postal Code:",value="4000")
if len(PostalCode) !=4 or not PostalCode.isdigit():
    st.warning("Invalid Postal Code")

st.divider()

st.header("General infos 📄")

# Radio button for selecting state of building
StateOfBuilding = st.radio("State of Building:",["As new","Good","Just Renovated","To Be Done Up","To Renovate","To Restore"],index=1)
StateOfBuilding = clean_imputs[StateOfBuilding]

# Dropdown for selecting PEB
PEB = st.selectbox("PEB:",("G","F","E", "D","C","B","A","A+","A++"),index=5)

# Dropdown for selecting flooding zone
FloodingZone = st.selectbox("Flooding Zone:",("Recognized Flood Zone","Possible Flood Zone","Not in a flood zone", "None of the above"),index=2)
FloodingZone = clean_imputs[FloodingZone]

st.divider()

st.header("Exterior 🌳")

# Number input for number of facades
NumberOfFacades = st.number_input("Number of Facades:", min_value=0,value=2)

# Number input for surface of plot
SurfaceOfPlot = st.number_input("Surface of Plot:", min_value=0, max_value= 2000,value=190)

# Radio button for selecting swimming pool
SwimmingPool = st.radio("Swimming Pool:", ["Yes","No"],index=1)
if SwimmingPool == "Yes":
    SwimmingPool = 1
else:
    SwimmingPool = 0

# Radio button for selecting terrace
Terrace = st.radio("Terrace", ["Yes","No"],index=1)
if Terrace == "Yes":
    Terrace = 1
else:
    Terrace = 0

# Radio button for selecting garden
garden = st.radio("Garden:", ["Yes","No"],index=1)
if garden == "Yes":
    garden = 1
    # Number input for garden area
    gardenArea = st.number_input("Garden Area:", min_value=0, max_value= 1000,value=40)
else:
    garden = 0
    gardenArea = 0

st.divider()

st.header("Interior 🛏️")

# Number input for living area
livingArea = st.number_input("Living Area:", min_value=0, max_value= 500,value=150)

# Slider for selecting number of bedrooms
beds= st.slider('Number of Bedrooms:', 0, 10, 2, step=1)

# Slider for selecting number of bathrooms
bath= st.slider('Number of Bathrooms:', 0, 6, 1, step=1)

# Slider for selecting number of showers
ShowerCount = st.slider('Number of Showers:', 0, 5, 1, step=1)

# Slider for selecting number of toilets
ToiletCount = st.slider('Number of Toilets:', 0, 5, 1, step=1)

# Dropdown for selecting kitchen
Kitchen = st.selectbox("Kitchen:",("Not Installed","Semi Equipped","Installed","USA Installed","USA Hyper Equipped"),index=2)
Kitchen = clean_imputs[Kitchen]

# Create a dictionary with all the property details
property_dict= {
    "BathroomCount":bath,
    "BedroomCount":beds,
    "Garden":garden,
    "GardenArea":gardenArea,
    "LivingArea":livingArea,
    "NumberOfFacades":NumberOfFacades,
    "PostalCode":PostalCode,
    "ShowerCount":ShowerCount,
    "SurfaceOfPlot":SurfaceOfPlot,
    "SwimmingPool": SwimmingPool,
    "Terrace":Terrace,
    "ToiletCount":ToiletCount,
    "TypeOfProperty":TypeOfProperty,
    "District":District,
    'FloodingZone':FloodingZone,
    'PEB':PEB,
    'StateOfBuilding':StateOfBuilding,
    'Kitchen':Kitchen,
    'Region':Region,
    'SubtypeOfProperty':SubtypeOfProperty,
    'Province':Province,
    'TypeOfSale':TypeOfSale
}

# Convert the dictionary to a DataFrame
property_dict=pd.DataFrame(property_dict,index=[1])

# Preprocess the input data using the preprocessor
X= property_dict[preprocessor.feature_names_in_]
X=preprocessor.transform(X)
preprocessed_dict= pd.concat([property_dict,X],axis=1).drop(columns=['District','FloodingZone','PEB','StateOfBuilding','Kitchen', 'Region','SubtypeOfProperty','Province', 'TypeOfSale'])

# Predict button
if st.button("Predict 💡"):
    prediction = model.predict(preprocessed_dict)
    st.success(f"The estimated price of the property is: {round(prediction[0])}€ 💰")
else:
    st.write("Fill in the property details and click Predict to see the estimated price!")
