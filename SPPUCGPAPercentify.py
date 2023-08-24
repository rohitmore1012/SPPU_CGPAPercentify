import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu  # select_options library


# Set page configuration to expand the sidebar by default
st.set_page_config(initial_sidebar_state="expanded")

# Initialize a state variable to control sidebar state
collapse_sidebar = False


# Function to determine grade based on CGPA


def determine_grade(cgpa):
    if 9.00 <= cgpa <= 10.00:
        return "O"
    elif 8.50 <= cgpa <= 8.99:
        return "A+"
    elif 7.50 <= cgpa <= 8.49:
        return "A"
    elif 6.50 <= cgpa <= 7.49:
        return "B+"
    elif 5.50 <= cgpa <= 6.49:
        return "B"
    elif 4.25 <= cgpa <= 5.49:
        return "C"
    elif 4.00 <= cgpa <= 4.24:
        return "P"
    else:
        return None

# Function to calculate percentage and formula based on grade


def calculate_percentage_and_formula(grade, cgpa):
    if grade == "O":
        percentage = 20 * cgpa - 100
        formula = "20 x CGPA - 100"
    elif grade == "A+":
        percentage = 20 * cgpa - 100
        formula = "20 x CGPA - 100"
    elif grade == "A":
        percentage = 10 * cgpa - 15
        formula = "10 x CGPA - 15"
    elif grade == "B+":
        percentage = 5 * cgpa + 22.5
        formula = "5 x CGPA + 22.5"
    elif grade == "B":
        percentage = 5 * cgpa + 22.5
        formula = "5 x CGPA + 22.5"
    elif grade == "C":
        percentage = 4 * cgpa + 28
        formula = "4 x CGPA + 28"
    elif grade == "P":
        percentage = 20 * cgpa - 40
        formula = "20 x CGPA - 40"
    else:
        percentage = None
        formula = None
    return percentage, formula

# Function to determine grade based on SGPA


def determine_grade_sgpa(sgpa):
    if 9.00 <= sgpa <= 10.00:
        return "O"
    elif 8.50 <= sgpa <= 8.99:
        return "A+"
    elif 7.50 <= sgpa <= 8.49:
        return "A"
    elif 6.50 <= sgpa <= 7.49:
        return "B+"
    elif 5.50 <= sgpa <= 6.49:
        return "B"
    elif 4.25 <= sgpa <= 5.49:
        return "C"
    elif 4.00 <= sgpa <= 4.24:
        return "P"
    else:
        return None

# Function to calculate percentage and formula based on SGPA


def calculate_percentage_and_formula_sgpa(grade, sgpa):
    if grade in ["O", "A+"]:
        percentage = 20 * sgpa - 100
        formula = "20 x SGPA - 100"
    elif grade == "A":
        percentage = 10 * sgpa - 15
        formula = "10 x SGPA - 15"
    elif grade in ["B+", "B"]:
        percentage = 5 * sgpa + 22.5
        formula = "5 x SGPA + 22.5"
    elif grade == "C":
        percentage = 4 * sgpa + 28
        formula = "4 x SGPA + 28"
    elif grade == "P":
        percentage = 20 * sgpa - 40
        formula = "20 x SGPA - 40"
    else:
        percentage = None
        formula = None
    return percentage, formula

# Function for grade prediction based on target CGPA/SGPA


def predict_grades_and_percentages(target_cgpa_sgpa):
    if target_cgpa_sgpa >= 9.00:
        predicted_grade = "O"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    elif 8.50 <= target_cgpa_sgpa < 9.00:
        predicted_grade = "A+"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    elif 7.50 <= target_cgpa_sgpa < 8.50:
        predicted_grade = "A"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    elif 6.50 <= target_cgpa_sgpa < 7.50:
        predicted_grade = "B+"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    elif 5.50 <= target_cgpa_sgpa < 6.50:
        predicted_grade = "B"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    elif 4.25 <= target_cgpa_sgpa < 5.50:
        predicted_grade = "C"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    elif 4.00 <= target_cgpa_sgpa < 4.25:
        predicted_grade = "P"
        predicted_percentage = calculate_percentage_and_formula(
            predicted_grade, target_cgpa_sgpa)[0]
    else:
        predicted_grade = "Invalid"
        predicted_percentage = None

    return predicted_grade, predicted_percentage

