### **System Configuration Application for Gaming App (Python Flask Design)**

#### **HTML Files**:

1. **`index.html`**:
   - **Purpose**: Home page of the application, displaying basic information about the system config app and providing a link to the configuration page.
   - **Content**:
     - Welcome message and brief description of the application.
     - Button or link to navigate to the configuration page.


2. **`config.html`**:
   - **Purpose**: Allows the user to configure and adjust system settings for the gaming app.
   - **Content**:
     - Form with various input fields for configuring different settings.
     - Save and Cancel buttons to submit or discard the changes.


3. **`confirmation.html`**:
   - **Purpose**: Displays a confirmation message after the user successfully configures the system settings.
   - **Content**:
     - Confirmation message indicating successful configuration.
     - Link to the home page or the configuration page for further actions.

#### **Routes**:

1. **`Homepage`**:
   - **URL**: Home page of the application, usually "/" or "/index".
   - **Method**: GET
   - **Functionality**: Displays the `index.html` file, presenting the welcome message and link to the configuration page.


2. **`ConfigPage`**:
   - **URL**: URL for the configuration page, such as "/config".
   - **Method**: GET
   - **Functionality**: Retrieves and displays the `config.html` file, allowing the user to adjust and configure the system settings.


3. **`SaveSettings`**:
   - **URL**: Endpoint for saving the configured settings.
   - **Method**: POST
   - **Functionality**: Receives the form data from the `config.html` file, processes it, and saves the settings accordingly.
   - **Response**: Redirects to the `confirmation.html` page.


4. **`ConfirmationPage`**:
   - **URL**: URL for the confirmation page, such as "/confirmation".
   - **Method**: GET
   - **Functionality**: Displays the confirmation message and provides links for further actions.