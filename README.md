🔹 How does the code work?
A GUI is created (Tkinter)

A window size is set (700x600), but it opens in full screen mode.
A videophone (animated background image) is used.
City Input Field (cityField) is processed , where the user enters the name of the city.
The "View weather" button, which calls the get_weather() function.
Getting weather data via OpenWeather API

A request to the openweathermap.org API with the passed city is formed.
The following is extracted from the received JSON response:
🌡 Temperature
🌤 Weather description (clear, cloudy, etc.)
🖼 Weather icon (loaded from the API and displayed in the UI).
Text animation

The animate_text() function gradually displays text on the screen.
Translucent panels

Two translucent rectangles are created:
Top panel with input field and button.
The bottom panel with weather information.
Weather data output

Text with temperature and weather description.
Weather icon.
