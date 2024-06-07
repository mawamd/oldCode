# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import pandas as pd

# Function to generate the insulin sliding scale table
def generate_table(correction_unit, correction_factor, target_glucose):
    glucose_ranges = []
    data = []
    
    start_range = target_glucose
    end_range = target_glucose + correction_factor - 1
    dose = correction_unit
    
    while start_range <= 500:  # Arbitrary upper limit for glucose ranges
        glucose_ranges.append(f"{start_range}-{end_range}")
        data.append({'Glucose Range': f'{start_range}-{end_range}', 'Humalog Dose': dose})
        start_range = end_range + 1
        end_range = start_range + correction_factor - 1
        dose += correction_unit
    
    return pd.DataFrame(data)

# Custom CSS for lighter theme, blue headers, and alternating row colors
st.markdown("""
    <style>
    /* Your custom CSS from myTable.css */
    @font-face {
        font-family: 'KaTeX_AMS';
        font-style: normal;
        font-weight: 400;
        src: url(../../static/media/KaTeX_AMS-Regular.73ea273a72f4aca30ca5.woff2) format('woff2'),
             url(../../static/media/KaTeX_AMS-Regular.d562e886c52f12660a41.woff) format('woff'),
             url(../../static/media/KaTeX_AMS-Regular.853be92419a6c3766b9a.ttf) format('truetype');
    }
    @font-face {
        font-family: 'KaTeX_Caligraphic';
        font-style: normal;
        font-weight: 700;
        src: url(../../static/media/KaTeX_Caligraphic-Bold.a1abf90dfd72792a577a.woff2) format('woff2'),
             url(../../static/media/KaTeX_Caligraphic-Bold.d757c535a2e5902f1325.woff) format('woff'),
             url(../../static/media/KaTeX_Caligraphic-Bold.7489a2fbfb9bfe704420.ttf) format('truetype');
    }
    @font-face {
        font-family: 'KaTeX_Caligraphic';
        font-style: normal;
        font-weight: 400;
        src: url(../../static/media/KaTeX_Caligraphic-Regular.d6484fce1ef428d5bd94.woff2) format('woff2'),
             url(../../static/media/KaTeX_Caligraphic-Regular.db074fa22cf224af93d7.woff) format('woff'),
             url(../../static/media/KaTeX_Caligraphic-Regular.7e873d3833eb108a0758.ttf) format('truetype');
    }
    /* Additional font faces omitted for brevity */
    
    .main {
        background-color: #f9f9f9;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    .stTextInput, .stNumberInput, .stSelectbox {
        background-color: #e6f0ff;
        color: #333;
        border-radius: 4px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 10px 24px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    h1 {
        color: #333;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }
    th, td {
        text-align: left;
        padding: 8px;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    tr:nth-child(odd) {
        background-color: #ffffff;
    }
    th {
        background-color: #5bc0de;
        color: white;
    }
    .css-1d391kg {
        background-color: #5bc0de !important;
    }
    .st-af, .st-ag, .st-ah, .st-ai, .st-aj, .st-ak, .st-al, .st-am {
        background-color: #e6f0ff;
        color: #333;
    }
    .st-bf {
        color: #333;
    }
    .st-emotion-cache-1qg05tj {
    font-size: 14px;
    color: rgb(0, 0, 0);
    display: flex;
    visibility: visible;
    margin-bottom: 0.25rem;
    height: auto;
    min-height: 1.5rem;
    vertical-align: middle;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
}
    </style>
    """, unsafe_allow_html=True)

st.title('Insulin Sliding Scale Calculator')

# Default values
default_correction_unit = 0.5
default_correction_factor = 60
default_target_glucose = 160

# User inputs
correction_unit = st.selectbox('Correction Unit', [0.5, 1.0], index=0)
correction_factor = st.number_input('Correction Factor', value=default_correction_factor, min_value=1, step=1)
target_glucose = st.number_input('Target Glucose', value=default_target_glucose, min_value=0, step=1)

if st.button('Generate Table'):
    table = generate_table(correction_unit, correction_factor, target_glucose)
    st.write(table.to_html(index=False, escape=False), unsafe_allow_html=True)
