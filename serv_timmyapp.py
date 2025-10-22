{% extends "base.html" %}
{% block content %}
  <h1>Welcome Home</h1>
  <p>Purple–pink glide mode. Explore the tiles below.</p>
  <div class="divider"></div>
  <div class="grid">
    <div class="tile span-6"><h2>Music</h2><p><a href="{{ url_for('music') }}">Enter Music</a></p></div>
    <div class="tile span-6"><h2>Weather</h2><p><a href="{{ url_for('weather') }}">See Weather</a></p></div>
    <div class="tile span-6"><h2>PEMDAS</h2><p><a href="{{ url_for('pemdas') }}">Practice</a></p></div>
    <div class="tile span-6"><h2>Riddle</h2><p><a href="{{ url_for('riddle') }}">Solve</a></p></div>
    <div class="tile span-12"><h2>Police Corner</h2><p><a href="{{ url_for('police') }}">Community notes</a></p></div>
  </div>
{% endblock %}
