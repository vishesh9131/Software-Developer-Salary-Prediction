

# Software Developer Salary Prediction

This project aims to predict the salary of software developers based on their country, education level, and years of experience. It utilizes machine learning techniques and is deployed as a Streamlit web application.

# Stack Overflow 

This project predicts the salary of software developers using the Stack Overflow Developer Survey dataset. The dataset contains a wealth of information about developers, including their demographics, education, experience, and salaries.

## Dataset

The Stack Overflow Developer Survey dataset is used for this project. It provides valuable insights into the developer community, with thousands of responses collected annually. The dataset typically includes various features such as:

- Country
- Education level
- Years of coding experience
- Employment status
- Company size
- Salary

## Usage

To use the application, follow these steps:

1. Clone the repository to your local machine:

```
git clone <repository_url>
```

2. Navigate to the project directory:

```
cd Software-Developer-Salary-Prediction
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run the Streamlit application:

```
streamlit run app.py
```

5. Access the application in your web browser. By default, it should be available at `http://localhost:8501`.

## Features

- **Input Fields**: Users can input their country, education level, and years of experience through interactive widgets.
- **Prediction**: The application provides an estimated salary based on the provided inputs using a machine learning model.
- **User-Friendly Interface**: The user interface is designed to be intuitive and easy to use.

## Dependencies

- Python 3.x
- Streamlit
- NumPy
- Pandas
- Scikit-learn

## File Structure

- `app.py`: The main Streamlit application file.
- `saved_steps.pkl`: A serialized file containing the trained machine learning model and preprocessing steps.
- `requirements.txt`: A file listing all the required dependencies for the project.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


You can copy this Markdown content and save it as `README.md` in your project directory.
