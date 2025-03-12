import streamlit as st
import db_man
from plant import Plant
from math import ceil

st.title("GardenGuardian")

st.subheader("Plant Database")
plants = db_man.read_items()
# https://streamly.streamlit.app used for building this section
cols = [st.columns(3) for i in range(ceil(len(plants)))]
j = 0
k = 0
for p in plants:
    with cols[j][k]:
        st.write(f"**{p[1]}**".upper())
        st.write(f"*Plant #{p[0]}*")
        st.write(f"Days since last watering: {db_man.read_log(p[0])}")
        st.write(f"Watering interval: {p[2]} days")
        st.button("Water plant!", key=f"item_button{p[0]}")
    k += 1
    if k >= 3:
        k = 0
        j += 1

with st.form("add_plant"):
    st.subheader("Add a new plant here")
    species = st.text_input(label="Plant species")
    schedule = st.number_input("Watering schedule")
    submit = st.form_submit_button("Add plant")

if submit:
    db_man.add_item(Plant(species, schedule))
    st.rerun()