# Function to calculate the final cumulative percentage


def calculate_cumulative_percentages(semester_cgpa_sgpa_list):
    cumulative_percentage = 0.0
    total_credits = 0

    for semester_cgpa_sgpa in semester_cgpa_sgpa_list:
        semester_gpa, credits = semester_cgpa_sgpa  # Unpack values from the tuple

        # Calculate the percentage for the current semester
        # Determine grade based on semester GPA
        semester_grade = determine_grade(semester_gpa)
        semester_percentage, _ = calculate_percentage_and_formula(
            semester_grade, semester_gpa)  # Calculate percentage

        # Add the weighted percentage to the cumulative_percentage
        cumulative_percentage += (semester_percentage * credits)

        # Update total credits
        total_credits += credits

    # Calculate the final cumulative percentage
    if total_credits > 0:
        final_cumulative_percentage = cumulative_percentage / total_credits
    else:
        final_cumulative_percentage = None

    return final_cumulative_percentage

# Function to calculate the final cumulative CGPA from the list of semester CGPAs and credits


def calculate_cgpa_from_sgpa_and_credits(semester_cgpa_sgpa_list):
    total_weighted_sgpa = 0.0
    total_credits = 0

    for semester_sgpa, credits in semester_cgpa_sgpa_list:
        total_weighted_sgpa += semester_sgpa * credits
        total_credits += credits

    if total_credits > 0:
        cgpa = total_weighted_sgpa / total_credits
        return cgpa
    else:
        return None


# Set page title and subtitle
st.title("SPPU CGPAPercentify")
st.subheader("2019 Pattern Grade-to-Percentage Conversion")

# Define default text color
text_color = "#000000"  # Default text color is black

