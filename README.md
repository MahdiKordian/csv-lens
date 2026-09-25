# 📊 CSV Lens — Interactive CSV Analyzer

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)

**CSV Lens** is an interactive web-based CSV analysis tool built with **Python** and **Streamlit**.

It lets you upload a CSV dataset, explore its structure, review statistics, visualize data, apply filters, and export the results — all through a clean, no-code interface.

The project is designed to make common data-exploration tasks easier without requiring users to write analysis code for every operation.

## 🚀 Live Demo

The app is deployed on **Streamlit Community Cloud** — try it live, no installation needed:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://csv-lens.streamlit.app)


---

## ✨ Features

### 📁 Data Upload

- Upload your own CSV file directly through the web interface.
- Use a built-in sample dataset to explore the app instantly.
- Automatically load and inspect uploaded data.

### 🔎 Dataset Overview

Get a quick overview of your dataset, including:

- Number of rows and columns
- Missing values and missing-value percentages
- Data types and unique values per column
- Column-level information at a glance

### 📈 Descriptive Statistics

Analyze numerical columns with common statistical measures:

- Mean and median
- Standard deviation
- Minimum and maximum values
- Quartiles
- Other summary statistics provided by Pandas

### 📊 Data Visualization

Explore your data through several visualization options:

- **Distribution** — Histograms for numerical columns and count plots for categorical columns
- **Correlation** — Correlation matrices and heatmaps for numerical variables
- **Categorical Analysis** — Frequency tables and horizontal bar charts
- **Custom Charts** — Scatter, line, and bar charts with hue-based comparisons

### 🎛️ Interactive Filtering

- Filter numerical data using range sliders.
- Filter categorical data using multiselect controls.
- View updated results based on the selected filters.

### 💾 Export Filtered Data

- Download the filtered dataset as a CSV file.
- Export using **UTF-8 with BOM** encoding for better compatibility with applications such as Microsoft Excel.

---

## 🛠️ Tech Stack

| Technology     | Purpose                               |
| -------------- | -------------------------------------- |
| **Python**     | Core programming language              |
| **Streamlit**  | Interactive web application framework  |
| **Pandas**     | Data manipulation and analysis         |
| **Matplotlib** | Data visualization                     |
| **Seaborn**    | Statistical visualization              |

---

## 🚀 Getting Started

### Prerequisites

Python **3.8+** is required.

Check your installed Python version with:

```bash
python --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/MahdiKordian/csv-lens.git
cd csv-lens
```

### 2. Create a Virtual Environment

Creating a virtual environment is recommended to keep the project's dependencies isolated.

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required packages with:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

### 5. Open the App

Streamlit will provide a local URL. The default address is usually:

```text
http://localhost:8501
```

Open the address in your browser to start using CSV Lens.

---

## 📂 Project Structure

```text
csv-lens/
│
├── assets/                 # Images and static assets
├── data/                   # Sample datasets
├── src/                    # Source modules
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
└── LICENSE                 # Project license
```

> The exact contents of `assets/`, `data/`, and `src/` may evolve as the project grows.

---

## 🧩 How It Works

```text
Upload CSV
    ↓
Load Dataset
    ↓
Inspect Dataset
    ↓
Analyze Statistics
    ↓
Visualize Data
    ↓
Apply Filters
    ↓
Export Results
```

This workflow takes you from raw data to interactive exploration without requiring a separate script for each analysis step.

---

## 🎯 Use Cases

CSV Lens can be useful for:

- Quickly exploring an unfamiliar CSV dataset
- Checking data quality and missing values
- Reviewing numerical statistics
- Understanding categorical distributions
- Exploring relationships between numerical variables
- Creating quick visualizations
- Filtering datasets interactively
- Exporting filtered results for further analysis

---

## 🔮 Future Improvements

Possible future improvements include:

- Support for additional file formats
- More visualization types
- Improved data-cleaning tools
- Dataset summary reports
- More advanced filtering options
- Performance improvements for larger datasets

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

To contribute:

1. Fork the repository.
2. Create a new branch:

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add: your feature description"
```

5. Push the branch:

```bash
git push origin feature/your-feature
```

6. Open a Pull Request.

You can also report bugs or suggest improvements through the [Issues page](https://github.com/MahdiKordian/csv-lens/issues).

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

### Mahdi Kordian

*An aspiring **AI Engineer** interested in Python, data analysis, machine learning, and artificial intelligence.*

- **GitHub:** [@MahdiKordian](https://github.com/MahdiKordian)
- **LinkedIn:** [Mahdi Kordian](https://www.linkedin.com/in/mahdikordian/)
- **Telegram:** [@mahdikordian](https://t.me/MahdiKordian/)
- **X:** [@MahdiKordian](https://x.com/MahdiKordian/)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

<p align="center">
  Built with Python 🐍 and Streamlit 🚀
</p>