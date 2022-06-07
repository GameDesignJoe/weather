from flask import Flask, render_template, request
import weather_data

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def weather_in_city():
    if request.method == 'POST':
        city_name = request.form.get('city')
        location = weather_data.find_lat_long_of_city(city_name)
        return render_template('weather_results.html', location=location)
    return render_template('weather_in_city.html')


if __name__ == '__main__':
    app.run()