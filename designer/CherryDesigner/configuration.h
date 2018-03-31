#ifndef CONFIGURATION_H
#define CONFIGURATION_H

#include <QWidget>

namespace Ui {
class Configuration;
}

class Configuration : public QWidget
{
    Q_OBJECT

public:
    explicit Configuration(QWidget *parent = 0);
    ~Configuration();

private:
    Ui::Configuration *ui;
};

#endif // CONFIGURATION_H
