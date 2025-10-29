from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock employee data (same as before)
employees = [
    {"id": 1, "name": "Kevin", "role": "Developer", "photo": "https://randomuser.me/api/portraits/men/32.jpg"},
    {"id": 2, "name": "Kim", "role": "QA Engineer", "photo": "https://randomuser.me/api/portraits/women/44.jpg"},
    {"id": 3, "name": "J.Mcgill", "role": "Product Manager", "photo": "https://randomuser.me/api/portraits/men/45.jpg"},
    {"id": 4, "name": "Mike", "role": "UX Designer", "photo": "https://randomuser.me/api/portraits/women/68.jpg"}
]

@app.route('/')
def landing():
    # Company info for landing page
    company = {
        "name": "Arclight Solutions",
        "tagline": "People-first tech for scalable business",
        "about": (
            "Arclight Solutions is a global technology consultancy focused on building cloud-native "
            "software and operational excellence for mid-sized enterprises. We value clarity, "
            "continuous learning, and measurable impact."
        ),
        "values": ["Customer-first", "Practical innovation", "Transparency", "Team growth"],
        "hero_image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1600&auto=format&fit=crop&ixlib=rb-4.0.3&s=1"
    }
    # show 3 sample employees on landing
    sample_emps = employees[:3]
    return render_template('landing.html', company=company, employees=sample_emps)

@app.route('/employees')
def directory():
    return render_template('directory.html', employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        new_id = max([e["id"] for e in employees] or [0]) + 1
        # default placeholder photo
        photo = request.form.get('photo') or "https://randomuser.me/api/portraits/lego/1.jpg"
        employees.append({"id": new_id, "name": name, "role": role, "photo": photo})
        return redirect(url_for('directory'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    global employees
    employees = [emp for emp in employees if emp["id"] != id]
    return redirect(url_for('directory'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
