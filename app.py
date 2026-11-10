from flask import Flask, render_template, request, redirect, session, send_file
import json, os, random, time
from flask import send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__)
app.secret_key = 'secret123'

# ---------- USERS ----------
def load_users():
    if not os.path.exists('students.json'):
        return {}
    with open('students.json', 'r') as f:
        return json.load(f)

def save_users(users):
    with open('students.json', 'w') as f:
        json.dump(users, f)

# ---------- QUESTIONS ----------
def load_questions():
    return {
        "maths": {
            "easy": [
                {"q": "1 + 1 = ?", "options": ["1","2","3"], "ans": "2","skill":"Addition","hint":"Basic addition"},
                {"q": "2 + 3 = ?", "options": ["4","5","6"], "ans": "5","skill":"Addition","hint":"Add"},
                {"q": "5 - 2 = ?", "options": ["2","3","4"], "ans": "3","skill":"Subtraction","hint":"Subtract"},
                {"q": "10 - 5 = ?", "options": ["4","5","6"], "ans": "5","skill":"Subtraction","hint":"Subtract"},
                {"q": "3 + 4 = ?", "options": ["6","7","8"], "ans": "7","skill":"Addition","hint":"Add"},
                {"q": "6 - 1 = ?", "options": ["4","5","6"], "ans": "5","skill":"Subtraction","hint":"Subtract"},
                {"q": "7 - 3 = ?", "options": ["3","4","5"], "ans": "4","skill":"Subtraction","hint":"Subtract"},
                {"q": "4 + 4 = ?", "options": ["6","7","8"], "ans": "8","skill":"Addition","hint":"Add"},
                {"q": "9 - 4 = ?", "options": ["4","5","6"], "ans": "5","skill":"Subtraction","hint":"Subtract"},
                {"q": "8 + 1 = ?", "options": ["8","9","10"], "ans": "9","skill":"Addition","hint":"Add"}
            ],
            "medium": [
                {"q": "5 × 2 = ?", "options": ["10","12","8"], "ans": "10","skill":"Multiplication","hint":"Multiply"},
                {"q": "6 × 3 = ?", "options": ["18","16","12"], "ans": "18","skill":"Multiplication","hint":"Multiply"},
                {"q": "10 ÷ 2 = ?", "options": ["4","5","6"], "ans": "5","skill":"Division","hint":"Divide"},
                {"q": "12 ÷ 3 = ?", "options": ["3","4","5"], "ans": "4","skill":"Division","hint":"Divide"},
                {"q": "4 × 5 = ?", "options": ["20","25","15"], "ans": "20","skill":"Multiplication","hint":"Multiply"},
                {"q": "9 × 2 = ?", "options": ["18","16","20"], "ans": "18","skill":"Multiplication","hint":"Multiply"},
                {"q": "15 ÷ 3 = ?", "options": ["4","5","6"], "ans": "5","skill":"Division","hint":"Divide"},
                {"q": "16 ÷ 4 = ?", "options": ["3","4","5"], "ans": "4","skill":"Division","hint":"Divide"},
                {"q": "7 × 3 = ?", "options": ["20","21","18"], "ans": "21","skill":"Multiplication","hint":"Multiply"},
                {"q": "18 ÷ 2 = ?", "options": ["8","9","10"], "ans": "9","skill":"Division","hint":"Divide"}
            ],
            "hard": [
                {"q": "25 ÷ 5 = ?", "options": ["5","4","6"], "ans": "5","skill":"Division","hint":"Divide"},
                {"q": "12 × 4 = ?", "options": ["48","40","36"], "ans": "48","skill":"Multiplication","hint":"Multiply"},
                {"q": "20 ÷ 4 = ?", "options": ["4","5","6"], "ans": "5","skill":"Division","hint":"Divide"},
                {"q": "9 × 5 = ?", "options": ["45","40","50"], "ans": "45","skill":"Multiplication","hint":"Multiply"},
                {"q": "30 ÷ 6 = ?", "options": ["4","5","6"], "ans": "5","skill":"Division","hint":"Divide"},
                {"q": "11 × 3 = ?", "options": ["33","30","36"], "ans": "33","skill":"Multiplication","hint":"Multiply"},
                {"q": "24 ÷ 6 = ?", "options": ["3","4","5"], "ans": "4","skill":"Division","hint":"Divide"},
                {"q": "14 × 2 = ?", "options": ["26","28","30"], "ans": "28","skill":"Multiplication","hint":"Multiply"},
                {"q": "27 ÷ 3 = ?", "options": ["8","9","10"], "ans": "9","skill":"Division","hint":"Divide"},
                {"q": "8 × 6 = ?", "options": ["48","42","50"], "ans": "48","skill":"Multiplication","hint":"Multiply"}
            ]
        },

        "english": {
            "easy": [
                {"q": "Opposite of hot?", "options": ["Cold","Warm","Heat"], "ans": "Cold","skill":"Vocabulary","hint":"Temperature"},
                {"q": "Opposite of big?", "options": ["Small","Large","Huge"], "ans": "Small","skill":"Vocabulary","hint":"Size"},
                {"q": "Opposite of day?", "options": ["Night","Evening","Morning"], "ans": "Night","skill":"Vocabulary","hint":"Time"},
                {"q": "Plural of cat?", "options": ["Cats","Cat","Cates"], "ans": "Cats","skill":"Grammar","hint":"Add s"},
                {"q": "Opposite of fast?", "options": ["Slow","Quick","Speed"], "ans": "Slow","skill":"Vocabulary","hint":"Speed"},
                {"q": "Opposite of up?", "options": ["Down","Above","Top"], "ans": "Down","skill":"Vocabulary","hint":"Direction"},
                {"q": "Plural of dog?", "options": ["Dogs","Dog","Doges"], "ans": "Dogs","skill":"Grammar","hint":"Add s"},
                {"q": "Opposite of happy?", "options": ["Sad","Joy","Smile"], "ans": "Sad","skill":"Vocabulary","hint":"Emotion"},
                {"q": "Opposite of open?", "options": ["Close","Start","Begin"], "ans": "Close","skill":"Vocabulary","hint":"Door"},
                {"q": "Plural of book?", "options": ["Books","Book","Bookes"], "ans": "Books","skill":"Grammar","hint":"Add s"}
            ],

            "medium": [
                {"q": "Synonym of happy?", "options": ["Joyful","Sad","Angry"], "ans": "Joyful","skill":"Vocabulary","hint":"Positive"},
                {"q": "Synonym of big?", "options": ["Large","Tiny","Short"], "ans": "Large","skill":"Vocabulary","hint":"Size"},
                {"q": "Synonym of fast?", "options": ["Quick","Slow","Late"], "ans": "Quick","skill":"Vocabulary","hint":"Speed"},
                {"q": "Past of go?", "options": ["Went","Go","Gone"], "ans": "Went","skill":"Grammar","hint":"Past tense"},
                {"q": "Past of eat?", "options": ["Ate","Eat","Eated"], "ans": "Ate","skill":"Grammar","hint":"Past tense"},
                {"q": "Synonym of small?", "options": ["Tiny","Huge","Big"], "ans": "Tiny","skill":"Vocabulary","hint":"Size"},
                {"q": "Past of run?", "options": ["Ran","Run","Runned"], "ans": "Ran","skill":"Grammar","hint":"Past tense"},
                {"q": "Synonym of smart?", "options": ["Intelligent","Dull","Slow"], "ans": "Intelligent","skill":"Vocabulary","hint":"Brain"},
                {"q": "Past of write?", "options": ["Wrote","Write","Written"], "ans": "Wrote","skill":"Grammar","hint":"Past tense"},
                {"q": "Synonym of angry?", "options": ["Mad","Happy","Calm"], "ans": "Mad","skill":"Vocabulary","hint":"Emotion"}
            ],

            "hard": [
                {"q": "Correct spelling?", "options": ["Receive","Recieve","Receeve"], "ans": "Receive","skill":"Grammar","hint":"i before e"},
                {"q": "Correct spelling?", "options": ["Separate","Seperate","Separete"], "ans": "Separate","skill":"Grammar","hint":"Spelling"},
                {"q": "Choose correct sentence?", "options": ["She has done it","She have done it","She did done it"], "ans": "She has done it","skill":"Grammar","hint":"Grammar"},
                {"q": "Choose correct word?", "options": ["Their","There","They"], "ans": "Their","skill":"Grammar","hint":"Possession"},
                {"q": "Choose correct word?", "options": ["Your","You","You're"], "ans": "Your","skill":"Grammar","hint":"Possession"},
                {"q": "Correct spelling?", "options": ["Environment","Enviroment","Envirnment"], "ans": "Environment","skill":"Grammar","hint":"Spelling"},
                {"q": "Choose correct sentence?", "options": ["He is taller than me","He is tall than me","He taller me"], "ans": "He is taller than me","skill":"Grammar","hint":"Comparison"},
                {"q": "Choose correct word?", "options": ["Its","It's","It"], "ans": "It's","skill":"Grammar","hint":"Contraction"},
                {"q": "Correct spelling?", "options": ["Beautiful","Beautifull","Beautifull"], "ans": "Beautiful","skill":"Grammar","hint":"Spelling"},
                {"q": "Choose correct sentence?", "options": ["I have finished","I has finished","I finishing"], "ans": "I have finished","skill":"Grammar","hint":"Grammar"}
            ]
        }
    }

