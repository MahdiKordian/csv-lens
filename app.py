import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dataset_overview(df):
    st.divider()
    st.subheader("Dataset Overview")
    col1,col2,col3=st.columns(3)
    col1.metric("Rows",str(df.shape[0]))
    col2.metric("Columns",str(df.shape[1]))
    col3.metric("Missing Values",str(df.isna().sum().sum()))
    st.dataframe(df, use_container_width=True)
    with st.expander("Column Information",expanded=False):
        info_df=pd.DataFrame({
            "Data type": df.dtypes,
            "Unique values": df.nunique(),
            "Missing values": df.isna().sum(),
            "The Missing Percentage": (df.isna().mean() * 100).round(2)})
        st.dataframe(info_df, use_container_width=True)


def descriptive_statistics(df):
    st.divider()
    st.subheader("Descriptive Statistics")
    stats=df.describe().T
    stats=stats.rename(columns={"25%": "Q1","50%":"Median (Q2)","75%":"Q3"})
    st.dataframe(stats, use_container_width=True)


def is_numeric(df, column):
    return pd.api.types.is_numeric_dtype(df[column])


def custom_chart(df, chart_type, x_axis, y_axis, hue):
    fig, ax = plt.subplots(figsize=(10, 5))

    if hue == "None":
        hue = None

    plot_kwargs = {}

    if hue is not None:
        plot_kwargs = {
            "hue": hue,
            "palette": "mako"
        }

    if chart_type == "Scatter":
        sns.scatterplot(
            data=df,
            x=x_axis,
            y=y_axis,
            ax=ax,
            **plot_kwargs
        )

    elif chart_type == "Line":
        sns.lineplot(
            data=df,
            x=x_axis,
            y=y_axis,
            ax=ax,
            **plot_kwargs
        )

    elif chart_type == "Bar":
        sns.barplot(
            data=df,
            x=x_axis,
            y=y_axis,
            ax=ax,
            **plot_kwargs
        )

    elif chart_type == "Hist":
        sns.histplot(
            data=df,
            x=x_axis,
            ax=ax,
            **plot_kwargs
        )

    st.pyplot(fig)

def data_analysis(df):
    st.divider()
    st.subheader("Data Analysis")
    tab1,tab2,tab3,tab4=st.tabs(["📉 Distribution", "🔗 Correlation", "📊 Categorization", "🎯 Custom"])
    with tab1:
        selected_column=st.selectbox("Select a column :", df.columns,key="distribution_column")
        fig,ax=plt.subplots(figsize=(10, 5))
        if is_numeric(df,selected_column):
            sns.histplot(df,x=selected_column,ax=ax,bins=20,color='steelblue')
        else:
            sns.countplot(data=df,x=selected_column,ax=ax,color='steelblue')
        st.pyplot(fig)
    with tab2:
        numeric_df = df.select_dtypes(include="number")
        if numeric_df.shape[1] < 2:
            st.info("⚠️ Correlation needs at least 2 numeric columns.")
        else:
            correlation_matrix = numeric_df.corr()
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(correlation_matrix,annot=True,fmt=".2f",ax=ax,cmap="Blues")
            st.pyplot(fig)

    with tab3:
        categorical_df = df.select_dtypes(include=["object", "category"])
        if categorical_df.shape[1] == 0:
            st.info("⚠️ No categorical columns found.")
        else:
            selected_column = st.selectbox("Select a column:",categorical_df.columns,key="categorization_column")
            category_counts = categorical_df[selected_column].value_counts()
            st.write(category_counts)
            fig, ax = plt.subplots(figsize=(10, max(4, len(category_counts) * 0.3)))
            sns.barplot(x=category_counts.values,y=category_counts.index,ax=ax)
            st.pyplot(fig)

    with tab4:
        st.subheader("Create a custom chart")
        col1,col2,col3,col4=st.columns(4)
        chart_type=col1.selectbox("Chart type",["Scatter","Line","Bar","Hist"])
        x_axis=col2.selectbox("X-axis",df.columns)
        y_axis=col3.selectbox("Y-axis",df.columns)
        hue=col4.selectbox("hue",["None"] + list(df.columns))
        custom_chart(df,chart_type,x_axis,y_axis,hue)




def filter_and_download(df):
    st.divider()
    st.subheader("Filter and Download")

    col1, col2 = st.columns(2)
    filter_column = col1.selectbox(
        "Select a column to filter:",
        df.columns,
        key="filter_column"
    )

    column_data = df[filter_column]

    if is_numeric(df, filter_column):
        numeric_values = column_data.dropna()

        if numeric_values.empty:
            st.info("No numeric values available to filter.")
            mask = pd.Series(False, index=df.index, dtype=bool)

        else:
            min_val = float(numeric_values.min())
            max_val = float(numeric_values.max())

            if min_val < max_val:
                selected_range = col2.slider(
                    "Select range:",
                    min_value=min_val,
                    max_value=max_val,
                    value=(min_val, max_val),
                    key=f"filter_range_{filter_column}"
                )

                mask = column_data.between(
                    selected_range[0],
                    selected_range[1]
                ).fillna(False)

            else:
                st.info("This column has only one unique value.")
                mask = column_data.notna()

    else:
        unique_vals = column_data.dropna().unique().tolist()

        selected_vals = col2.multiselect(
            "Select values:",
            unique_vals,
            default=unique_vals,
            key=f"filter_values_{filter_column}"
        )

        mask = column_data.isin(selected_vals)

    if column_data.isna().any():
        include_missing = col2.checkbox(
            "Include rows with missing values",
            value=False,
            key=f"include_missing_values_{filter_column}"
        )

        if include_missing:
            mask = mask | column_data.isna()

    filtered_df = df[mask]

    st.caption(
        f"Filtered rows: {filtered_df.shape[0]} / {df.shape[0]}"
    )

    st.dataframe(filtered_df, use_container_width=True)

    st.download_button(
        "⬇️ Download filtered data (CSV)",
        data=filtered_df.to_csv(index=False).encode("utf-8-sig"),
        file_name="filtered_data.csv",
        mime="text/csv",
        use_container_width=True
    )




if __name__=="__main__":
    st.set_page_config(page_title="CSV Lens",
                   page_icon="assets/csv_lens.png",
                   layout='centered',
                   initial_sidebar_state='auto')

    st.title('CSV Lens')
    st.subheader('Interactive CSV Analyzer')

    uploaded_file=st.file_uploader(label="upload your csv file",type='csv')
    st.caption("Don't have a CSV?")
    use_sample = st.button("📄 Try with a sample file", use_container_width=True)

    if use_sample:
        st.session_state["use_sample"] = True

    df = None

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state["use_sample"] = False
        except Exception as e:
            st.error(f"Error reading file: {e}")
            df = None

    elif st.session_state.get("use_sample", False):
        try:
            df = pd.read_csv("./data/sample.csv")
        except Exception as e:
            st.error(f"Sample file not found: {e}")
            df = None


    if df is not None:
        dataset_overview(df)
        descriptive_statistics(df)
        data_analysis(df)
        filter_and_download(df)

