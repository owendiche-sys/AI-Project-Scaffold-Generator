import json
from pathlib import Path

import streamlit as st


PROJECT_TEMPLATES = {
    "classification": {
        "title_suffix": "Classification Project",
        "overview": "This project builds a machine learning classification pipeline, including data preprocessing, exploratory analysis, model training, and evaluation.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_eda.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
scikit-learn
matplotlib
streamlit""",
    },
    "regression": {
        "title_suffix": "Regression Project",
        "overview": "This project builds a machine learning regression workflow for predicting continuous outcomes, covering preprocessing, modelling, and performance evaluation.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_eda.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
scikit-learn
matplotlib
streamlit""",
    },
    "dashboard": {
        "title_suffix": "Analytics Dashboard Project",
        "overview": "This project creates an analytics dashboard for exploring business or operational data, including preprocessing, KPI design, and interactive visualisation.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── preprocess.py
│   └── kpis.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
matplotlib
streamlit""",
    },
    "time_series": {
        "title_suffix": "Time Series Forecasting Project",
        "overview": "This project builds a time series forecasting workflow for predicting future values from historical data, including preprocessing, exploratory analysis, baseline modelling, and evaluation.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_time_series_eda.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
scikit-learn
matplotlib
streamlit""",
    },
    "clustering": {
        "title_suffix": "Clustering Project",
        "overview": "This project builds an unsupervised learning workflow for discovering patterns and segments in data using clustering techniques and exploratory analysis.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_clustering_eda.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
scikit-learn
matplotlib
streamlit""",
    },
    "nlp": {
        "title_suffix": "Natural Language Processing Project",
        "overview": "This project builds a natural language processing workflow for analysing and modelling text data, including preprocessing, feature extraction, and baseline modelling.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_text_eda.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
scikit-learn
matplotlib
streamlit
nltk""",
    },
    "computer_vision": {
        "title_suffix": "Computer Vision Project",
        "overview": "This project builds a computer vision workflow for image classification or analysis, including preprocessing, model training, and evaluation.",
        "folder_structure": """project_name/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── 01_image_eda.ipynb
├── src/
│   ├── preprocess.py
│   ├── train.py
│   └── evaluate.py
├── app/
│   └── app.py
├── outputs/
│   └── figures/
├── README.md
└── requirements.txt""",
        "requirements": """pandas
numpy
matplotlib
streamlit
torch
torchvision""",
    },
}


def get_preprocess_template(project_name: str) -> str:
    return f'''"""
Preprocessing script for {project_name}.
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from CSV."""
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic cleaning logic."""
    df = df.copy()
    df = df.drop_duplicates()
    return df


if __name__ == "__main__":
    print("Preprocessing pipeline ready.")
'''


def get_train_template(project_name: str, project_type: str) -> str:
    if project_type == "classification":
        model_import = "from sklearn.ensemble import RandomForestClassifier"
        model_line = "model = RandomForestClassifier(random_state=42)"
        metric_text = 'print("Training complete for classification model.")'

        return f'''"""
Training script for {project_name}.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
{model_import}


def train_model(df: pd.DataFrame, target_column: str):
    """Train a baseline model."""
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    {model_line}
    model.fit(X_train, y_train)

    return model, X_test, y_test


if __name__ == "__main__":
    {metric_text}
'''

    elif project_type == "regression":
        model_import = "from sklearn.ensemble import RandomForestRegressor"
        model_line = "model = RandomForestRegressor(random_state=42)"
        metric_text = 'print("Training complete for regression model.")'

        return f'''"""
Training script for {project_name}.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
{model_import}


def train_model(df: pd.DataFrame, target_column: str):
    """Train a baseline model."""
    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = pd.get_dummies(X, drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    {model_line}
    model.fit(X_train, y_train)

    return model, X_test, y_test


if __name__ == "__main__":
    {metric_text}
'''

    elif project_type == "time_series":
        return f'''"""
Training script for {project_name}.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


def create_lag_features(df: pd.DataFrame, target_column: str, lags: int = 3) -> pd.DataFrame:
    """Create simple lag features."""
    df = df.copy()
    for lag in range(1, lags + 1):
        df[f"{{target_column}}_lag_{{lag}}"] = df[target_column].shift(lag)
    return df.dropna()


def train_model(df: pd.DataFrame, target_column: str):
    """Train a simple forecasting baseline."""
    df = create_lag_features(df, target_column)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    model = LinearRegression()
    model.fit(X, y)

    return model, X, y


if __name__ == "__main__":
    print("Training complete for time series forecasting model.")
'''

    elif project_type == "clustering":
        return f'''"""
Training script for {project_name}.
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def train_model(df: pd.DataFrame, n_clusters: int = 3):
    """Train a clustering model."""
    X = pd.get_dummies(df, drop_first=True)
    X = X.select_dtypes(include=["number"])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = model.fit_predict(X_scaled)

    return model, X_scaled, clusters


if __name__ == "__main__":
    print("Training complete for clustering model.")
'''

    else:
        raise ValueError(f"Unsupported project type: {project_type}")


