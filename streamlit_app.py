import streamlit as st


st.title("buy your wallet!!")

number = st.number_input("Enter the quantity of wallets, $20 each",min_value=0, max_value=10, step=1, key="wallets")
price_of_wallet = number*20

#discount price for tiered pricing 
if "cart" not in st.session_state:
    st.session_state["cart"]=[]

list_of_materials = []
list_of_wallet_prices = []

for i in range(number):
    st.subheader("Wallet " + str(i + 1))
    customise = ['size', 'material', 'colour', 'engraving'] #add colours appeal to more ages bro idk anymore, list
    
    st.write('customisations available:')
    for item in customise: #for loop
        st.write(item)

    customise_pressed = "customise_pressed" + str(i)
    engraving_pressed = "engraving_pressed" + str(i)
    
    if customise_pressed not in st.session_state: #visibility of button
        st.session_state[customise_pressed] = False
    if engraving_pressed not in st.session_state:
        st.session_state[engraving_pressed] = False

    if st.button("Customise your wallet", key = "customisation_button" + str(i)):
        st.session_state[customise_pressed] = True #when button pressed

    amount_of_wallet = number
    if amount_of_wallet > 0 and st.session_state[customise_pressed]:
        st.image(['https://pngimg.com/uploads/wallet/wallet_PNG77078.png', "https://toppng.com/uploads/preview/leather-wallet-11530960452p1ggvjjey4.png"], caption = ['small', "medium"], width = 100)
      
        size = st.selectbox("Select a size", ["small", "medium", "large"], key="size" + str(i)) #reyna's code + for loop for customers to customise each wallet
        if size == "medium":
            st.write("For medium add $10")
            price_of_wallet += 10
        elif size == "large":
            st.write("For large add $20")
            price_of_wallet += 20
        else:
            st.write("small adds $0")
        
        choice = st.selectbox("Select one material", ["leather", "nylon", "canvas"], key = "material" + str(i))
        
        if choice == "leather":
            st.write("For leather add $50")
            price_of_wallet += 50
        elif choice == "nylon":
            st.write("For nylon add $25")
            price_of_wallet += 25
        else:
            st.write("Canvas adds $0")

        list_of_materials.append(choice)
    
        if st.button("Add engraving", key = "engrave_button" + str(i)):
            st.session_state[engraving_pressed] = True

        if st.session_state[engraving_pressed]:
            engraving_text = st.text_input("What would you like engraved?", key="engraving_text" + str(i))
            st.write("Engraving adds $10")
            price_of_wallet += 10
            
        list_of_wallet_prices.append(price_of_wallet)
        
        if st.session_state[customise_pressed] and st.button("Add to cart", key="add_cart"+str(i)):
            wallet_details = {"quantity":1,"size":size,"material":choice,"engravement":engraving_text}
            st.session_state["cart"].append(wallet_details)
            st.success("Wallet {} added to cart!".format(i+1))

#Discounts
from typing import Counter
discounted_price = 0
if price_of_wallet > 300:
    discounted_price = 0.9(price_of_wallet)
if 'leather' and 'nylon' in list_of_materials:
    discounted_price = 0.85(price_of_wallet)
number_of_each_material = Counter(list_of_materials)
if 'leather' in Counter(list_of_materials) >= 2 and len(list_of_materials) >= 3:
    discounted_price = price_of_wallet - 0.5(list_of_materials[2])

st.header("Your Cart")
for i,custom in enumerate(st.session_state["cart"],1):
    st.write("Wallet {}:{}".format(i,custom))

st.write("Your total =", price_of_wallet)

st.button("Purchase")
