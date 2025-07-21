import streamlit as st
import json

st.set_page_config(page_title="Exoplanet Datapoint Counter", layout="centered")

st.title("Exoplanet Datapoints Counter")
st.markdown("""
Upload or **drag and drop** your `.json` file containing image observation data.
The app will count how many image-like observations exist.
""")

uploaded_file = st.file_uploader(
    label="Drop your JSON file here or click to upload",
    type=["json"],
    accept_multiple_files=False,
    label_visibility="visible"
)

if uploaded_file:
    try:
        data = json.load(uploaded_file)

        if isinstance(data, list) and len(data) > 1:
            header = data[0]
            observations = data[1:]
            total = len(observations)

            st.success(f"Total number of image observations: **{total}**")

            with st.expander("Show field names"):
                st.write(header)

            with st.expander("Preview first 5 observations"):
                st.json(observations[:5])
        else:
            st.warning("The JSON file is valid but does not contain enough data rows.")

    except json.JSONDecodeError:
        st.error("The uploaded file is not a valid JSON.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

else:
    st.info("Drag and drop your JSON file above to get started.")
