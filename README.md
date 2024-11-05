# Covid-19 Dashboard

## Overview
The Covid-19 Dashboard is a web application built using Dash, Plotly, and Bootstrap that visualizes Covid-19 data. The application provides insights into total cases, active cases, recovered cases, deaths, and detailed statistics based on user-selected criteria. Users can explore trends over time and view case distributions by age group and state.

## Features
- Displays total, active, recovered, and death cases in a visually appealing card format.
- Interactive line graph showing the daily confirmed cases over time.
- Bar chart visualizing the number of cases across different age groups.
- Dynamic bar chart that updates based on user-selected patient statuses.
- Responsive design using Bootstrap for a seamless user experience.

## Technologies Used
- Python
- Dash
- Plotly
- Pandas
- Bootstrap
- Font Awesome for icons

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
2. Install the required packages
  ```bash
  pip install dash plotly pandas
  ```
3. Download the necessary CSV files ( **IndividualDetails.csv**, **covid_19_india.csv**, **AgeGroupDetails.csv** ) and place them in the project directory.

## Usage
1. Run the Dash application
      ```bash
      python app.py
      ```
2. Open your web browser and go to **http://127.0.0.1:8050** to view the dashboard.

## Code Structure
- **app.py:** Main application code.
- **IndividualDetails.csv:** Contains individual patient details.
- **covid_19_india.csv:** Contains Covid-19 confirmed cases data.
- **AgeGroupDetails.csv:** Contains case distribution data by age group.

## Customization
- You can customize the appearance of the dashboard by modifying the CSS classes and styles in the **app.py** file.
- To add more features, explore the Plotly documentation for additional graph types and customization options.

## View 
https://github.com/user-attachments/assets/8ec7c3b7-fef8-474f-a9a6-403271f366f8



  
