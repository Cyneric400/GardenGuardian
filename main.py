import streamlit as st
import db_man
from plant import Plant

st.title("GardenGuardian")

st.subheader("Plant Database")
st.write([p for p in db_man.read_items()])

with st.form("add_plant"):
    st.subheader("Add a new plant here")
    species = st.text_input(label="Plant species")
    schedule = st.number_input("Watering schedule")
    submit = st.form_submit_button("Add plant")

if submit:
    db_man.add_item(Plant(species, schedule))
    st.rerun()
    
