import streamlit as st
import db_man
from plant import Plant
from math import ceil
from datetime import date


def water_plant(plant: Plant):
    plant.set_last_watered(date.today())


def main():
    st.title("GardenGuardian")

    st.subheader("Plant Database")
    plants = db_man.read_items()
    # Convert list of tuples to a list of Plant objects
    for i, plant in enumerate(plants):
        plants[i] = Plant(species=plant[1], schedule=plant[2], id=plant[0])
        plants[i].set_last_watered(db_man.read_log(plants[i].id))
        if plants[i].id == 2:
            print(plants[i].last_watered)

    num_cols = 3
    num_rows = ceil(len(plants) / 3.0)
    # https://streamly.streamlit.app used for building this section
    cols = [st.columns(num_cols, border=True, vertical_alignment="center") for i in range(num_rows)]
    for j in range(num_rows):
        for k in range(min(num_cols, len(plants) - (j * num_cols))):
            p = plants[(j * num_cols) + k]
            print(type(p))
            with cols[j][k]:
                st.write(f"**{p.species}**".upper())
                st.write(f"*Plant #{p.id}*")
                st.write(f"Days since last watering: {(date.today() - p.last_watered).days}")
                st.write(f"Watering interval: {p.schedule} days")
                # Create a centered button
                # https://discuss.streamlit.io/t/alignment-of-content/29894
                inner_cols = st.columns([0.13, 0.75, 0.12])
                with inner_cols[1]:
                    # Call update log and pass in the current plant.
                    st.button("Water plant!", key=f"item_button{p.id}", on_click=lambda pl: water_plant(pl))
    
    with st.form("add_plant"):
        st.subheader("Add a new plant here")
        species = st.text_input(label="Plant species")
        schedule = st.number_input("Watering schedule")
        submit = st.form_submit_button("Add plant")

    if submit:
        db_man.add_item(Plant(species, schedule))
        st.rerun()


main()
