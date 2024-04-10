#include <QtWidgets>

class Calculator : public QWidget
{
public:
    Calculator(QWidget *parent = nullptr)
        : QWidget(parent)
    {
        // Create the input field
        input_field = new QLineEdit(this);

        // Create the buttons
        btn_1 = new QPushButton("1", this);
        btn_2 = new QPushButton("2", this);
        btn_3 = new QPushButton("3", this);
        btn_4 = new QPushButton("4", this);
        btn_5 = new QPushButton("5", this);
        btn_6 = new QPushButton("6", this);
        btn_7 = new QPushButton("7", this);
        btn_8 = new QPushButton("8", this);
        btn_9 = new QPushButton("9", this);
        btn_0 = new QPushButton("0", this);
        btn_clear = new QPushButton("C", this);
        btn_add = new QPushButton("+", this);
        btn_subtract = new QPushButton("-", this);
        btn_multiply = new QPushButton("*", this);
        btn_divide = new QPushButton("/", this);
        btn_equals = new QPushButton("=", this);

        // Create the layout
        QVBoxLayout *vbox = new QVBoxLayout(this);
        QHBoxLayout *hbox1 = new QHBoxLayout();
        QHBoxLayout *hbox2 = new QHBoxLayout();
        QHBoxLayout *hbox3 = new QHBoxLayout();
        QHBoxLayout *hbox4 = new QHBoxLayout();
        QHBoxLayout *hbox5 = new QHBoxLayout();

        hbox1->addWidget(input_field);

        hbox2->addWidget(btn_1);
        hbox2->addWidget(btn_2);
        hbox2->addWidget(btn_3);
        hbox2->addWidget(btn_add);

        hbox3->addWidget(btn_4);
        hbox3->addWidget(btn_5);
        hbox3->addWidget(btn_6);
        hbox3->addWidget(btn_subtract);

        hbox4->addWidget(btn_7);
        hbox4->addWidget(btn_8);
        hbox4->addWidget(btn_9);
        hbox4->addWidget(btn_multiply);

        hbox5->addWidget(btn_clear);
        hbox5->addWidget(btn_0);
        hbox5->addWidget(btn_equals);
        hbox5->addWidget(btn_divide);

        vbox->addLayout(hbox1);
        vbox->addLayout(hbox2);
        vbox->addLayout(hbox3);
        vbox->addLayout(hbox4);
        vbox->addLayout(hbox5);

        setLayout(vbox);

        // Connect the signals to the slots
        connect(btn_0, &QPushButton::clicked, this, &Calculator::input_0);
        connect(btn_1, &QPushButton::clicked, this, &Calculator::input_1);
        connect(btn_2, &QPushButton::clicked, this, &Calculator::input_2);
        connect(btn_3, &QPushButton::clicked, this, &Calculator::input_3);
        connect(btn_4, &QPushButton::clicked, this, &Calculator::input_4);
        connect(btn_5, &QPushButton::clicked, this, &Calculator::input_5);
        connect(btn_6, &QPushButton::clicked, this, &Calculator::input_6);
        connect(btn_7, &QPushButton::clicked, this, &Calculator::input_7);
        connect(btn_8, &QPushButton::clicked, this, &Calculator::input_8);
        connect(btn_9, &QPushButton::clicked, this, &Calculator::input_9);
        connect(btn_add, &QPushButton::clicked, this, &Calculator::input_add);
        connect(btn_subtract, &QPushButton::clicked, this, &Calculator::input_subtract);
        connect(btn_multiply, &QPushButton::clicked, this, &Calculator::input_multiply);
        connect(btn_divide, &QPushButton::clicked, this, &Calculator::input_divide);
        connect(btn_clear, &QPushButton::clicked, this, &Calculator::clear);
        connect(btn_equals, &QPushButton::clicked, this, &Calculator::calculate);
    }

private:
    QLineEdit *input_field;
    QPushButton *btn_1, *btn_2, *btn_3, *btn_4, *btn_5, *btn_6, *btn_7, *btn_8, *btn_9, *btn_0;
    QPushButton *btn_clear, *btn_add, *btn_subtract, *btn_multiply, *btn_divide, *btn_equals;

    QString current_input;

    void input(QString value)
    {
        current_input += value;
        input_field->setText(current_input);
    }

    void input_0() { input("0"); }
    void input_1() { input("1"); }
    void input_2() { input("2"); }
    void input_3() { input("3"); }
    void input_4() { input("4"); }
    void input_5() { input("5"); }
    void input_6() { input("6"); }
    void input_7() { input("7"); }
    void input_8() { input("8"); }
    void input_9() { input("9"); }
    void input_add() { input("+"); }
    void input_subtract() { input("-"); }
    void input_multiply() { input("*"); }
    void input_divide() { input("/"); }

    void clear()
    {
        current_input = "";
        input_field->setText("");
    }

    void calculate()
    {
        QString expression = input_field->text();
        bool ok;
        double result = expression.toDouble(&ok);
        if (!ok) {
            // Handle the case where the input is not a valid number
            input_field->setText("Error");
            return;
        }

        // Evaluate the expression
        QStringList tokens = expression.split(QRegularExpression("[+\\-*/]"), QString::SkipEmptyParts);
        QStringList operators = expression.split(QRegularExpression("[0-9\\.]+"), QString::SkipEmptyParts);
        for (int i = 0; i < operators.size(); i++) {
            QString op = operators[i];
            if (op == "+")
                result += tokens[i+1].toDouble();
            else if (op == "-")
                result -= tokens[i+1].toDouble();
            else if (op == "*")
                result *= tokens[i+1].toDouble();
            else if (op == "/")
                result /= tokens[i+1].toDouble();
        }

        // Display the result
        input_field->setText(QString::number(result));
    }
};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    Calculator calculator;
    calculator.show();

    return app.exec();
}