def get_evaluate_template(project_name: str, project_type: str) -> str:
    if project_type == "classification":
        metric_import = "from sklearn.metrics import accuracy_score, classification_report"
        metric_code = """predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))"""

    elif project_type == "regression":
        metric_import = "from sklearn.metrics import mean_absolute_error, r2_score"
        metric_code = """predictions = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("R2:", r2_score(y_test, predictions))"""

    elif project_type == "time_series":
        metric_import = "from sklearn.metrics import mean_absolute_error, mean_squared_error"
        metric_code = """predictions = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, predictions))
    print("MSE:", mean_squared_error(y_test, predictions))"""

    elif project_type == "clustering":
        metric_import = "from sklearn.metrics import silhouette_score"
        metric_code = """score = silhouette_score(X_test, y_test)
    print("Silhouette Score:", score)"""

    else:
        raise ValueError(f"Unsupported project type: {project_type}")

    return f'''"""
Evaluation script for {project_name}.
"""

{metric_import}


def evaluate_model(model, X_test, y_test):
    """Evaluate fitted model."""
    {metric_code}
'''


def get_nlp_train_template(project_name: str) -> str:
    return f'''"""
Training script for {project_name}.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def train_model(df: pd.DataFrame, text_column: str, target_column: str):
    """Train a baseline NLP classifier."""
    X = df[text_column].astype(str)
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vec, y_train)

    return model, vectorizer, X_test_vec, y_test


if __name__ == "__main__":
    print("Training complete for NLP model.")
'''


def get_nlp_evaluate_template(project_name: str) -> str:
    return f'''"""
Evaluation script for {project_name}.
"""

from sklearn.metrics import accuracy_score, classification_report


def evaluate_model(model, X_test, y_test):
    """Evaluate NLP model."""
    predictions = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions))
'''


def get_cv_train_template(project_name: str) -> str:
    return f'''"""
Training script for {project_name}.
"""

import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader


def get_data_loaders(data_dir: str, batch_size: int = 32):
    """Create image data loaders."""
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    train_dataset = datasets.ImageFolder(root=data_dir, transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    return train_loader


class SimpleCNN(nn.Module):
    def __init__(self, num_classes: int):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(32 * 32 * 32, num_classes)
        )

    def forward(self, x):
        return self.model(x)


if __name__ == "__main__":
    print("Computer vision training template ready.")
'''


def get_cv_evaluate_template(project_name: str) -> str:
    return f'''"""
Evaluation script for {project_name}.
"""

def evaluate_model(model, test_loader):
    """Placeholder evaluation function."""
    print("Add evaluation logic for the computer vision model.")
'''


