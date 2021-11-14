from flask import Flask, render_template, request, url_for, redirect
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		birthday = request.form["birthday"]
		birthtime = request.form["birthtime"]
		print(birthday, birthtime)
		return redirect(url_for("stats", birthday=birthday, birthtime=birthtime))

	return render_template("index.html")


@app.route('/stats')
def stats():
	birthday = request.args.get("birthday")
	birthtime = request.args.get("birthtime")
	print(birthday)
	print(birthtime)

	birthdatetime = birthday+" "+birthtime
	then = datetime.datetime.strptime(birthdatetime, "%Y-%m-%d %H:%M")
	now = datetime.datetime.now()

	elapsed_time = now-then
	seconds = elapsed_time.total_seconds()
	days = seconds/(60*60*24)
	print(days)

	return render_template("stats.html", days=days)

if __name__ == "__main__":
	app.run(debug=True)