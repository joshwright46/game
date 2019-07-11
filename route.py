from flask import Flask, render_template


app = Flask(__name__)    

@app.route('/')          
def begin_race():
    return render_template('index.html')

########## Start Race Branch ##########
@app.route('/race_track')
def race_track():
  return render_template('race_track.html')

@app.route('/street_race')
def street_track():
  return render_template('street_race.html')

@app.route('/start_race')
def start_race():
  return render_template('start_race.html')

@app.route('/race_car')
def race_car():
  return render_template('race_car.html')

@app.route('/street_car')
def street_car():
  return render_template('street_car.html')

@app.route('/you_win')
def you_win():
  return render_template('you_win.html')

@app.route('/you_lose')
def you_lose():
  return render_template('you_lose.html')




########## No Race Branch ##########
@app.route('/no_race')
def no_race():
  return render_template('no_race.html')



if __name__=="__main__":      
    app.run(debug=True)    