def get_dashboard_app_template(project_name: str) -> str:
    return f'''"""
Streamlit app for {project_name}.
"""

import streamlit as st
import pandas as pd

st.set_page_config(page_title="{project_name}", layout="wide")

st.title("{project_name}")
st.write("Interactive dashboard starter template.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Columns")
    st.write(df.columns.tolist())
'''


def get_ml_app_template(project_name: str) -> str:
    return f'''"""
Streamlit app for {project_name}.
"""

import streamlit as st

st.set_page_config(page_title="{project_name}", layout="wide")

st.title("{project_name}")
st.write("Starter interface for presenting results, insights, and model outputs.")
'''


def generate_readme(project_name: str, project_type: str, problem_statement: str) -> str:
    template = PROJECT_TEMPLATES[project_type]
    structure = template["folder_structure"].replace(
        "project_name", project_name.lower().replace(" ", "_")
    )

    tech_stack = ["Python", "Pandas", "NumPy", "Matplotlib", "Streamlit"]

    if project_type in ["classification", "regression", "clustering", "time_series", "nlp"]:
        if "Scikit-learn" not in tech_stack:
            tech_stack.append("Scikit-learn")

    if project_type == "nlp":
        tech_stack.append("NLTK")

    if project_type == "computer_vision":
        tech_stack.extend(["PyTorch", "Torchvision"])

    tech_stack_md = "\n".join(f"- {item}" for item in tech_stack)

    usage_map = {
        "classification": [
            "Place raw data inside the `data/raw/` folder.",
            "Run preprocessing from `src/preprocess.py`.",
            "Train the model with `src/train.py`.",
            "Evaluate performance with `src/evaluate.py`.",
            "Use `app/app.py` to present outputs in Streamlit.",
        ],
        "regression": [
            "Place raw data inside the `data/raw/` folder.",
            "Run preprocessing from `src/preprocess.py`.",
            "Train the regression model with `src/train.py`.",
            "Evaluate predictions with `src/evaluate.py`.",
            "Use `app/app.py` to present outputs in Streamlit.",
        ],
        "dashboard": [
            "Place raw data inside the `data/raw/` folder.",
            "Run preprocessing from `src/preprocess.py`.",
            "Define KPI logic in `src/kpis.py`.",
            "Launch the dashboard through `app/app.py`.",
        ],
        "time_series": [
            "Place historical time series data inside the `data/raw/` folder.",
            "Run preprocessing from `src/preprocess.py`.",
            "Create lag-based forecasting logic in `src/train.py`.",
            "Evaluate forecast error with `src/evaluate.py`.",
            "Use `app/app.py` to present results in Streamlit.",
        ],
        "clustering": [
            "Place raw data inside the `data/raw/` folder.",
            "Run preprocessing from `src/preprocess.py`.",
            "Train the clustering model with `src/train.py`.",
            "Assess clustering quality with `src/evaluate.py`.",
            "Use `app/app.py` to present outputs in Streamlit.",
        ],
        "nlp": [
            "Place text data inside the `data/raw/` folder.",
            "Run preprocessing from `src/preprocess.py`.",
            "Train the NLP model with `src/train.py`.",
            "Evaluate classification performance with `src/evaluate.py`.",
            "Use `app/app.py` to present outputs in Streamlit.",
        ],
        "computer_vision": [
            "Place image data inside the `data/raw/` folder.",
            "Prepare image loaders and transforms in `src/train.py`.",
            "Train the computer vision model.",
            "Add evaluation logic in `src/evaluate.py`.",
            "Use `app/app.py` to present outputs in Streamlit.",
        ],
    }

    usage_steps = "\n".join(
        f"{i + 1}. {step}" for i, step in enumerate(usage_map[project_type])
    )

    return f"""# {project_name}

## Overview

{template["overview"]}

## Problem Statement

{problem_statement}

## Project Structure

```text
{structure}
"""

