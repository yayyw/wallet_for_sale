import streamlit as st

st.title("buy your wallet!!")

number = st.number_input("Enter the quantity of wallets, $20 each",min_value=0, max_value=10, step=1, key="wallets") 

customise = ['size', 'material', 'engraving'] 

st.image("https://i.imgur.com/C88SG8i.jpeg")

st.write('customisations available:')
for item in customise: #for loop
    st.write(item)
    
if "cart" not in st.session_state:
    st.session_state["cart"]= []

if "list_of_materials" not in st.session_state:
    st.session_state["list_of_materials"] = []
list_of_materials = st.session_state["list_of_materials"]

if "list_of_wallet_prices" not in st.session_state:
    st.session_state["list_of_wallet_prices"] = []
list_of_wallet_prices = st.session_state["list_of_wallet_prices"]

if "total_price" not in st.session_state:
    st.session_state["total_price"] = 0

for i in range(number):
    price_of_wallet = 20
    st.subheader("Wallet " + str(i + 1))

    customise_pressed = "customise_pressed" + str(i) # unique for each wallet, prevents clashes
    engraving_pressed = "engraving_pressed" + str(i)
    remove = "remove_from_cart" + str(i)
    
    if customise_pressed not in st.session_state: #visibility of button
        st.session_state[customise_pressed] = False
    if engraving_pressed not in st.session_state:
        st.session_state[engraving_pressed] = False

    if st.button("Customise your wallet", key = "customisation_button" + str(i)):
        st.session_state[customise_pressed] = True #when button pressed

    amount_of_wallet = number
    if amount_of_wallet > 0 and st.session_state[customise_pressed]:
      
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
    
        if st.button("Add engraving", key = "engrave_button" + str(i)):
            st.session_state[engraving_pressed] = True
        engraving_text = ""
        if st.session_state[engraving_pressed]:
            engraving_text = st.text_input("What would you like engraved?", key="engraving_text" + str(i))
            st.write("Engraving adds $10")
            price_of_wallet += 10

        
        if st.session_state[customise_pressed] and st.button("Add to cart", key="add_cart" + str(i)):
            st.session_state["total_price"] += price_of_wallet
            wallet_details = {"size":size, "material":choice, "engravement":engraving_text}
            list_of_wallet_prices.append(price_of_wallet)
            list_of_materials.append(choice)
            st.session_state["cart"].append(wallet_details)
            st.success("Wallet {} added to cart!".format(i+1)) #add to cart

        if remove not in st.session_state:
            st.session_state[remove] = False

        if st.button("remove from cart", key = "remove_from_cart" + str(i)):
            st.session_state[customise_pressed] = True
            
        if st.button("remove from cart", key="remove_from_cart" + str(i)) and len(list_of_wallet_prices) > i:
            wallet_price = list_of_wallet_prices[i]
            st.session_state["total_price"] = max(0, st.session_state["total_price"] - wallet_price)
            del st.session_state["cart"][i]
            del list_of_wallet_prices[i]
            st.success(f"Wallet {i+1} removed from cart :(") #i starts from 0

        elif len(st.session_state["cart"]) == 0:
            st.write("No wallets in cart:(")


#Discounts
percentage_discount = []
from collections import Counter
total_price  = st.session_state["total_price"]
discounted_price = total_price

if total_price > 200:
    percentage_discount.append(0.9)
if 'leather' in list_of_materials and 'nylon' in list_of_materials:
    percentage_discount.append(0.85)
for  i in percentage_discount:
    discounted_price *= i

material_counts = Counter(list_of_materials)

if material_counts['leather'] > 1 and len(list_of_wallet_prices) > 2:
    discounted_price -= 0.5*(list_of_wallet_prices[2])
    st.write('discount, more than 1 leather')
    
with st.sidebar:
    st.header("Your Cart")
    if "cart" in st.session_state and len(st.session_state["cart"]) > 0:
        for i, custom in enumerate(st.session_state["cart"], 1):
            if custom['engravement']:
                st.write(f"Wallet {i}: size: {custom['size']}, material: {custom['material']}, engravement: {custom['engravement']}")
            else:
                st.write(f"Wallet {i}: size: {custom['size']}, material: {custom['material']}")
    else:
        st.write("No wallets added to cart yet.")
    st.write("Your total =", total_price)
    st.write("Total after discount=", discounted_price)
    st.button("Purchase")
    

file_name = "customer_data.txt"
with open(file_name, "w") as file:
    file.write("This is a new file created using open().")
    


