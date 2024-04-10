#include <QtWidgets>

class Calculator : public QWidget
{
    Q_OBJECT

public:
    Calculator(QWidget *parent = nullptr);

private slots:
    void digitClicked();
    void operatorClicked();
    void equalsClicked();
    void clearClicked();

private:
    QLineEdit *display;
    QPushButton *digitButtons[10];
    QPushButton *addButton, *subtractButton, *multiplyButton, *divideButton;
    QPushButton *equalsButton, *clearButton;

    QString pendingOperator;
    double pendingValue;

    void calculate(double rightOperand, const QString &pendingOperator);

    double sumOperand, subOperand, multOperand, divOperand;
};

Calculator::Calculator(QWidget *parent)
    : QWidget(parent), pendingValue(0.0), sumOperand(0.0), subOperand(0.0), multOperand(0.0), divOperand(0.0)
{
    display = new QLineEdit("0");
    display->setReadOnly(true);
    display->setAlignment(Qt::AlignRight);
    display->setMaxLength(15);

    QGridLayout *gridLayout = new QGridLayout;
    gridLayout->addWidget(display, 0, 0, 1, 4);

    for (int i = 0; i < 10; ++i) {
        digitButtons[i] = new QPushButton(QString::number(i));
        connect(digitButtons[i], SIGNAL(clicked())), this, SLOT(digitClicked()));
        gridLayout->addWidget(digitButtons[i], 4 - (i / 3), i % 3, 1, 1);
    }

    addButton = new QPushButton("+");
    subtractButton = new QPushButton("-");
    multiplyButton = new QPushButton("*");
    divideButton = new QPushButton("/");
    equalsButton = new QPushButton("=");
    clearButton = new QPushButton("C");

    connect(addButton, SIGNAL(clicked()), this, SLOT(operatorClicked()));
    connect(subtractButton, SIGNAL(clicked()), this, SLOT(operatorClicked()));
    connect(multiplyButton, SIGNAL(clicked()), this, SLOT(operatorClicked()));
    connect(divideButton, SIGNAL(clicked()), this, SLOT(operatorClicked()));
    connect(equalsButton, SIGNAL(clicked()), this, SLOT(equalsClicked()));
    connect(clearButton, SIGNAL(clicked()), this, SLOT(clearClicked()));

    gridLayout->addWidget(addButton, 1, 3, 1, 1);
    gridLayout->addWidget(subtractButton, 2, 3, 1, 1);
    gridLayout->addWidget(multiplyButton, 3, 3, 1, 1);
    gridLayout->addWidget(divideButton, 4, 3, 1, 1);
    gridLayout->addWidget(equalsButton, 4, 2, 1, 1);
    gridLayout->addWidget(clearButton, 4, 1, 1, 1);

    setLayout(gridLayout);
}

void Calculator::digitClicked()
{
    QPushButton *clickedButton = qobject_cast<QPushButton *>(sender());
    int digitValue = clickedButton->text().toInt();

    if (display->text() == "0" && digitValue == 0.0)
        return;

    if (display->text() == "0")
        display->setText(QString::number(digitValue));
    else
        display->setText(display->text() + QString::number(digitValue));
}

void Calculator::operatorClicked()
{
    QPushButton *clickedButton = qobject_cast<QPushButton *>(sender());
    QString clickedOperator = clickedButton->text();

    double operand = display->text().toDouble();
    calculate(operand, pendingOperator);

    pendingOperator = clickedOperator;
    display->setText(QString::number(pendingValue));
}

void Calculator::equalsClicked()
{
    double operand = display->text().toDouble();
    calculate(operand, pendingOperator);
    display->setText(QString::number(pendingValue));
    pendingValue = 0.0;
    pendingOperator.clear();
}

void Calculator::clearClicked()
{
    display->setText("0");
    pendingValue = 0.0;
    pendingOperator.clear();
}

void Calculator::calculate(double rightOperand, const QString &pendingOperator)
{
    if (pendingOperator == "+")
        pendingValue += rightOperand;
    else if (pendingOperator == "-")
        pendingValue -= rightOperand;
    else if (pendingOperator == "*")
        pendingValue *= rightOperand;
    else if (pendingOperator == "/") {
        if (rightOperand == 0.0) {
            display->setText("Error: Divide by zero");
            pendingValue = 0.0;
            pendingOperator.clear();
            return;
        }
        pendingValue /= rightOperand;
    }
    else
        pendingValue = rightOperand;
}

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    Calculator calculator;
    calculator.setWindowTitle("Simple Calculator");
    calculator.show();

    return app.exec();
}

#include "main.moc"