# ---------- ROUTES ----------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        users=load_users()
        users[request.form['email']] = {
            "name":request.form['name'],
            "password":request.form['password']
        }
        save_users(users)
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        users=load_users()
        email=request.form['email']
        pwd=request.form['password']
        if email in users and users[email]['password']==pwd:
            session['user']=email
            return redirect('/dashboard')
        return "Invalid login"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    users = load_users()
    name = users[session['user']]['name']
    return render_template('dashboard.html', name=name)

# ---------- START QUIZ ----------
@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    if 'user' not in session:
        return redirect('/login')

    session['subject'] = request.form.get('subject')
    session['level'] = request.form.get('level')

    # RESET
    session['score'] = 0
    session['history'] = []
    session['skills'] = {}
    session['asked'] = []
    session['correct_streak'] = 0
    session['total_questions'] = 0
    session['skipped'] = 0
    session['hints_used'] = 0
    session['start_time'] = time.time()

    return redirect('/tutor')

# ---------- TUTOR ----------
@app.route('/tutor', methods=['GET', 'POST'])
def tutor():

    if 'subject' not in session:
        return redirect('/dashboard')

    data = load_questions()[session['subject']]

    session.setdefault('level', 'easy')
    session.setdefault('score', 0)
    session.setdefault('history', [])
    session.setdefault('skills', {})
    session.setdefault('asked', [])
    session.setdefault('correct_streak', 0)
    session.setdefault('total_questions', 0)
    session.setdefault('skipped', 0)
    session.setdefault('hints_used', 0)

    level = session['level']

    # ---------------- POST ----------------
    if request.method == 'POST':

        current_q = session.get('current_q')

        if 'skip' in request.form:
            session['skipped'] += 1
            session['total_questions'] += 1

        else:
            selected = request.form.get('answer')

            if selected:
                correct = current_q['ans']
                skill = current_q['skill']

                is_correct = selected == correct

                # SAVE HISTORY PROPERLY
                session['history'].append({
                    "question": current_q['q'],
                    "selected": selected,
                    "correct": correct,
                    "result": "Correct" if is_correct else "Wrong"
                })

                # SKILL TRACK
                if skill not in session['skills']:
                    session['skills'][skill] = {"correct": 0, "wrong": 0}

                if is_correct:
                    session['score'] += 1
                    session['skills'][skill]["correct"] += 1
                    session['correct_streak'] += 1
                else:
                    session['skills'][skill]["wrong"] += 1
                    session['correct_streak'] = 0

                # CALCULATE SCORE
                c = session['skills'][skill]["correct"]
                w = session['skills'][skill]["wrong"]

                session['skills'][skill]["score"] = round(c / (c + w), 2)

                # LEVEL CHANGE
                if is_correct and session['correct_streak'] == 3:
                    if session['level'] == 'easy':
                        session['level'] = 'medium'
                    elif session['level'] == 'medium':
                        session['level'] = 'hard'
                    session['correct_streak'] = 0

                if not is_correct:
                    if session['level'] == 'hard':
                        session['level'] = 'medium'
                    elif session['level'] == 'medium':
                        session['level'] = 'easy'

                session['total_questions'] += 1

        session.modified = True

        # END QUIZ AFTER 10 QUESTIONS
        if session['total_questions'] >= 10:
            return redirect('/feedback')

        return redirect('/tutor')

    # ---------------- GET ----------------
    questions = data[level]

    remaining = [q for q in questions if q['q'] not in session['asked']]

    if not remaining:
        session['asked'] = []
        remaining = questions

    question = random.choice(remaining)

    session['current_q'] = question
    session['asked'].append(question['q'])

    return render_template('tutor.html', q=question, level=level, timer=15)

