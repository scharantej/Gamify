
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def homepage():
    """Display the home page."""

    # Render the index.html template
    return render_template('index.html')

# Define the route for the configuration page
@app.route('/config')
def config_page():
    """Display the configuration page."""

    # Render the config.html template
    return render_template('config.html')

# Define the route for saving the configuration settings
@app.route('/save_settings', methods=['POST'])
def save_settings():
    """Save the configuration settings."""

    # Get the form data
    settings = request.form

    # Process and save the settings
    save_settings_to_file(settings)

    # Redirect to the confirmation page
    return redirect(url_for('confirmation_page'))

# Define the route for the confirmation page
@app.route('/confirmation')
def confirmation_page():
    """Display the confirmation page."""

    # Render the confirmation.html template
    return render_template('confirmation.html')

# Function to save the configuration settings to a file
def save_settings_to_file(settings):
    """Save the configuration settings to a file."""

    # Open the configuration file
    with open('config.ini', 'w') as f:
        # Write the settings to the file
        for key, value in settings.items():
            f.write(f'{key} = {value}\n')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
