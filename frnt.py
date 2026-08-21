import streamlit as st
from extractor import extract_event_details

st.title("📌 Event Information Extractor")

text = st.text_area(
    "Enter Event Description"
)

if st.button("Extract"):

    if text.strip():

        try:
            response = extract_event_details(text)

            # Check for Invalid Event Description
            if (
                response.event_name
                and response.event_name[0] == "Invalid Event Description"
            ):
                st.error("❌ Invalid Event Description")

            else:
                st.success("✅ Event Details Extracted Successfully!")

                st.markdown("## 📌 Event Information")

                st.write(
                    f"**Event Name:** {response.event_name[0] if response.event_name else 'Not_available'}"
                )

                st.write(
                    f"**Event Date:** {response.event_date[0] if response.event_date else 'Not_available'}"
                )

                st.write(
                    f"**Event Time:** {response.event_time[0] if response.event_time else 'Not_available'}"
                )

                st.write(
                    f"**Event Location:** {response.event_location[0] if response.event_location else 'Not_available'}"
                )

                st.write(
                    f"**Organizer:** {response.organizer[0] if response.organizer else 'Not_available'}"
                )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter an event description.")