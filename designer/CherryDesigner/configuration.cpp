#include "configuration.h"
#include "ui_configuration.h"

Configuration::Configuration(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Configuration)
{
    ui->setupUi(this);
}

Configuration::~Configuration()
{
    delete ui;
}
