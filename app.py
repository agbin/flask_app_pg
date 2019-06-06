from flask_app import app
import db

import views.phone_numbers


db.init_pool(app)


if __name__ == "__main__":
    app.run(debug=True)
