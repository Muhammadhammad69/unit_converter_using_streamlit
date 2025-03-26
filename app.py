import streamlit as st
from units import all_units
from unit_conversion import unit_conversion_func

st.markdown( """
    <style>
        .stApp{
            background-color: #D3D3D3;
        }
        .result-box{
            background-color: #f0f2f6;
            font-weight: 600;
            box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
            padding: 15px;
            font-size: 20px;
            border-radius: 8px;
            text-align: center;
            }
            </style>
            """
            , unsafe_allow_html=True)



unit_category =["Select Unit"] + [unit.replace("_", " ").capitalize() for unit in all_units]

main_unit = st.selectbox("Units", unit_category, ) if len(unit_category) > 0 else ""

# st.selectbox("From", ["Kilometer", "Kil"])
# check = st.selectbox("To", ["Kilometer", "Kil"])
if main_unit != "Select Unit":
    st.markdown("# Universal Unit Converter App")
    value = st.number_input("Enter the value to be converted")
    sub_unit = [unit.replace("_", " ").capitalize() for unit in all_units[main_unit.lower().replace(" ", "_")]]

    col1, col2 = st.columns(2)
    with col1:    
        from_unit = st.selectbox("From", sub_unit, index=0 ) if len(sub_unit) > 0 else ""
    with col2:  
        to_unit = st.selectbox("To", sub_unit, index=1) if len(sub_unit) > 0 else ""
    print(from_unit, to_unit)
# if value > 0 and /
    if st.button("Convert"):
        if value > 0:
            result = unit_conversion_func(main_unit,from_unit, to_unit, value)
            output_value = str(result["answer_value"])
            full_value = ""
            if "e" in output_value:
                point_value = output_value[output_value.index("e") + 2: len(output_value)]
                print(point_value)
                point_value_upgrade = int(point_value) + 3 if int(point_value) > 9 else int(point_value)
                full_value = format(float(output_value), f".{str(point_value_upgrade)}f")
                # print(full_value)
            full_value = f"=> ({full_value})" if len(full_value) > 0 else ""
            st.markdown(f"<div class='result-box'>{result['message']} {full_value}</div>", 
            unsafe_allow_html=True)

