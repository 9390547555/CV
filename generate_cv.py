from fpdf import FPDF

class ModernCV(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Curriculum Vitae', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_cv(filename):
    pdf = ModernCV()
    pdf.add_page()

    # Add profile section
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Profile', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, 'As a forward-thinking agriculture bachelor student currently pursuing a master\'s degree in climate science policy, I am passionate about leveraging my interdisciplinary background to thrive in the corporate arena. With a track record of effective leadership and a commitment to driving sustainable change, I am eager to contribute my unique perspective and skills to a dynamic corporate environment.', 0, 1)

    # Add contact information
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Contact', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, 'Phone: 9390547144', 0, 1)
    pdf.cell(0, 10, 'LinkedIn: linkedin.com/in/sampath-ganesh-gudapati-7755a6251', 0, 1)
    pdf.cell(0, 10, 'Email: Sampathgudapati465@gmail.com', 0, 1)
    pdf.cell(0, 10, 'Address: TERI SAS, New Delhi, 110070', 0, 1)

    # Add hobbies
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Hobbies', 0, 1)
    pdf.set_font('Arial', '', 12)
    hobbies = ['Exploring sustainable Gardening', 'Enjoying movies', 'Playing Badminton', 'Tuning into Podcasts And songs']
    for hobby in hobbies:
        pdf.cell(0, 10, f'- {hobby}', 0, 1)

    # Add internship experience
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Internship Experience', 0, 1)
    pdf.set_font('Arial', '', 12)
    internships = [
        'ICRISAT [INTERN]\n08 June 2022–21 October 2022\nCompleted project work on water balance components and watershed approach, Geoinformatics, and some experiments on soil physics and soil chemistry, and Agrometeorology. MEMBER IN THE PROJECT OF THE “MOBILE SOIL -TESTING LABORATORY LAUNCH BY LARUS LAB ICRISAT”.',
        'Student intern in Organic Growers By PMKVY.'
    ]
    for internship in internships:
        pdf.multi_cell(0, 10, internship)

    # Add education
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Education', 0, 1)
    pdf.set_font('Arial', '', 12)
    education = [
        'TERI School of Advanced Studies (TERI SAS)\nAugust-10-2023-Expected graduation 2025\nCurrent C.GPA-6.89 as of the first semester.\nRelevant Coursework:\n- Climate Change Science and Policy\n- Environmental Economics\n- Sustainable Development Strategies\n- Climate Modeling and Analysis',
        'Centurion University Technology Management (Odisha, India)\nSeptember 2019 – April 2023\nAgricultural BSC (HONS)- C.GPA-7.89\n- Core Student Committee Member: Organized diverse events and initiatives within CSAR.\n- National Service Scheme (NSS) Team Lead: Spearheaded community service projects and initiatives.\n- Participant, Krishi Mela: Engaged in agricultural exhibitions and discussions on sustainable practices.',
        'Sri Tirumala Junior College (Rajahmundry, Andhra Pradesh)\nBoard of Intermediate Education (2017-2019)\nCGPA-8.8.',
        'Vidya Vikas International School (Jangareddygudem, A.P)\nBoard of Secondary Education (2016-2017)\nCGPA-9.0'
    ]
    for edu in education:
        pdf.multi_cell(0, 10, edu)

    # Add skills
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Skills', 0, 1)
    pdf.set_font('Arial', '', 12)
    skills = ['Python', 'Java', 'C++', 'Machine Learning', 'Web Development', 'Microsoft Office Suite']
    for skill in skills:
        pdf.cell(0, 10, f'- {skill}', 0, 1)

    pdf.output(filename)

# Generate CV
create_cv('trendy_cv.pdf')
