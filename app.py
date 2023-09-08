
from flask import Flask,request,jsonify

app =  Flask(__name__)

termek_lista = [
    {
        "ID": 1,
        "termék neve": "Laptop",
        "leírása": "Hordozható számítógép nagy teljesítménnyel.",
        "ára": 359000
    },
    {
        "ID": 2,
        "termék neve": "Okostelefon",
        "leírása": "Modern okostelefon kiváló kamerával.",
        "ára": 199000
    },
    {
        "ID": 3,
        "termék neve": "Televízió",
        "leírása": "Nagy méretű HD televízió.",
        "ára": 300000
    },
    {
        "ID": 4,
        "termék neve": "Kávéfőző",
        "leírása": "Programozható kávéfőző.",
        "ára": 2300
    },
    {
        "ID": 5,
        "termék neve": "Hűtőszekrény",
        "leírása": "Nagy hűtőszekrény energiahatékonysággal.",
        "ára": 199500
    },
    {
        "ID": 6,
        "termék neve": "Mikrohullámú sütő",
        "leírása": "Mikrohullámú sütő gyors ételkészítéshez.",
        "ára": 60000
    },
    {
        "ID": 7,
        "termék neve": "Fényképezőgép",
        "leírása": "DSLR fényképezőgép professzionális felhasználóknak.",
        "ára": 299000
    },
    {
        "ID": 8,
        "termék neve": "Asztali számítógép",
        "leírása": "Erős asztali számítógép játékhoz és munkához.",
        "ára": 516000
    },
    {
        "ID": 9,
        "termék neve": "Vezeték nélküli egér",
        "leírása": "Kényelmes vezeték nélküli egér használathoz.",
        "ára": 9000
    },
    {
        "ID": 10,
        "termék neve": "Hangszóró rendszer",
        "leírása": "Magas minőségű hangszóró rendszer zenehallgatáshoz.",
        "ára": 99000
    }
]

@app.route('/termek',methods=['GET','POST'])
def termek():
    if request.method == 'GET':
        if len(termek_lista)>0:
            return jsonify(termek_lista)
        else:
            'Nem találtam semmit', 404

    if request.method == 'POST':
        uj_termek = request.form['termék neve']
        uj_lairas = request.form['leírás']
        uj_ar = request.form['ára']
        ID = termek_lista[-1] ['ID']+1

    uj_objektum = {
        'ID': ID,
        'termék neve': uj_termek,
        'leírás': uj_lairas,
        'ára':uj_ar
    }

    termek_lista.append(uj_objektum)
    return jsonify(termek_lista), 201

if __name__ == '__main__':
    app.run()