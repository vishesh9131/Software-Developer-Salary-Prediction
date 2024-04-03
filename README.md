
![Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Stack_Overflow_logo.svg/1280px-Stack_Overflow_logo.svg.png)




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

## Run Locally

To use the application, follow these steps:

1. Clone the repository to your local machine:

```
git clone github.com/vishesh9131/Software-Developer-Salary-Prediction.git
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
- `Salar_yprediction.ipynb`: This script, `app.py`, serves as the main file for deploying a Streamlit web application that predicts software developer salaries based on input features such as country, education level, and years of experience. It loads a pre-trained machine learning model and preprocessing steps from a serialized file (`saved_steps.pkl`). The script utilizes the Streamlit library to create an interactive user interface with input fields for selecting country, education level, and experience. Upon clicking the "Calculate Salary" button, the script processes the user inputs, encodes them using pre-trained OneHotEncoder objects (`le_country` and `le_education`), and makes salary predictions using the loaded machine learning model (`regressor_loaded`). Finally, it displays the estimated salary to the user. This file is essential for deploying the software developer salary prediction application via Streamlit, providing an intuitive interface for users to interact with.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.






## License

This project is licensed under the [MIT License](LICENSE).


You can copy this Markdown content and save it as `README.md` in your project directory.
## Authors

- [@Vishesh9131](https://github.com/vishesh9131)