# ---------- FEEDBACK ----------
@app.route('/feedback')
def feedback():

    score = session.get('score', 0)
    total = session.get('total_questions', 0)
    skipped = session.get('skipped', 0)

    attempted = total - skipped
    accuracy = round((score / attempted) * 100, 2) if attempted > 0 else 0

    return render_template(
        'feedback.html',
        score=score,
        total=total,
        skipped=skipped,
        accuracy=accuracy
    )

# ---------- PROGRESS ----------
@app.route('/progress')
def progress():

    history = session.get('history', [])
    score = session.get('score', 0)
    total = session.get('total_questions', 0)
    skipped = session.get('skipped', 0)

    attempted = total - skipped
    accuracy = round((score / attempted) * 100, 2) if attempted > 0 else 0

    time_spent = round(time.time() - session.get('start_time', time.time()), 2)

    return render_template(
        'progress.html',
        skills=session.get('skills', {}),
        history=history,
        score=score,
        total=total,
        skipped=skipped,
        accuracy=accuracy,
        time_spent=time_spent
    )
@app.route('/download')
def download():

    file_path = "report.pdf"

    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    elements = []

    score = session.get('score', 0)
    total = session.get('total_questions', 0)
    skipped = session.get('skipped', 0)

    attempted = total - skipped
    accuracy = round((score / attempted) * 100, 2) if attempted > 0 else 0

    elements.append(Paragraph("Quiz Report", styles['Title']))
    elements.append(Spacer(1, 10))

    elements.append(Paragraph(f"Total Questions: {total}", styles['Normal']))
    elements.append(Paragraph(f"Correct Answers: {score}", styles['Normal']))
    elements.append(Paragraph(f"Skipped: {skipped}", styles['Normal']))
    elements.append(Paragraph(f"Accuracy: {accuracy}%", styles['Normal']))

    elements.append(Spacer(1, 10))
    elements.append(Paragraph("Skill Analysis:", styles['Heading2']))

    for skill, data in session.get('skills', {}).items():
        elements.append(Paragraph(
            f"{skill}: {data.get('score', 0)}",
            styles['Normal']
        ))

    doc.build(elements)

    return send_file(file_path, as_attachment=True)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)