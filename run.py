from flaskblog import create_app

#Now it uses default cfg class. But, we could
#pass in here some another configuration class
app = create_app()

if __name__ == '__main__':
	app.run(debug=True)