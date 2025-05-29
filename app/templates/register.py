<!-- templates/register.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Register</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <h2>Register</h2>
    
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
          {% for message in messages %}
            <li>{{ message }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
    <form method="POST" action="{{ url_for('main.register') }}">
        <label for="name">Name:</label><br>
        <input type="text" name="name" id="name" required><br><br>
        
        <label for="email">Email:</label><br>
        <input type="email" name="email" id="email" required><br><br>
        
        <label for="password">Password:</label><br>
        <input type="password" name="password" id="password" required><br><br>
        
        <button type="submit">Register</button>
    </form>
</body>
</html>

