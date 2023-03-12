from flask import Flask, render_template
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/member')
def sample_file_upload():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs)
    return render_template("auto_answer.html", news=news)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')