import os

from flask_sqlalchemy import SQLAlchemy
from app import app, request, platform, flask, render_template
from traits.number import percentToFloat
from gsp import GSP


# Home
@app.route("/", methods=['GET'])
def index():
    title = "Ikhtisar"
    greeting = "Wellcome to my first project to learn Flask in Python."
    pythonSystemVersion = platform.python_version()
    flaskAppVersion = flask.__version__
    data = {
        "content": "home.jinja",
        "title": title,
        "greeting": greeting,
        "python_system_version": pythonSystemVersion,
        "flask_app_version": flaskAppVersion,
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/generalized-sequential-pattern-calculation-result", methods=['GET'])
def generalized_sequential_pattern_calculation_result():
    title = "Hasil perhitungan Generalized Sequential Pattern (GSP)"
    app.logger.info('%s is the title.', title)

    # Dates
    startDate = request.args.get('tanggal_awal')
    endDate = request.args.get('tanggal_akhir')

    # Minimal support
    minSupport = request.args.get('min_support') if (request.args.get('min_support')) else 10

    #transactions = [
    #    ["a", "b", "c", frozenset(["c", "d"]), "d"],
    #    ["a", "a", "b", frozenset(["c", "d"]), 'c'],
    #    ["a", "a"]
    #]

    transactions = [
        [
            frozenset({'sv'}), frozenset({'x'}), frozenset({'+', 'qo', 'sv'}), frozenset({'sv'}), frozenset({'x'}), frozenset({'sd', 'sv'}), frozenset({'%', 'sd', 'sv'}), frozenset({'b'}), frozenset({'+', 'sd'}), frozenset({'sv'}), frozenset({'+'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'%', 'aa'}), frozenset({'+', 'sv'}), frozenset({'b'}), frozenset({'sv'}), frozenset({'b'}), frozenset({'+', 'sv(^q)'}), frozenset({'aa'}), frozenset({'+', '^q', 'qh'}), frozenset({'aa'}), frozenset({'sv'}), frozenset({'sv'}), frozenset({'+', 'sv'}), frozenset({'%', 'sd', 'sv', 'sv^r'}), frozenset({'^q', 'qh', 'sd', 'sv', 'sv(^q)'}), frozenset({'aa'}), frozenset({'+'}), frozenset({'aa', 'sv'}), frozenset({'sd'}), frozenset({'bf'}), frozenset({'aa', 'sd'}), frozenset({'b^m'}), frozenset({'+'}), frozenset({'b'}), frozenset({'%', 'o', 'qy'}), frozenset({'qr'}), frozenset({'b', 'sd'}), frozenset({'%'}), frozenset({'+'}), frozenset({'x'}), frozenset({'+', 'sd'}), frozenset({'^2'}), frozenset({'sd'}), frozenset({'%'}), frozenset({'+', 'sd'}), frozenset({'b'}), frozenset({'+'}), frozenset({'aa', 'sd', 'sv'}), frozenset({'aa', 'sd'}), frozenset({'b'}), frozenset({'^q', 'sd(^q)'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'b', 'qw'}), frozenset({'sd'}), frozenset({'b', 'ba'}), frozenset({'aa', 'sd^t'}), frozenset({'x'}), frozenset({'+'}), frozenset({'x'}), frozenset({'+'}), frozenset({'b'}), frozenset({'+', 'sd^t'}), frozenset({'b'}), frozenset({'sd^t'}), frozenset({'bk'})
        ],
        [
            frozenset({'sd', 'sd^t'}), frozenset({'ba'}), frozenset({'b', 'sd^t'}), frozenset({'ba'}), frozenset({'sv^t'}), frozenset({'aa'}), frozenset({'ad'}), frozenset({'^h', 'aa'}), frozenset({'x'}), frozenset({'sd'}), frozenset({'aa', 'sv'}), frozenset({'sd'}), frozenset({'+'}), frozenset({'aa', 'sd'}), frozenset({'%'}), frozenset({'^h', 'sd'}), frozenset({'aa'}), frozenset({'+', '^h', 'sd', 't1'}), frozenset({'b'}), frozenset({'%'}), frozenset({'qy'}), frozenset({'sd'}), frozenset({'b', 'bf'}), frozenset({'qw', 'sd'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'b', 'b^r', 'sd'}), frozenset({'x'}), frozenset({'+'}), frozenset({'b'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'sv'}), frozenset({'sd'}), frozenset({'sv'}), frozenset({'+'}), frozenset({'b', 'sd'}), frozenset({'sd'}), frozenset({'aa', 'aa^r', 'sv'}), frozenset({'sv'}), frozenset({'b', 'b^r'}), frozenset({'%', 'sd'}), frozenset({'ba', 'sv'}), frozenset({'%', 'b'}), frozenset({'%', 'qy'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'sd'}), frozenset({'sv'}), frozenset({'ba'}), frozenset({'+'}), frozenset({'qw'}), frozenset({'sd'}), frozenset({'%', 'b^m', 'bk', 'sd'}), frozenset({'b'}), frozenset({'%', '+'}), frozenset({'ad', 'b'}), frozenset({'aa', 'sd'}), frozenset({'sd', 'sv'}), frozenset({'+'}), frozenset({'+'}), frozenset({'b', 'b^r'}), frozenset({'sd'}), frozenset({'%', 'qy'}), frozenset({'%', 'sd'}), frozenset({'b', 'b^r', 'qo', 'sd'}), frozenset({'sd'}), frozenset({'%'}), frozenset({'sd', 'sv'}), frozenset({'%'}), frozenset({'sv'}), frozenset({'sd'}), frozenset({'sd'}), frozenset({'b', 'b^r'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'b', 'b^r'}), frozenset({'sd'}), frozenset({'sd'}), frozenset({'%'}), frozenset({'+', 'sd'}), frozenset({'b'}), frozenset({'+'}), frozenset({'b', 'sd'}), frozenset({'+'}), frozenset({'qy'}), frozenset({'+'}), frozenset({'+'}), frozenset({'sd'}), frozenset({'bh'}), frozenset({'sd'}), frozenset({'b', 'b^r'}), frozenset({'%', '+'}), frozenset({'b', 'qy^g'}), frozenset({'ny', 'ny^r'}), frozenset({'sv'}), frozenset({'qh', 'sv'}), frozenset({'aa', 'sv'}), frozenset({'%', 'b', 'b^r'}), frozenset({'sv'}), frozenset({'aa'}), frozenset({'sd'}), frozenset({'%', 'aa', 'sd'}), frozenset({'sv'}), frozenset({'aa'}), frozenset({'sv'}), frozenset({'sd'}), frozenset({'aa', 'qh', 'sv'}), frozenset({'aa'}), frozenset({'+'}), frozenset({'sd(^q)'}), frozenset({'+'}), frozenset({'+'}), frozenset({'%'}), frozenset({'sd'}), frozenset({'aa', 'sd', 'sv'}), frozenset({'b'}), frozenset({'+'}), frozenset({'ba'}), frozenset({'sd'}), frozenset({'x'}), frozenset({'%', 'sd'}), frozenset({'fe', 'qy'}), frozenset({'sd'}), frozenset({'%', '+'}), frozenset({'nn', 'sd^e'}), frozenset({'%', 'sd', 'x'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd', 'sv'}), frozenset({'aa', 'sd'})
        ],
        [
            frozenset({'o', 'qrr', 'qw', 'sd', 'sv'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'+'}), frozenset({'aa'}), frozenset({'sd'}), frozenset({'b', 'sd'}), frozenset({'b'}), frozenset({'sd', 'sd(^q)'}), frozenset({'x'}), frozenset({'%', 'sd'}), frozenset({'sv'}), frozenset({'aa', 'sd'}), frozenset({'b'}), frozenset({'h', 'sd'})
        ]
    ]

    normalizedMinimalSupport = percentToFloat(minSupport)

    alg = GSP(transactions = transactions, minsup = normalizedMinimalSupport)
    result = alg.run_alg()

    data = {
        "content": "generalized-sequential-pattern.jinja",
        "title": title,
        "start_date": startDate,
        "end_date": endDate,
        "transactions": transactions,
        "minimal_support": minSupport,
        "normalized_minimal_support": normalizedMinimalSupport,
        "result": result
    }

    return render_template('index.jinja', data = data, os = os)