# Set page title and subtitle with CSS styles
st.markdown("""
    <style>
    .header {
        color: #0055a6;
        font-size: 32px;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 18px;
        color: #555555;
        margin-bottom: 15px;
    }
    .section-header {
        color: #0055a6;
        font-size: 24px;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)


# Sidebar section starts here

# st.write("SPPU CGPAPercentify") # Title

st.sidebar.image("https://www.careeryojana.in/wp-content/uploads/2021/04/SPPU-University.png", width=100,
                 use_column_width=False)  # logo
st.sidebar.write('''# SPPU CGPAPercentify ''')
with st.sidebar:
    selected = option_menu("Navigation", ["Home", "CGPA to Percentage", "SGPA to Percentage",
                           "Grade Prediction", "Semester-wise CGPA and Percentage Calculation", "About"])

    # After handling the option selection, change the state variable to collapse the sidebar
    collapse_sidebar = True

# If the state variable is True, collapse the sidebar
if collapse_sidebar:
    st.markdown(
        '<style>div.sidebar-closed { display: none }</style>', unsafe_allow_html=True)
    st.sidebar.markdown(
        '<style>div[aria-expanded="false"] { margin-left: -40px; }</style>', unsafe_allow_html=True)


if selected == "Home":
    st.markdown(
        "<h1 class='header'>Welcome to SPPU CGPAPercentify!</h1>", unsafe_allow_html=True)
    st.write("As a student of Savitribai Phule Pune University (SPPU), you often encounter the need to convert your academic performance metrics, such as CGPA and SGPA, into their percentage equivalents. This process is crucial for various purposes, including scholarship applications, job placements, and more.")

    st.write("SPPU CGPAPercentify is designed to make this conversion seamless and hassle-free. With this web app, you can effortlessly calculate the corresponding percentages for your CGPA or SGPA based on the SPPU grading system.")

    st.write("Here's how you can use SPPU CGPAPercentify:")
    st.write(
        "**1. Explore the 'CGPA to Percentage' section if you have your CGPA ready.**")
    st.write(
        "**2. Utilize the 'SGPA to Percentage' section for SGPA-to-percentage conversions.**")
    st.write(
        "**3. Predict your future grades and percentages with the 'Grade Prediction' feature.**")
    st.write("**4. Calculate your cumulative percentage and CGPA across multiple semesters in the 'Semester-wise CGPA and Percentage Calculation' section.**")
    st.write(
        "**5. Learn more about SPPU CGPAPercentify and its functionalities in the 'About' section.**")

    st.write("Whether you're a student looking to streamline your academic progress or an individual seeking accurate percentage conversions, SPPU CGPAPercentify is here to simplify your journey.")

    st.write("So go ahead and begin your conversion process. Feel free to explore the sections that cater to your needs, and don't hesitate to check out the 'About' section for more details on the app.")

    st.markdown(
        "<p class='subheader'>Let's ensure that your academic journey is complemented by a user-friendly and efficient tool. Happy converting!</p>", unsafe_allow_html=True)
    # st.snow()

    # CGPA to Percentage section
elif selected == "CGPA to Percentage":
    st.markdown(
        "<h2 class='section-header'>Convert CGPA to Percentage</h2>", unsafe_allow_html=True)
    # Explanation for CGPA to Percentage section
    st.write("Welcome to the 'CGPA to Percentage' section!\n\n"
             "Here, you can easily convert your CGPA to its equivalent percentage based on SPPU's grading system.\n\n"
             "Simply enter your CGPA, and the app will determine the corresponding grade, percentage, and formula used for the conversion.")
    cgpa = st.number_input(
        "Enter CGPA:", min_value=0.0, max_value=10.0, step=0.01)

    grade = determine_grade(cgpa)
    if grade is not None:
        percentage, formula = calculate_percentage_and_formula(grade, cgpa)
        st.write(
            f"Percentage equivalent of **CGPA {cgpa:.2f}** with **grade {grade}** is **{percentage:.2f}%**.")
        st.balloons()

        st.write(
            f"For **CGPA {cgpa:.2f}**, which corresponds to an **{grade} grade**, the formula used in the SPPU CGPA Percentage system for **{grade} grade is {formula}**.")
        st.write(
            f"Accordingly, **{formula.replace('CGPA', str(cgpa))} = {percentage:.2f}%**")
        # f"i.e. **{formula.replace('CGPA', str(cgpa))} = {percentage:.2f}%**")

    else:
        st.write("Enter a valid CGPA between 4.00 and 10.00.")

        # SGPA to Percentage section

elif selected == "SGPA to Percentage":
    st.markdown(
        "<h2 class='section-header'>Convert SGPA to Percentage</h2>", unsafe_allow_html=True)
    # Explanation for SGPA to Percentage section
    st.write("Explore the 'SGPA to Percentage' section to convert your SGPA into its corresponding percentage.\n\n"
             "Similar to the CGPA conversion, enter your SGPA, and the app will calculate the grade, percentage, and formula for the conversion.")

    sgpa = st.number_input(
        "Enter SGPA:", min_value=0.0, max_value=10.0, step=0.01)

    grade_sgpa = determine_grade_sgpa(sgpa)
    if grade_sgpa is not None:
        percentage_sgpa, formula_sgpa = calculate_percentage_and_formula_sgpa(
            grade_sgpa, sgpa)
        st.write(
            f"Percentage equivalent of **SGPA {sgpa:.2f}** with **grade {grade_sgpa}** is **{percentage_sgpa:.2f}%**.")
        st.balloons()

        st.write(
            f"For SGPA {sgpa:.2f}, which corresponds to an **{grade_sgpa} grade**, the formula used in the SPPU SGPA Percentage system for **{grade_sgpa} grade** is **{formula_sgpa}**.")
        st.write(
            f"Accordingly, **{formula_sgpa.replace('SGPA', str(sgpa))} = {percentage_sgpa:.2f}%**")

    else:
        st.write("Enter a valid CGPA between 4.00 and 10.00.")

        # Grade Prediction section
elif selected == "Grade Prediction":
    st.markdown(
        "<h2 class='section-header'>Grade Prediction</h2>", unsafe_allow_html=True)

    st.write(
        "Predict your future grades and percentages based on target CGPA/SGPA:")

    # Explanation for Grade Prediction section
    st.write("In the 'Grade Prediction' section, you can predict your future grades and percentages based on a target CGPA or SGPA.\n\n"
             "Enter your desired target, and the app will provide you with the predicted grade and percentage, giving you insights into your academic goals.")

    target_cgpa_sgpa = st.number_input(
        "Enter Target CGPA/SGPA:", min_value=0.0, max_value=10.0, step=0.01)

    if st.button("Predict Grades and Percentages"):
        predicted_grade, predicted_percentage = predict_grades_and_percentages(
            target_cgpa_sgpa)

        if predicted_grade != "Invalid":
            st.write(
                f"**Predicted Grade: {predicted_grade}, Predicted Percentage: {predicted_percentage:.2f}%**")
            st.balloons()
        else:
            st.write("Invalid input or prediction not available.")

        # Multiple Semesters section
elif selected == "Semester-wise CGPA and Percentage Calculation":
    st.markdown(
        "<h2 class='section-header'>Calculate Percentages and CGPA Semester-wise</h2>", unsafe_allow_html=True)
    # Explanation for Semester-wise CGPA and Percentage Calculation section
    st.write("The 'Semester-wise CGPA and Percentage Calculation' section allows you to calculate cumulative percentages and CGPA across multiple semesters. \n\n"
             "Enter your SGPA and credits for each semester, and the app will compute the cumulative percentage and CGPA, helping you track your academic progress over time.")

    num_semesters = st.slider("Number of Semesters:",
                              min_value=1, max_value=8, step=1)

    semester_cgpa_sgpa_list = []
    # set limit to 8 semesters for now (can be changed later)

    for semester in range(1, num_semesters + 1):
        st.write(f"Semester {semester}")
        cgpa_sgpa = st.number_input(
            f"Enter SGPA for Semester {semester}:", min_value=0.0, max_value=10.0, step=0.01)
        credits = st.number_input(
            f"Enter Credits for Semester {semester}:", min_value=0, max_value=100, step=1)  # Add credits input
        semester_cgpa_sgpa_list.append(
            (cgpa_sgpa, credits))  # Pack values into a tuple

    if st.button("Calculate"):
        cumulative_percentages = calculate_cumulative_percentages(
            semester_cgpa_sgpa_list)
        cumulative_cgpa = calculate_cgpa_from_sgpa_and_credits(
            semester_cgpa_sgpa_list)

        if cumulative_percentages is not None and cumulative_cgpa is not None:
            st.write(f"**Percentage: {cumulative_percentages:.2f}%**")
            st.write(f"**CGPA: {cumulative_cgpa:.2f}**")
            st.balloons()

            # Display calculation breakdown
            st.write("**Calculation Breakdown:**")
            for i, (semester_sgpa, credits) in enumerate(semester_cgpa_sgpa_list, start=1):
                semester_grade = determine_grade_sgpa(semester_sgpa)
                semester_percentage, _ = calculate_percentage_and_formula_sgpa(
                    semester_grade, semester_sgpa)

                st.write(
                    f"**Semester {i} - SGPA: {semester_sgpa:.2f} | Grade: {semester_grade} | Percentage: {semester_percentage:.2f}%**")

        else:
            st.write("Invalid input or calculation not available.")

        # About section
elif selected == "About":
    st.markdown(
        "<h2 class='section-header'>About SPPU CGPAPercentify</h2>", unsafe_allow_html=True)
    st.write(
        "SPPU CGPAPercentify is a simple web app designed for SPPU students to quickly "
        "convert their CGPA to percentage. It provides an easy way to calculate percentage "
        "equivalents based on the SPPU CGPA grading system.\n\n"
        "Web App Developer: **Rohit More**\n\n"
        "Connect with me on LinkedIn: [Rohit More](https://www.linkedin.com/in/rohit-more1012/)\n\n"
        "View the source code on GitHub: [SPPU CGPAPercentify](https://github.com/rohitmore1012/SPPU_CGPAPercentify)\n\n"
        "Join our Telegram Group for updates and discussions: [Telegram Group](https://t.me/SPPU_COMPUTER_ER)\n\n"


        "How it works:\n"
        "1. Enter your CGPA in the 'CGPA to Percentage' section.\n"
        "2. The app will determine your grade based on your CGPA.\n"
        "3. It will then calculate the percentage equivalent and display the result.\n\n"
        "Feel free to use this tool to simplify your grade-to-percentage conversions!\n\n"
        "For more information on the SPPU CGPA to percentage conversion, you can refer to the "
        "[official SPPU document](https://campus.unipune.ac.in/CCEP/CBCS/CBCS_Passing_Standards.aspx)."
    )
    # st.snow()

# Add page footer
st.markdown("---")
st.write("For CGPA and SGPA to Percentage calculations based on SPPU's guidelines.")