def generate_project_scaffold(project_name: str, project_type: str, problem_statement: str):
    if project_type not in PROJECT_TEMPLATES:
        raise ValueError(f"Unsupported project type: {project_type}")

    template = PROJECT_TEMPLATES[project_type]
    safe_name = slugify_project_name(project_name)

    starter_files = {
        "src/preprocess.py": get_preprocess_template(project_name),
        "README.md": generate_readme(project_name, project_type, problem_statement),
        "requirements.txt": template["requirements"],
    }

    if project_type in {"classification", "regression", "time_series", "clustering"}:
        starter_files["src/train.py"] = get_train_template(project_name, project_type)
        starter_files["src/evaluate.py"] = get_evaluate_template(project_name, project_type)
        starter_files["app/app.py"] = get_ml_app_template(project_name)

    if project_type == "dashboard":
        starter_files["src/kpis.py"] = '''"""
KPI helper functions.
"""

def calculate_kpis(df):
    """Return basic KPI placeholders."""
    return {
        "rows": len(df),
        "columns": len(df.columns),
    }
'''
        starter_files["app/app.py"] = get_dashboard_app_template(project_name)

    if project_type == "nlp":
        starter_files["src/train.py"] = get_nlp_train_template(project_name)
        starter_files["src/evaluate.py"] = get_nlp_evaluate_template(project_name)
        starter_files["app/app.py"] = get_ml_app_template(project_name)

    if project_type == "computer_vision":
        starter_files["src/train.py"] = get_cv_train_template(project_name)
        starter_files["src/evaluate.py"] = get_cv_evaluate_template(project_name)
        starter_files["app/app.py"] = get_ml_app_template(project_name)

    result = {
        "project_title": f"{project_name} - {template['title_suffix']}",
        "project_type": project_type,
        "overview": template["overview"],
        "folder_structure": template["folder_structure"].replace("project_name", safe_name),
        "readme_md": starter_files["README.md"],
        "requirements_txt": starter_files["requirements.txt"],
        "starter_files": starter_files,
    }

    return result

def save_project_output(result, base_dir="generated_project"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)

    for filepath, content in result["starter_files"].items():
        full_path = base / filepath
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding="utf-8")

    metadata = {
        "project_title": result["project_title"],
        "project_type": result["project_type"],
        "overview": result["overview"],
        "folder_structure": result["folder_structure"],
}

    (base / "project_meta.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
)

st.set_page_config(page_title="AI Project Scaffold Generator", layout="wide")

st.title("AI Project Scaffold Generator")
st.write("Generate starter project structures for data science workflows.")

with st.form("generator_form"):
    project_name = st.text_input(
        "Project name",
        placeholder="e.g. Customer Churn Predictor",
    )
    project_type = st.selectbox(
        "Project type",
        options=[
            "classification",
            "regression",
            "dashboard",
            "time_series",
            "clustering",
            "nlp",
            "computer_vision",
        ],
    )
    problem_statement = st.text_area(
        "Problem statement",
        placeholder="Describe what the project should do...",
        height=120,
    )
    submitted = st.form_submit_button("Generate Project")

if submitted:
    if not project_name.strip() or not problem_statement.strip():
        st.error("Please enter both a project name and a problem statement.")
    else:
        result = generate_project_scaffold(
            project_name=project_name.strip(),
            project_type=project_type,
            problem_statement=problem_statement.strip(),
        )

        st.success("Project scaffold generated.")

        st.subheader("Project Title")
        st.write(result["project_title"])

        st.subheader("Overview")
        st.write(result["overview"])

        st.subheader("Folder Structure")
        st.code(result["folder_structure"], language="text")

        st.subheader("README")
        st.code(result["readme_md"], language="markdown")

        st.subheader("Requirements")
        st.code(result["requirements_txt"], language="text")

        st.subheader("Starter Files")
        for filename, content in result["starter_files"].items():
            with st.expander(filename):
                st.code(content)

        project_folder = slugify_project_name(project_name)
        save_project_output(result, base_dir=project_folder)
        st.info(f"Project files saved locally in: {project_folder}")