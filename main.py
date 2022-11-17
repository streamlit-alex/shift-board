import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Shift Board",
    page_icon=" 🕰 ",
    layout="wide",
)

data = pd.read_csv('data.csv', encoding="iso8859_2")

# dashboard title
st.title("Peak Shift Board 🕰️ ")

with st.form(key='shift_board',clear_on_submit=True):
    emp_id = st.text_input("Enter your operator name")

    # top-level filters
    tod_filter = st.multiselect("Can you work days or nights?", ["Days", "Nights"])

    dow_filter = st.multiselect("Which days can you work?", ["Friday 25th",
                                                             "Saturday 26th", "Sunday 27th","Monday 28th",
                                                             "Tuesday 29th", "Wednesday 30th", "Thursday 1st"])

    length = st.slider("What is your preferred shift length?", max_value=12, min_value=8)

    hours = st.number_input("How many shifts can you work between Nov 24th and December 1st (4 min)", step=1)

    # creating a single-element container
    placeholder = st.empty()

    # save data to local folder
    submit_button = st.form_submit_button(label='Update')

    if submit_button:
        update = data[data['Operator'] == emp_id]
        if len(update):
            update['Schedule'] = tod_filter
            update['Available Days'] = dow_filter
            update['Shift Length'] = length.value
            update['Available Hours'] = hours.value
        else:
            pd.concat([data, pd.DataFrame(data={'Operator': [emp_id], 'Schedule': [tod_filter],
                                              'Available Days': [dow_filter], 'Shift Length': [length],
                                              'Available Hours': [hours]})])
        data.to_csv('data.csv')
        st.snow()


