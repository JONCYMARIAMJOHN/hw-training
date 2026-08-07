import streamlit as st
import pandas as pd

st.title("QA Automation Tool")

uploaded_file = st.file_uploader("Upload CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file, sep="|")

    # Column list
    st.write(f"### Field list")
    column_list = df.columns.tolist()
    st.write("Field list : \n", column_list)
    # -------------------------------------------------------



    # Null Summary
    st.write(f"### Null Summary")
    null_summary = pd.DataFrame({
    'Null_Count': df.isnull().sum(),
    'Null_Percentage': (df.isnull().sum() / len(df)) * 100,
    'Unique': df.apply(lambda col: "Yes" if col.is_unique else "No"),
    'Value': df.apply(lambda col: col.unique() if col.nunique() < 2 else "More values")
    })
    null_summary['Null_Percentage'] = null_summary['Null_Percentage'].round(2)
    completely_null_columns = null_summary.index[null_summary['Null_Percentage'] == 100].tolist()
    mandatory_columns = null_summary.index[null_summary['Null_Percentage'] == 0].tolist()

    
    st.write("Null Summary : \n", null_summary)
    st.write("Empty fields : \n", completely_null_columns)
    st.write("Mandatory fields : \n", mandatory_columns)
    # ----------------------------------------------------------

    # White Space Checking
    st.write(f"### White Space Checking")
    selected_field = st.selectbox("\nChoose a field to check whether whitespace exists :",column_list, key="whitespace_field")  
    st.write("Selected field:", selected_field)
    white_space_rows = df[
    df[selected_field].fillna('').astype(str).str.contains(
        r'(^\s)|(\s$)|(\s{2,})',
        regex=True
    )]
    st.write("Number of records with whitespace :", len(white_space_rows))
    st.write(white_space_rows[['pdp_url', selected_field]])


#----------------------------------------------------------
    # Numeric values checking

    st.write(f"### Numeric Values Checking")
    selected_numeric_field = st.selectbox("\nChoose a field to check numric values :",column_list, key="numeric_field")  
    st.write("Selected field:", selected_numeric_field)

    non_numeric_rows = df[
    (df[selected_numeric_field] != "") &
    (pd.to_numeric(
        df[selected_numeric_field],
        errors="coerce"
    ).isna())]
    
    st.write(f"Number of non-numeric values: {len(non_numeric_rows)}")
    if not non_numeric_rows.empty:
        st.write(non_numeric_rows[[ "pdp_url",selected_numeric_field]])







    #-----------------------------------------------------
    # Unique Values Checking

    st.write(f"### Unique Values Checking")
    selected_col = st.selectbox("\nChoose a field to check unique values :",column_list, key="unique_field")  
    st.write("Selected field:", selected_col)
    st.write(df[selected_col].unique())
